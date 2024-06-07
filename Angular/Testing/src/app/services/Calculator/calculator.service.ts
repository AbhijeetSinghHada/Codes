import { Injectable } from '@angular/core';
import { LoggerService } from '../logger/logger.service';

@Injectable({
    providedIn: 'root',
})
export class CalculatorService {
    constructor(private logger: LoggerService) {}
    add(x: number, y: number) {
        let result = x + y;
        let logResult = this.logger.log(
            `Add Method Called wiht params : ${x} nd ${y}`
        );
        // console.log(logResult);
        return result;
    }
    subtract(x: number, y: number) {
        let result = x - y;
        let logResult = this.logger.log(
            `Subtract Method Called wiht params : ${x} nd ${y}`
        );
        // console.log(
        //     logResult + ` Subtract Method Called wiht params : ${x} nd ${y}`
        // );
        return result;
    }
}
