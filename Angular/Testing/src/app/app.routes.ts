import { RouterModule, Routes } from '@angular/router';
import { PostsComponent } from './components/posts/posts.component';
import { PostDetailsComponent } from './components/post-details/post-details.component';
import { NgModule } from '@angular/core';

export const routes: Routes = [
    {
        path: 'posts',
        component: PostsComponent,
    },
    {
        path: 'details/:id',
        component: PostDetailsComponent,
    },
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule],
})
export class AppRoutingModule {}
