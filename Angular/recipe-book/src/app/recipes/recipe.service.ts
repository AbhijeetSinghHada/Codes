import { Injectable } from '@angular/core';

import { Recipe } from './recipe.model';
import { Ingredient } from '../shared/ingredient.model';
import { ShoppingListService } from '../shopping-list/shopping-list.service';

@Injectable()
export class RecipeService {
  private recipes: Recipe[] = [
    new Recipe(
      'Tasty Schnitzel',
      'A super-tasty Schnitzel - just awesome!',
      'https://upload.wikimedia.org/wikipedia/commons/7/72/Schnitzel.JPG',
      [new Ingredient('Meat', 1), new Ingredient('French Fries', 20)]
    ),
    new Recipe(
      'Big Fat Burger',
      'What else you need to say?',
      'https://upload.wikimedia.org/wikipedia/commons/b/be/Burger_King_Angus_Bacon_%26_Cheese_Steak_Burger.jpg',
      [new Ingredient('Buns', 2), new Ingredient('Meat', 1)]
    ),
    new Recipe(
      'Kachori',
      'Kota kachori is a delicious snack from the city of Kota in Rajasthan, India. It is a deep-fried pastry stuffed with a spicy mixture of urad dal, onions, and spices. Kota kachori is crispy on the outside and soft on the inside, and has a unique flavor that makes it irresistible.',
      'https://th.bing.com/th/id/OIP.QCdLE9MFI3sxWaFWTHEaeAHaE8?pid=ImgDet&w=1500&h=1001&rs=1',
      [
        new Ingredient('Dal', 1),
        new Ingredient('Maida', 1),
        new Ingredient('Spices', 4),
      ]
    ),
    new Recipe(
      'Pav Bhaji',
      'Pav bhaji is a delicious and popular dish from India that consists of a thick vegetable curry (bhaji) served with a soft bread roll (pav).',
      'https://vegecravings.com/wp-content/uploads/2016/10/pav-bhaji-recipe-step-by-step-instructions.jpg.webp',
      [new Ingredient('Buns', 6), new Ingredient('All Veggies', 2)]
    ),
    new Recipe(
      'Chole Bhature',
      'Chole Bhature is a delicious and popular dish from India that consists of a spicy chickpea curry (chole) and a deep-fried bread (bhature).',
      'https://2.bp.blogspot.com/-OU_L_dlS_G0/Wx9rVpMKeVI/AAAAAAAAAEE/lL6pyCPBVoQkBxbpYZg9wRt6-Lce51C7ACLcBGAs/s1600/imperial%2Binn.jpg',
      [new Ingredient('Chole', 2), new Ingredient('Maida', 1)]
    ),
  ];

  constructor(private slService: ShoppingListService) {}

  getRecipes() {
    return this.recipes.slice();
  }

  getRecipe(index: number) {
    return this.recipes[index];
  }

  addIngredientsToShoppingList(ingredients: Ingredient[]) {
    this.slService.addIngredients(ingredients);
  }
}
