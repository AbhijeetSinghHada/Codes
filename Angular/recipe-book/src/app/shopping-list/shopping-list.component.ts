import { Component } from '@angular/core';
import { Ingredient } from '../shared/ingredient.model';
import { LoggingService } from '../shared/logging.service';

@Component({
  selector: 'app-shopping-list',
  templateUrl: './shopping-list.component.html',
  styleUrls: ['./shopping-list.component.css'],
})
export class ShoppingListComponent {
  constructor(private loggingService: LoggingService) {}
  ingredients: Ingredient[] = [
    new Ingredient('Apples', 5),
    new Ingredient('Tomataos', 10),
  ];

  onAddClick(event) {
    this.loggingService.logUserInput(event);
    this.loggingService.dataAdded.emit(JSON.stringify(event));
    this.ingredients.push(event);
  }
}
