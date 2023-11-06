import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-even',
  templateUrl: 'even.component.html',
})
export class EvenComponent {
  @Input() value: number;
}
