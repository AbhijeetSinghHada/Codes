import {
  Component,
  ElementRef,
  EventEmitter,
  Output,
  ViewChild,
} from '@angular/core';
import { Ingredient } from 'src/app/shared/ingredient.model';

@Component({
  selector: 'app-shopping-edit',
  templateUrl: './shopping-edit.component.html',
  styleUrls: ['./shopping-edit.component.css'],
})
export class ShoppingEditComponent {
  @Output() eventIngredientAdd = new EventEmitter<Ingredient>();
  @ViewChild('nameInput') ingredientName: ElementRef;
  @ViewChild('amountInput') ingredientAmount: ElementRef;

  onAddClick() {
    this.eventIngredientAdd.emit({
      name: this.ingredientName.nativeElement.value,
      amount: this.ingredientAmount.nativeElement.value,
    });
  }
}
