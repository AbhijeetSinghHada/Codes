import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { UsersComponent } from './users/users.component';
import { UserComponent } from './users/user/user.component';
import { ServersComponent } from './servers/servers.component';
import { ServerComponent } from './servers/server/server.component';
import { EditServerComponent } from './servers/edit-server/edit-server.component';
import { canActivate } from './auth-guard.service';
const appRoutes: Routes = [
  { path: '', component: HomeComponent },
  {
    path: 'users',
    component: UsersComponent,
    children: [{ path: ':id/:name', component: UserComponent }],
  },
  {
    path: 'servers',
    // canActivate: [canActivate],
    canActivateChild: [canActivate],
    component: ServersComponent,
    children: [
      { path: ':id', component: ServerComponent },
      { path: ':id/edit', component: EditServerComponent },
    ],
  },
  { path: '**', redirectTo: '', pathMatch: 'full' },
];
@NgModule({
  imports: [RouterModule.forRoot(appRoutes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
