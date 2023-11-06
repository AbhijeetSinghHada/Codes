import { EventEmitter } from '@angular/core';

export class LoggingService {
  count = 0;
  dataAdded = new EventEmitter<string>();
  logUserInput(userData: object) {
    console.log(
      'User Added Certain Data : ' +
        JSON.stringify(userData) +
        ' cp : ' +
        this.count++
    );
  }
}
