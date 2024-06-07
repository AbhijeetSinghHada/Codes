import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription, interval } from 'rxjs';
import { Observable } from 'rxjs-compat';
import { filter, map } from 'rxjs/operators';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit, OnDestroy {
  private firstSubscription: Subscription;
  private testObservable: Observable<any>;
  customObser;
  constructor() {}

  ngOnInit() {
    // this.firstSubscription = interval(1000).subscribe((count: number) => {
    //   console.log(count);
    // });
    this.testObservable = new Observable((observer) => {
      let count = 0;
      setInterval(() => {
        observer.next(count);
        if (count == 6) {
          observer.error('Greater than 6');
        }
        count++;
      }, 800);
    });

    const newObservable = this.testObservable
      .pipe(
        map((data: any) => {
          return data ** 2;
        }),
        filter((data: number) => {
          return data % 2 != 0;
        })
      )
      .subscribe(
        (value) => {
          console.log(value);
        },
        (error) => {
          console.log(error);
          alert(error);
        }
      );

    let new_Observable = new Observable((subscriber_) => {
      setInterval(() => {
        subscriber_.next(20);
      }, 2000);
      subscriber_.error();
      subscriber_.complete();
    });

    new_Observable.subscribe((data) => {});
    // this.firstSubscription = this.testObservable.subscribe(
    //   (value) => {
    //     console.log(value);
    //   },
    //   (error) => {
    //     console.log(error);
    //     alert(error);
    //   }
    // );
    this.customObser = new Observable((subscriber) => {
      let count = 0;
      setInterval(() => {
        const lists = ['Hello ', 'World ', count];
        subscriber.next(lists);
        count++;
      }, 500);
    });

    // this.customObser.subscribe((value: Array<any>) => {
    //   console.log(value.join().replaceAll(',', ''));
    // });
  }

  ngOnDestroy() {
    this.firstSubscription.unsubscribe();
  }
}

import { Directive } from '@angular/core';

@Directive({ selector: '[selector-name]' })
export class NameDirective {
  constructor() {}
}
