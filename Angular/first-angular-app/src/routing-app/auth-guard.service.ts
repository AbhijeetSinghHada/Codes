import { inject } from '@angular/core';
import {
  ActivatedRouteSnapshot,
  CanActivateChildFn,
  CanActivateFn,
  Router,
  RouterStateSnapshot,
} from '@angular/router';
import { AuthService } from './auth.service';

export const canActivate: CanActivateFn = (
  route: ActivatedRouteSnapshot,
  state: RouterStateSnapshot
) => {
  const authService = inject(AuthService);
  const router = inject(Router);

  return authService.isAuthenticated().then((authenticated: boolean) => {
    if (authenticated) {
      return true;
    } else {
      router.navigate(['/']);
    }
  });
};
export const canActivateChild: CanActivateChildFn = (
  route: ActivatedRouteSnapshot,
  state: RouterStateSnapshot
) => {
  return canActivate(route, state);
};
