import { Component } from '@angular/core';
import { Subscription } from 'rxjs';

import { UserService } from '../user.service';
import { UserModel } from '../user.model';

@Component({
  selector: 'app-display-data',
  templateUrl: './display-data.component.html',
  styleUrls: ['./display-data.component.css'],
})
export class DisplayDataComponent {
  userData: UserModel;
  userObservableSubscription: Subscription;
  constructor(private userService: UserService) {}
  ngOnInit() {
    this.userData = this.userService.user;
    this.userObservableSubscription = this.userService.observable.subscribe(
      (data) => {
        console.log(data);
        this.userData = JSON.parse(JSON.stringify(data));
      }
    );
  }
  ngOnDestory() {
    this.userObservableSubscription.unsubscribe();
  }
}
