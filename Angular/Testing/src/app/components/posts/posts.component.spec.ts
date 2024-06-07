import { of } from 'rxjs';
import { Post } from '../../models/posts';
import { PostService } from '../../services/Post/post.service';
import { PostsComponent } from './posts.component';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { provideRouter } from '@angular/router';
import { By } from '@angular/platform-browser';
import { PostComponent } from './post/post.component';

describe('Posts Component', () => {
    let POSTS: Post[];
    let fixture: ComponentFixture<PostsComponent>;
    let component: PostsComponent;
    let mockPostService: PostService;
    beforeEach(() => {
        POSTS = [
            {
                id: 1,
                title: 'Post 1',
                body: 'Body of Post 1',
            },
            {
                id: 2,
                title: 'Post 2',
                body: 'Body of Post 2',
            },
            {
                id: 3,
                title: 'Post 3',
                body: 'Body of Post 3',
            },
            {
                id: 4,
                title: 'Post 4',
                body: 'Body of Post 4',
            },
        ];
        mockPostService = jasmine.createSpyObj('PostService', {
            getPosts: of(POSTS),
            deletePost: of(true),
        });
        TestBed.configureTestingModule({
            providers: [
                {
                    provide: PostService,
                    useValue: mockPostService,
                },
                provideRouter([]),
            ],
        });
        fixture = TestBed.createComponent(PostsComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });
    it('should get posts from service for the Posts array', () => {
        expect(component.posts).toEqual(POSTS);
        expect(component.posts.length).toEqual(POSTS.length);
    });
    it('should call getPosts from service only once', () => {
        expect(mockPostService.getPosts).toHaveBeenCalledTimes(1);
    });
    it('should call deletePost from service only once', () => {
        component.deletePost(POSTS[1]);
        expect(mockPostService.deletePost).toHaveBeenCalledTimes(1);
    });
    it('should create post component exactly one time for each post', () => {
        const postElements = fixture.debugElement.queryAll(By.css('app-post'));
        expect(postElements.length).toEqual(POSTS.length);
    });
    it('should delete the passed post from the Posts array', () => {
        component.deletePost({
            id: 2,
            title: 'Post 2',
            body: 'Body of Post 2',
        });
        POSTS.splice(1, 1);
        expect(component.posts).toEqual(POSTS);
    });

    it('should check if post component is intialised with correct value or not', () => {
        const postAllComponent = fixture.debugElement.queryAll(
            By.directive(PostComponent)
        );
        for (let i in postAllComponent) {
            const singlePostComponent = postAllComponent[i].componentInstance;
            expect(singlePostComponent.post).toBe(POSTS[i]);
        }
    });

    it('should call the delete function when post component button is clicked', () => {
        const postComponentsAll = fixture.debugElement.queryAll(
            By.directive(PostComponent)
        );
        spyOn(component, 'deletePost');
        postComponentsAll[0]
            .query(By.css('button'))
            .triggerEventHandler('click', {
                stopPropagation: () => {},
            });
        expect(component.deletePost).toHaveBeenCalledOnceWith(POSTS[0]);
    });
});
