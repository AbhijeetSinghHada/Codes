import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  // name = 'first-angular-app';
  // serverNumber = Math.floor(Math.random() * 999);
  // serverhello() {
  //   return { hello: 'jii' }.hello;
  // }
  even: number[] = [];
  odd: number[] = [];

  OnIncrementEvent(event) {
    if (event.value % 2 == 0) {
      this.even.push(event.value);
    } else {
      this.odd.push(event.value);
    }
  }
}
