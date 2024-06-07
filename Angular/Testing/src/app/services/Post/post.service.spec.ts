import { TestBed } from '@angular/core/testing';
import {
    HttpClientTestingModule,
    HttpTestingController,
} from '@angular/common/http/testing';
import { PostService } from './post.service';
import { HttpClient } from '@angular/common/http';
import { Post } from '../../models/posts';

describe('Post Service', () => {
    let http: HttpClient;
    let postService: PostService;
    let httpTestingController: HttpTestingController;
    let POSTS: any;

    beforeEach(() => {
        POSTS = [
            {
                id: 1,
                title: 'Title 1',
                body: 'Body 1',
            },
            {
                id: 2,
                title: 'Title 2',
                body: 'Body 2',
            },
            {
                id: 3,
                title: 'Title 3',
                body: 'Body 3',
            },
            {
                id: 4,
                title: 'Title 4',
                body: 'Body 4',
            },
        ];

        TestBed.configureTestingModule({
            imports: [HttpClientTestingModule],
            providers: [PostService, HttpClient],
        });

        postService = TestBed.inject(PostService);
        http = TestBed.inject(HttpClient);
        httpTestingController = TestBed.inject(HttpTestingController);
    });

    afterEach(() => {
        httpTestingController.verify();
    });

    describe('getPosts', () => {
        it('should return correct value for request', (done: DoneFn) => {
            postService.getPosts().subscribe(
                (data) => {
                    expect(data).toEqual(POSTS);
                    done();
                },
                (error) => {
                    done.fail();
                }
            );

            const req = httpTestingController.expectOne(
                'https://jsonplaceholder.typicode.com/posts'
            );
            expect(req.request.method).toBe('GET');
            req.flush(POSTS);
        });

        it('should handle error', (done: DoneFn) => {
            const errorMessage = 'Error occurred';

            postService.getPosts().subscribe(
                (data) => {
                    done.fail();
                },
                (error) => {
                    expect(error.error).toBe(errorMessage);
                    done();
                }
            );

            const req = httpTestingController.expectOne(
                'https://jsonplaceholder.typicode.com/posts'
            );
            expect(req.request.method).toBe('GET');
            req.flush(errorMessage, { status: 404, statusText: 'Not Found' });
        });
    });

    describe('deletePost', () => {
        it('should return correct value for request', (done: DoneFn) => {
            const postId = 1;

            postService.deletePost({ id: postId } as Post).subscribe(
                (data) => {
                    expect(data).toBeTrue();
                    done();
                },
                (error) => {
                    done.fail();
                }
            );

            const req = httpTestingController.expectOne(
                `https://jsonplaceholder.typicode.com/post/${postId}`
            );
            expect(req.request.method).toBe('DELETE');
            req.flush(true);
        });

        it('should handle error', (done: DoneFn) => {
            const postId = 1;
            const errorMessage = 'Error occurred';
            postService.deletePost({ id: postId } as Post).subscribe(
                (data) => {
                    done.fail();
                },
                (error) => {
                    expect(error.error).toBe(errorMessage);
                    done();
                }
            );

            const req = httpTestingController.expectOne(
                `https://jsonplaceholder.typicode.com/post/${postId}`
            );
            expect(req.request.method).toBe('DELETE');
            req.flush(errorMessage, { status: 404, statusText: 'Not Found' });
        });
    });
});
