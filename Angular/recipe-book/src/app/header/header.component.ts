import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./heder.component.css'],
})
export class HeaderComponent {
  collapsed = true;
  @Output() eventUserSelection = new EventEmitter<string>();
  onToggleRecipe(event) {
    this.eventUserSelection.emit(event.target.innerText);
  }
  onToggleShoppingList(event) {
    this.eventUserSelection.emit(event.target.innerText);
  }
}
