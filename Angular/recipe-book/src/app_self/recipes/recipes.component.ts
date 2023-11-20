import { Component } from '@angular/core';
import { Recipe } from './recipes.model';
import { RecipeService } from './recipe.service';
import { Subscription } from 'rxjs';
@Component({
  selector: 'app-recipes',
  templateUrl: './recipes.component.html',
  styleUrls: ['./recipes.component.css'],
  providers: [RecipeService],
})
export class RecipesComponent {
  recipeSubcription: Subscription;
  constructor(private recipeService: RecipeService) {
    this.recipeSubcription = this.recipeService.selectedRecipeDetails.subscribe(
      (recipe: Recipe) => (this.recipeDetails = recipe)
    );
  }
  recipeDetails: Recipe;

  ngOnDestroy() {
    this.recipeSubcription.unsubscribe();
  }
}
