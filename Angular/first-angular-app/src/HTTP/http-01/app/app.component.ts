import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { map } from 'rxjs/operators';
import { PostService } from './post.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  isFetchingPosts = false;
  loadedPosts: any = [];
  error;
  errorSubscription: Subscription;
  constructor(private http: HttpClient, private postService: PostService) {}

  ngOnInit() {
    // this.fetchPosts();
    this.errorSubscription = this.postService.error.subscribe((error) => {
      this.error = error;
    });
  }

  onCreatePost(postData: { username: string; password: string }) {
    // Send Http request
    this.postService.createAndStorePost(postData);
  }
  private fetchPosts() {
    this.isFetchingPosts = true;
    this.postService.fetchPosts().subscribe(
      (data) => {
        this.isFetchingPosts = false;
        this.loadedPosts = data;
      },
      (error: HttpErrorResponse) => {
        this.isFetchingPosts = false;
        this.loadedPosts = [];
        this.error = error;
      }
    );
  }
  onFetchPosts() {
    // Send Http request
    this.fetchPosts();
  }

  onClearPosts() {
    // Send Http request
    this.postService.clearPosts().subscribe((data) => {
      this.fetchPosts();
    });
  }
  ngOnDestroy() {
    this.errorSubscription.unsubscribe();
  }
}
