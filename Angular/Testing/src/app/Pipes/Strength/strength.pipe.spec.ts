import { StrengthPipe } from './strength.pipe';

describe('StrengthPipe', () => {
    it('create an instance', () => {
        const pipe = new StrengthPipe();
        expect(pipe).toBeTruthy();
    });
    it('should display weak if 5 is passed', () => {
        const pipe = new StrengthPipe();
        expect(pipe.transform(5)).toBe('5 Weak');
    });
    it('should display strong if 10 is passed', () => {
        const pipe = new StrengthPipe();
        expect(pipe.transform(10)).toBe('10 Strong');
    });
    it('should display strongest if 20 is passed', () => {
        const pipe = new StrengthPipe();
        expect(pipe.transform(20)).toBe('20 Strongest');
    });
});
