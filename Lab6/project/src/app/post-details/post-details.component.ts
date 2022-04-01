import { Location } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { POSTS } from '../fake-db';
import { Photos, Post } from '../models';
import { PhotosComponent } from '../photos/photos.component';
import { PostsService } from '../posts.service';

@Component({
  selector: 'app-post-details',
  templateUrl: './post-details.component.html',
  styleUrls: ['./post-details.component.css']
})
export class PostDetailsComponent implements OnInit {

  post!: Post;
  loaded?:boolean;
  photos: Photos[];
  constructor(private route: ActivatedRoute,
    private location: Location,
    private postsService:PostsService) { 

      this.photos=[];
    }

  ngOnInit(): void {
    // const id=+Number(this.route.snapshot.paramMap.get('id'));
    // this.post = POSTS.find((x)=>x.id===id);
    
    // this.route.paramMap.subscribe((params)=>{
    //   const id= +Number(params.get('id'));
    //   this.post = POSTS.find((x)=>x.id===id);
    // });
    this.getPost();
  }
  

  getPost(){
      this.route.paramMap.subscribe((params)=>{
      const id= +Number(params.get('id'));
      this.loaded=false;
      this.postsService.getPost(id).subscribe((post)=>{
        this.post=post;
        this.loaded=true;
      });
  });
  }
  
  updatePost(){
    this.loaded=false;
    this.postsService.updatePost(this.post).subscribe((post)=>{
      console.log(post);
      this.loaded=true;
    });
  }
   showPhotos(){
      this.postsService.albumsPhotos(this.post.id).subscribe((photos)=>{
       this.photos=photos;
      });
   }
  

  goBack() {
    this.location.back();

  }
}