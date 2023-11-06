import { Component, EventEmitter, Output } from '@angular/core';
import { Recipe } from './recipes.model';
@Component({
  selector: 'app-recipes',
  templateUrl: './recipes.component.html',
  styleUrls: ['./recipes.component.css'],
})
export class RecipesComponent {
  recipeDetails: Recipe;
  onRecipeDetailsFetched(event) {
    this.recipeDetails = event;
  }
}
