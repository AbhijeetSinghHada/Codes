import { NgFor } from '@angular/common';
import { Component, effect, signal } from '@angular/core';

@Component({
  selector: 'app-signals',
  templateUrl: './signals.component.html',
  standalone: true,
  imports: [NgFor],
})
export class SignalsComponent {
  actions = signal<string[]>([]);
  counter = signal(0);

  constructor() {
    effect(() => {
      console.log(this.counter());
    });
  }

  increment() {
    this.counter.update((oldCounter) => oldCounter + 1);
    this.actions.mutate((oldValue) => oldValue.push('Increment'));
  }

  decrement() {
    // this.counter.set(this.counter() - 1);
    this.counter.set(this.counter() - 1);
    this.actions.mutate((oldValue) => oldValue.push('Decrement'));
  }
}
