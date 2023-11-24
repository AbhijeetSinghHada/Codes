import { Component, OnInit, ElementRef, ViewChild } from '@angular/core';

import { Ingredient } from '../../shared/ingredient.model';
import { ShoppingListService } from '../shopping-list.service';
import { NgForm } from '@angular/forms';
import { NgFor } from '@angular/common';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-shopping-edit',
  templateUrl: './shopping-edit.component.html',
  styleUrls: ['./shopping-edit.component.css'],
})
export class ShoppingEditComponent implements OnInit {
  @ViewChild('f') form: NgForm;
  subscriptionEditiing: Subscription;
  editIngredient: Ingredient;
  editedItemIndex: number;
  editingMode: boolean = false;
  constructor(private slService: ShoppingListService) {}
  ngOnInit() {
    this.subscriptionEditiing = this.slService.editingIngredient.subscribe(
      (data) => {
        this.editedItemIndex = data;
        this.editingMode = true;
        this.editIngredient = this.slService.getIngredient(data);
        this.form.setValue({
          name: this.editIngredient.name,
          amount: this.editIngredient.amount,
        });
      }
    );
  }

  onAddItem(form: NgForm) {
    const ingName = form.value.name;
    const ingAmount = form.value.amount;
    const newIngredient = new Ingredient(ingName, ingAmount);

    if (this.editingMode) {
      this.slService.updateIngredient(this.editedItemIndex, newIngredient);
    } else {
      this.slService.addIngredient(newIngredient);
    }
    form.reset();
    this.editingMode = false;
  }
  onClear() {
    this.form.reset();
    this.editingMode = false;
  }
  onDelete() {
    this.slService.deleteIngredient(this.editedItemIndex);
    this.onClear();
  }
  ngOnDestroy() {
    this.subscriptionEditiing.unsubscribe();
  }
}
