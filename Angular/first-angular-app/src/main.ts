import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { AppModule } from './HTTP/http-01/app/app.module';

platformBrowserDynamic()
  .bootstrapModule(AppModule)
  .catch((err) => console.error(err));
