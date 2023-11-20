import { Component } from '@angular/core';
import { Ingredient } from '../shared/ingredient.model';
import { LoggingService } from '../shared/logging.service';
import { ShoppingListService } from './shopping-list.service';
import { RecipeService } from '../recipes/recipe.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-shopping-list',
  templateUrl: './shopping-list.component.html',
  styleUrls: ['./shopping-list.component.css'],
})
export class ShoppingListComponent {
  shoppingListExcSubject: Subscription;
  constructor(
    private loggingService: LoggingService,
    private shoppingListService: ShoppingListService
  ) {
    this.ingredients = this.shoppingListService.getIngredients();
    this.shoppingListExcSubject =
      shoppingListService.ingredientsExchangeEvent.subscribe((ingredients) =>
        this.addIngredients(ingredients)
      );
  }
  ingredients: Ingredient[];

  addIngredients(ingredientsList) {
    console.log('in add ingredients');
    for (let ingredient of ingredientsList) {
      this.shoppingListService.addIngredient(ingredient);
    }
    this.ingredients = this.shoppingListService.getIngredients();
  }

  onAddClick(event) {
    this.loggingService.dataAdded.emit(JSON.stringify(event));
    this.shoppingListService.addIngredient(event);
    this.ingredients = this.shoppingListService.getIngredients();
  }
  ngOnDestroy() {
    this.shoppingListExcSubject.unsubscribe();
  }
}
