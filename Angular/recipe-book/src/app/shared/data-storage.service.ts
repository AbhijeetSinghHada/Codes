import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { RecipeService } from '../recipes/recipe.service';
import { Subject, exhaustMap, map, take, tap } from 'rxjs';
import { AuthService } from '../auth/auth.service';

@Injectable({ providedIn: 'root' })
export class DataStorageService {
  constructor(
    private http: HttpClient,
    private recipeService: RecipeService,
    private authService: AuthService
  ) {}
  currentDataIndex;
  recipeFetchSubject = new Subject();
  storeRecipes() {
    let recipes = this.recipeService.getRecipes();

    this.http
      .put(
        'https://recipe-project-5248b-default-rtdb.firebaseio.com/recipes.json',
        recipes
      )
      .subscribe();
  }
  fetchRecipes() {
    return this.authService.user.pipe(
      take(1),
      exhaustMap((user) => {
        return this.http.get(
          'https://recipe-project-5248b-default-rtdb.firebaseio.com/recipes.json'
        );
      }),
      map((recipes: Array<any>) => {
        return recipes.map((recipe) => {
          return {
            ...recipe,
            ingredients: recipe.ingredients ? recipe.ingredients : [],
          };
        });
      }),
      tap((response) => {
        this.recipeService.updateAllRecipes(response);
      })
    );
  }
}
