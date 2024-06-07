import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PostComponent } from './post.component';
import { Post } from '../../../models/posts';
import { first } from 'rxjs';
import { RouterModule, provideRouter } from '@angular/router';
import { DebugElement } from '@angular/core';
import { By } from '@angular/platform-browser';

describe('PostComponent', () => {
    let component: PostComponent;
    let fixture: ComponentFixture<PostComponent>;
    beforeEach(() => {
        TestBed.configureTestingModule({
            providers: [provideRouter([])],
        });
        fixture = TestBed.createComponent(PostComponent);
        component = fixture.componentInstance;
    });
    it('should have created a instance using testbed', () => {
        expect(component).toBeDefined();
    });
    it('should render the post title', () => {
        component.post = {
            id: 1,
            title: 'title 1',
            body: 'body 1',
        };
        fixture.detectChanges();
        const postElement: HTMLElement = fixture.nativeElement;
        const postTitleElement = postElement.querySelector('a');
        expect(postTitleElement?.innerText).toEqual(component.post.title);
    });
    it('should render the post title using the debug element', () => {
        component.post = {
            id: 1,
            title: 'title 1',
            body: 'body 1',
        };
        fixture.detectChanges();
        const postElement: DebugElement = fixture.debugElement;
        const postTitleElement: HTMLElement = postElement.query(
            By.css('a')
        ).nativeElement;
        expect(postTitleElement?.innerText).toEqual(component.post.title);
    });
    it('should raise an event when delete post is clicked', () => {
        const post: Post = {
            id: 1,
            title: 'title 1',
            body: 'body 1',
        };
        component.post = post;
        component.delete.pipe(first()).subscribe((selectedPost) => {
            expect(selectedPost).toEqual(post);
        });
        component.OnDelete(new MouseEvent('click'));
    });
});
