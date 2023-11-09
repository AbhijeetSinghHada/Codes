import { Component, Input } from '@angular/core';
import { Recipe } from '../recipes.model';
import { RecipeService } from '../recipe.service';
import { ShoppingListService } from 'src/app/shopping-list/shopping-list.service';

@Component({
  selector: 'app-recipe-detail',
  templateUrl: './recipe-details.component.html',
  styleUrls: ['./recipe-details.component.css'],
})
export class RecipeDetailsComponent {
  constructor(
    private recipeService: RecipeService,
    private shoppingListService: ShoppingListService
  ) {
    this.recipeService.selectedRecipeDetails.subscribe(
      (recipe: Recipe) => (this.recipeDetails = recipe)
    );
  }
  recipeDetails: Recipe;
  onShoppingListClick() {
    this.shoppingListService.ingredientsExchangeEvent.emit(
      this.recipeDetails.ingredients
    );
  }
  // ngAfterViewChecked() {
  //   console.log('ngAfterViewChecked called - recipeDetails');
  // }
  // ngAfterContentChecked() {
  //   console.log('ngAfterContentChecked called - recipeDetails');
  // }
}
