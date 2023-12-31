import {
  HttpEventType,
  HttpHandler,
  HttpInterceptor,
  HttpRequest,
} from '@angular/common/http';
import { tap } from 'rxjs/operators';

export class AuthInterceptorService implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler) {
    console.log(req.url);
    const modifiedRequest = req.clone({
      headers: req.headers.append('hii', 'hello'),
    });

    return next.handle(modifiedRequest).pipe(
      tap((event) => {
        console.log(event);
        if (event.type === HttpEventType.Response) {
          console.log(event.body);
        }
      })
    );
  }
}
