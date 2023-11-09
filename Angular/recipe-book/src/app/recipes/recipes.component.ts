import { Component } from '@angular/core';
import { Recipe } from './recipes.model';
import { RecipeService } from './recipe.service';
@Component({
  selector: 'app-recipes',
  templateUrl: './recipes.component.html',
  styleUrls: ['./recipes.component.css'],
  providers: [RecipeService],
})
export class RecipesComponent {
  constructor(private recipeService: RecipeService) {
    this.recipeService.selectedRecipeDetails.subscribe((recipe) => {
      this.recipeDetails = recipe;
    });
  }
  recipeDetails: Recipe;
  onRecipeDetailsFetched(event) {
    this.recipeDetails = event;
  }
  // ngAfterViewChecked() {
  //   console.log('ngAfterViewChecked called - recipe');
  // }
  // ngAfterContentChecked() {
  //   console.log('ngAfterContentChecked called - recipe');
  // }
}
