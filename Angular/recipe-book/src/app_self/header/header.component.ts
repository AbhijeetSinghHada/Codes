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
  @Input() name1: string;
}
