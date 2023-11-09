import {
  Component,
  EventEmitter,
  Input,
  OnChanges,
  Output,
} from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./heder.component.css'],
})
export class HeaderComponent {
  collapsed = true;
  @Output() eventUserSelection = new EventEmitter<string>();
  @Input() name1: string;
  onToggleRecipe(event) {
    this.eventUserSelection.emit(event.target.innerText);
  }
  onToggleShoppingList(event) {
    this.eventUserSelection.emit(event.target.innerText);
  }
}
