import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { RecipesComponent } from './recipes/recipes.component';
import { RecipeListComponent } from './recipes/recipe-list/recipe-list.component';
import { RecipeItemComponent } from './recipes/recipe-list/recipe-item/recipe-item.component';
import { ShoppingListComponent } from './shopping-list/shopping-list.component';
import { ShoppingEditComponent } from './shopping-list/shopping-edit/shopping-edit.component';
import { RecipeDetailsComponent } from './recipes/recipe-details/recipe-details.component';
import { DropdownDirective } from './shared/dropdown.directive';
import { TestingDirective } from './shared/testing.directive';
import { FormsModule } from '@angular/forms';
import { AppRouteModule } from './app-route.module';
import { WarningRecipeComponent } from './warningrecipe/warningrecipe.component';
import { RecipeEditComponent } from './recipes/recipe-edit/recipe-edit.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    RecipesComponent,
    RecipeListComponent,
    RecipeItemComponent,
    ShoppingListComponent,
    ShoppingEditComponent,
    RecipeDetailsComponent,
    DropdownDirective,
    TestingDirective,
    WarningRecipeComponent,
    RecipeEditComponent,
  ],
  imports: [BrowserModule, FormsModule, AppRouteModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
