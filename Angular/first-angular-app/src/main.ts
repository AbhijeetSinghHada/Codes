import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './signals/app.component';
import { importProvidersFrom } from '@angular/core';
import { AppRoutingModule } from './standalone-components-routing/app-routing.module';

import { AppModule } from './animations/app.module';

platformBrowserDynamic()
  .bootstrapModule(AppModule)
  .catch((err) => console.error(err));

// bootstrapApplication(AppComponent, {
//   providers: [importProvidersFrom(AppRoutingModule)],
// });
// bootstrapApplication(AppComponent);
