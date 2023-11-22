import { BehaviorSubject, Observable, Subject } from 'rxjs';
import { Injectable } from '@angular/core';

import { UserModel } from './user.model';

@Injectable({ providedIn: 'root' })
export class UserService {
  public userSubject: BehaviorSubject<any> = new BehaviorSubject({});

  public observable: Observable<any> = this.userSubject.asObservable();
  user: UserModel;
  constructor() {
    this.user = new UserModel('Abhi', 1, 'Admin', []);
    this.userSubject.next(this.user);
  }
  getUserDetails() {
    return this.user;
  }
}
