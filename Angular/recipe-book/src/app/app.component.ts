import { Component } from '@angular/core';
import { LoggingService } from './shared/logging.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [LoggingService],
})
export class AppComponent {
  constructor(private loggingService: LoggingService) {
    this.loggingService.dataAdded.subscribe((event: string) =>
      alert('Added a new Item object : ' + event)
    );
  }
  userSelection: string = 'Recipe';

  onEventUserSelection(event) {
    this.loggingService.logUserInput(event);
    this.userSelection = event;
  }
}
