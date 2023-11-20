import { Ingredient } from '../shared/ingredient.model';
import { Subject } from 'rxjs';

export class ShoppingListService {
  ingredientsExchangeEvent = new Subject<Ingredient[]>();

  ingredients: Ingredient[] = [
    new Ingredient('Apples', 5),
    new Ingredient('Tomataos', 10),
  ];

  addIngredient(ingredient: Ingredient) {
    this.ingredients.push(ingredient);
    this.ingredientsExchangeEvent.next(this.ingredients.slice());
  }
  getIngredients() {
    return this.ingredients.slice();
  }
}
