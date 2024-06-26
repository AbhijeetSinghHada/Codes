import { Injectable } from '@angular/core';

@Injectable({
    providedIn: 'root',
})
export class LoggerService {
    messages: string[] = [];
    constructor() {}

    log(message: string): any {
        this.messages.push(message);
    }
    clear() {
        this.messages = [];
    }
}
