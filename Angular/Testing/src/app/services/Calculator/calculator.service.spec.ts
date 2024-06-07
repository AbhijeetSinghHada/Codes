import { TestBed } from '@angular/core/testing';
import { LoggerService } from '../logger/logger.service';
import { CalculatorService } from './calculator.service';

describe('Calculator Service', () => {
    let mockLoggerService: any;
    let calc: CalculatorService;
    beforeEach(() => {
        mockLoggerService = jasmine.createSpyObj('LoggerService', ['log']);
        TestBed.configureTestingModule({
            providers: [
                CalculatorService,
                {
                    provide: LoggerService,
                    useValue: mockLoggerService,
                },
            ],
        });
        calc = TestBed.inject(CalculatorService);
        mockLoggerService.log.and.returnValue('Using CreateSpy');
    });
    it('should add two numbers', () => {
        // let logger = new LoggerService();
        // spyOn(logger, 'log'); // this will not allow the origional function be called and mocks the methods to do nothing
        // spyOn(logger, 'log').and.callThrough(); // this will also call the origional function
        const result = calc.add(2, 6);
        expect(result).toBe(8);
        expect(mockLoggerService.log).toHaveBeenCalledTimes(1);
    });
    it('should subtract two numbers', () => {
        // let logger = new LoggerService();
        // spyOn(logger, 'log');
        // spyOn(logger, 'log').and.returnValue(1000 - 5); // this will also call the origional function

        // let calc = new CalculatorService(logger);
        const result = calc.subtract(2, 6);
        expect(result).toBe(-4);
        expect(mockLoggerService.log).toHaveBeenCalledTimes(1);
    });
});
