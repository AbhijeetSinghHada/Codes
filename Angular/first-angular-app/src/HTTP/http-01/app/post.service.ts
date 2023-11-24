import { Injectable } from '@angular/core';
import {
  HttpClient,
  HttpEventType,
  HttpHeaders,
  HttpParams,
} from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';
import { Subject, throwError } from 'rxjs';
@Injectable({ providedIn: 'root' })
export class PostService {
  error = new Subject<string>();
  constructor(private http: HttpClient) {}
  createAndStorePost(postData) {
    return this.http
      .post(
        'https://angular-http-course-2457f-default-rtdb.asia-southeast1.firebasedatabase.app/posts.json',
        postData,
        {
          observe: 'response',
        }
      )
      .subscribe(
        (data) => {
          console.log(data);
        },
        (error) => {
          this.error.next(error.message);
        }
      );
  }
  fetchPosts() {
    return this.http
      .get(
        'https://angular-http-course-2457f-default-rtdb.asia-southeast1.firebasedatabase.app/posts.json',
        {
          headers: new HttpHeaders({
            'Auhorizationsadfb-wfed': 'Helloooooo',
            dwfgefw: 'wfeggefw',
          }),
          params: new HttpParams()
            .set('slot-type', 'LMV')
            .append('kittu', 'dada'),
        }
      )
      .pipe(
        map(
          (responseData: {
            [key: string]: { username: string; password: string; id?: string };
          }) => {
            const postsArray = [];
            for (let key in responseData) {
              if (responseData.hasOwnProperty(key)) {
                postsArray.push({ ...responseData[key], id: key });
              }
            }
            return postsArray;
          }
        ),
        catchError((errorRef) => {
          console.log(errorRef);
          return throwError(errorRef);
        })
      );
  }
  clearPosts() {
    return this.http
      .delete(
        'https://angular-http-course-2457f-default-rtdb.asia-southeast1.firebasedatabase.app/posts.json',
        { observe: 'events' }
      )
      .pipe(
        tap((event) => {
          if (event.type === HttpEventType.Sent) {
            console.log('Sent : ');
          }
          if (event.type === HttpEventType.Response) {
            console.log(event.body);
          }
        })
      );
  }
}
