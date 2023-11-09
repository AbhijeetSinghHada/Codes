import { Component, Input, ViewChild } from '@angular/core';
import { LoggingService } from './shared/logging.service';
import { ShoppingListService } from './shopping-list/shopping-list.service';
import { count } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [LoggingService, ShoppingListService],
})
export class AppComponent {
  constructor(private loggingService: LoggingService) {
    this.loggingService.dataAdded.subscribe((event: string) =>
      alert('Added a new Item object : ' + event)
    );
  }
  userSelection: string = 'Recipe';
  onEventUserSelection(event: any) {
    this.loggingService.logUserInput(event);
    this.userSelection = event;
  }
}
