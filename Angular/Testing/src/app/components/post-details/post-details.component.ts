import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { PostService } from '../../services/Post/post.service';
import { Post } from '../../models/posts';

@Component({
    selector: 'app-post-details',
    standalone: true,
    imports: [],
    templateUrl: './post-details.component.html',
    styleUrl: './post-details.component.css',
})
export class PostDetailsComponent implements OnInit {
    post!: Post;
    constructor(
        private route: ActivatedRoute,
        private postService: PostService,
        private location: Location
    ) {}

    ngOnInit(): void {
        this.getPosts();
    }

    getPosts() {
        const id = this.route.snapshot.params['id'];
        id &&
            this.postService.getPost(id).subscribe((post) => {
                this.post = post;
            });
    }
}
