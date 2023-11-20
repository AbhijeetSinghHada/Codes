import { Component, Input } from '@angular/core';
import { Recipe } from '../recipes.model';
import { RecipeService } from '../recipe.service';
import { ShoppingListService } from 'src/app/shopping-list/shopping-list.service';
import { ActivatedRoute, Params } from '@angular/router';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-recipe-detail',
  templateUrl: './recipe-details.component.html',
  styleUrls: ['./recipe-details.component.css'],
})
export class RecipeDetailsComponent {
  recipeDetails: Recipe;
  constructor(
    private recipeService: RecipeService,
    private shoppingListService: ShoppingListService,
    private route: ActivatedRoute
  ) {
    const id = this.route.snapshot.params['id'];
    this.recipeDetails = recipeService.fetchRecipeById(id);
    this.route.params.subscribe((params: Params) => {
      const id = params['id'];
      this.recipeDetails = recipeService.fetchRecipeById(id);
    });
  }
  onShoppingListClick() {
    console.log('on shoopuing list clicked');
    this.shoppingListService.ingredientsExchangeEvent.next(
      this.recipeDetails.ingredients
    );
  }
}
