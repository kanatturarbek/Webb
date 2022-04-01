import { Component, OnInit } from '@angular/core';
import { POSTS } from '../fake-db';
import { Post } from '../models';
import { PostsService } from '../posts.service';

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.css']
})
export class PostsComponent implements OnInit {
  posts?: Post[];
  loaded?:boolean;
  newPost?:string;
  constructor(private postService:PostsService) { 
    this.newPost='';
  }

  ngOnInit(): void {
    this.getPosts();
  }
 
  getPosts(){
    this.loaded=false;
    this.postService.getPosts().subscribe((posts)=>{
      this.posts=posts;
      this.loaded=true;
    });
  }

addPost(){
  const post={
    title:this.newPost
  };
  this.loaded=false;
  this.postService.addPost(post as Post).subscribe((post)=>{
    console.log(post);
    this.loaded=true;
    this.posts?.unshift(post);
    this.newPost='';
  });
}

  deletePost(id:number){
    this.posts=this.posts?.filter((x)=>x.id!==id);
    this.postService.deletePost(id).subscribe(()=>{
      console.log('deleted',id);
    })
    }
}
