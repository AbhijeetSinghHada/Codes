import { Recipe } from './recipes.model';
import { Ingredient } from '../shared/ingredient.model';
import { Subject } from 'rxjs';

export class RecipeService {
  selectedRecipeDetails = new Subject<Recipe>();
  private recipes: Recipe[] = [
    new Recipe(
      1,
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
      2,
      'Pav Bhaji',
      'Pav bhaji is a delicious and popular dish from India that consists of a thick vegetable curry (bhaji) served with a soft bread roll (pav).',
      'https://vegecravings.com/wp-content/uploads/2016/10/pav-bhaji-recipe-step-by-step-instructions.jpg.webp',
      [new Ingredient('Buns', 6), new Ingredient('All Veggies', 2)]
    ),
    new Recipe(
      3,
      'Chole Bhature',
      'Chole Bhature is a delicious and popular dish from India that consists of a spicy chickpea curry (chole) and a deep-fried bread (bhature).',
      'https://2.bp.blogspot.com/-OU_L_dlS_G0/Wx9rVpMKeVI/AAAAAAAAAEE/lL6pyCPBVoQkBxbpYZg9wRt6-Lce51C7ACLcBGAs/s1600/imperial%2Binn.jpg',
      [new Ingredient('Chole', 2), new Ingredient('Maida', 1)]
    ),
  ];

  getRecipes() {
    return this.recipes.slice();
  }
  fetchRecipeById(id: number) {
    return this.recipes[id - 1];
  }
}
