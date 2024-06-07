import { TestBed } from '@angular/core/testing';

import { LoggerService } from './logger.service';

describe('LoggerService', () => {
    let service: LoggerService;

    beforeAll(() => {
        TestBed.configureTestingModule({
            providers: [LoggerService],
        });
        service = TestBed.inject(LoggerService);
    });

    it('should be created', () => {
        expect(service).toBeTruthy();
    });
    it('should append string to the array', () => {
        const testMsg = 'test';
        service.log(testMsg);
        expect(service.messages).toContain(testMsg);
    });
    it('should append empty string to the array', () => {
        const testMsg = '';
        service.log(testMsg);
        expect(service.messages).toContain(testMsg);
    });
    it('should pop empty string from the array', () => {
        const testMsg = '';
        service.clear();
        expect(service.messages).not.toContain(testMsg);
    });
});
