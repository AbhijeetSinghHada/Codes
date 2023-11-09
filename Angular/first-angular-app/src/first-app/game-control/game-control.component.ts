import { Component, EventEmitter, Output } from '@angular/core';
@Component({
  selector: 'app-game-control',
  templateUrl: 'game-control.component.html',
})
export class GameControlComponent {
  counter: number = 0;
  @Output() incrementingEvent = new EventEmitter<{ value: number }>();
  interval: any;
  startCounter() {
    this.interval = setInterval(() => {
      this.counter += 1;
      this.incrementingEvent.emit({
        value: this.counter,
      });
    }, 1000);
  }
  stopCounter() {
    clearInterval(this.interval);
  }
}
