import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { UserService } from './user.service';
import { DataService } from './data.service';

@Component({
  selector: 'app-user',
  standalone: true,
  imports: [CommonModule],
  providers: [UserService, DataService],
  templateUrl: './user.component.html',
  styleUrl: './user.component.css',
})
export class UserComponent {
  user: { name: string };
  isLoggedIn = true;
  data: string | undefined = undefined;
  constructor(
    private userService: UserService,
    private dataService: DataService
  ) {
    this.user = this.userService.user;
  }
  ngOnInit() {
    this.dataService.getData().then((data) => {
      this.data = data;
    });
  }
}
