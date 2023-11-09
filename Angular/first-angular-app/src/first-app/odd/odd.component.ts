import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-odd',
  templateUrl: 'odd.component.html',
})
export class OddComponent {
  @Input() value: Number;
}
