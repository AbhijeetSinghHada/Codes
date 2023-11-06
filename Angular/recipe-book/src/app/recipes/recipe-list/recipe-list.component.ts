import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { Recipe } from '../recipes.model';

@Component({
  selector: 'app-recipe-list',
  templateUrl: './recipe-list.component.html',
  styleUrls: ['./recipe-list.component.css'],
})
export class RecipeListComponent implements OnInit {
  recipes: Recipe[] = [
    new Recipe(
      'A Test Recipe 1',
      'This is a test Recipe maybe',
      'https://vegecravings.com/wp-content/uploads/2016/10/pav-bhaji-recipe-step-by-step-instructions.jpg.webp'
    ),
    new Recipe(
      'A Test Recipe 2',
      'This is a test Recipe maybe',
      'https://vegecravings.com/wp-content/uploads/2016/10/pav-bhaji-recipe-step-by-step-instructions.jpg.webp'
    ),
    new Recipe(
      'A Test Recipe 3',
      'This is a test Recipe maybe',
      'https://vegecravings.com/wp-content/uploads/2016/10/pav-bhaji-recipe-step-by-step-instructions.jpg.webp'
    ),
  ];
  @Output() selectedRecipeDetails = new EventEmitter<Recipe>();
  onRecipeDetailsFetched(event) {
    this.selectedRecipeDetails.emit(event);
  }
  constructor() {}
  ngOnInit() {}
}
