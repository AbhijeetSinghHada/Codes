import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { AuthResponseData, AuthService } from './auth.service';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
})
export class AuthComponent {
  constructor(private authService: AuthService, private router: Router) {}
  isLoginMode = true;
  isLoading = false;
  error = null;
  onSwitchMode() {
    this.isLoginMode = !this.isLoginMode;
  }
  onSubmit(authFrom: NgForm) {
    if (!authFrom.valid) {
      return;
    }
    this.isLoading = true;
    const email = authFrom.value.email;
    const password = authFrom.value.password;
    let authObservable: Observable<AuthResponseData>;
    if (this.isLoginMode) {
      authObservable = this.authService.login(email, password);
    } else {
      authObservable = this.authService.signup(email, password);
    }
    authObservable.subscribe({
      next: (data) => {
        this.isLoading = false;
        this.router.navigate(['/recipes']);
      },
      error: (error: Error) => {
        this.error = error.message;
        this.isLoading = false;
      },
    });
    authFrom.reset();
  }
}
