import { Component } from '@angular/core';
import { UserService } from '../user.service';
import { UserModel } from '../user.model';
import { ReimburesmentModel } from '../reimbursement.model';

@Component({
  selector: 'app-input-data',
  templateUrl: './input-data.component.html',
  styleUrls: ['./input-data.component.css'],
})
export class InputDataComponent {
  user: UserModel;
  constructor(private userService: UserService) {
    this.user = JSON.parse(JSON.stringify(userService.user));
  }
  onSubmit() {
    this.userService.userSubject.next(JSON.parse(JSON.stringify(this.user)));
  }
  onAdd() {
    this.user.reimburesment.push(
      new ReimburesmentModel(null, '', null, 'cash')
    );
  }
  onDelete(index: number) {
    this.user.reimburesment.splice(index, 1);
  }
}
