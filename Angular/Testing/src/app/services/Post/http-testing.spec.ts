import { HttpClient } from '@angular/common/http';
import {
    HttpClientTestingModule,
    HttpTestingController,
} from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';

let testUrl = '/data';
interface Data {
    name: string;
}

describe('Http Client Testing Module', () => {
    let httpClient: HttpClient;
    let httpTestingController: HttpTestingController;
    beforeEach(() => {
        TestBed.configureTestingModule({
            imports: [HttpClientTestingModule],
        });
        httpClient = TestBed.inject(HttpClient);
        httpTestingController = TestBed.inject(HttpTestingController);
    });
    it('should call the test url once', () => {
        const testData: Data = { name: 'Abhijeet Singh' };
        httpClient.get<Data>(testUrl).subscribe((data) => {
            expect(data).toEqual(testData);
        });
        const request = httpTestingController.expectOne('/data');
        request.flush(testData);
    });
    it('should send multiple requests', () => {
        const testData: Data[] = [
            { name: 'Abhijeet Singh' },
            { name: 'Narpat Singh' },
        ];
        httpClient.get<Data[]>(testUrl).subscribe((data) => {
            expect(data.length).toEqual(0);
        });
        httpClient.get<Data[]>(testUrl).subscribe((data) => {
            expect(data).toEqual([testData[0]]);
        });
        httpClient.get<Data[]>(testUrl).subscribe((data) => {
            expect(data).toEqual(testData);
        });
        const requests = httpTestingController.match('/data');
        expect(requests.length).toEqual(3);
        requests[0].flush([]);
        requests[1].flush([testData[0]]);
        requests[2].flush(testData);
    });
});
