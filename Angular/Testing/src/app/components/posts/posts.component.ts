import { Component } from '@angular/core';
import { Post } from '../../models/posts';
import { PostService } from '../../services/Post/post.service';
import { PostComponent } from './post/post.component';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';

@Component({
    selector: 'app-posts',
    standalone: true,
    imports: [CommonModule, PostComponent],
    providers: [HttpClientModule],
    templateUrl: './posts.component.html',
    styleUrl: './posts.component.css',
})
export class PostsComponent {
    posts: Post[] = [];
    constructor(private postService: PostService) {}
    ngOnInit() {
        this.getPosts();
    }

    getPosts() {
        this.postService.getPosts().subscribe((data: Post[]) => {
            this.posts = data;
        });
    }
    deletePost(post: Post) {
        this.posts = this.posts.filter((p) => p.id !== post.id);
        this.postService.deletePost(post).subscribe();
    }
}
