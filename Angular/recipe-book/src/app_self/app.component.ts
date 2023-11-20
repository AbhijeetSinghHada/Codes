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
export class AppComponent {}
