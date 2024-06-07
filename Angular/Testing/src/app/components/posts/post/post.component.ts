import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Post } from '../../../models/posts';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { StrengthPipe } from '../../../Pipes/Strength/strength.pipe';

@Component({
    selector: 'app-post',
    standalone: true,
    imports: [CommonModule, RouterModule, StrengthPipe],
    templateUrl: './post.component.html',
    styleUrl: './post.component.css',
})
export class PostComponent implements OnInit {
    @Input() post!: Post;
    @Output() delete: EventEmitter<Post> = new EventEmitter();
    constructor() {}
    ngOnInit(): void {
        // console.log('Inside Child Post');
    }

    OnDelete(event: Event) {
        event.stopPropagation();
        this.delete.emit(this.post);
    }
}
