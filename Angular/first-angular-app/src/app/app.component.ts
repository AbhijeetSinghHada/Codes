import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  name = 'first-angular-app';
  serverNumber = Math.floor(Math.random() * 999);
  serverhello() {
    return { hello: 'jii' }.hello;
  }
}
