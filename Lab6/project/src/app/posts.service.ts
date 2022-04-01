import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { POSTS } from './fake-db';
import { Photos, Post } from './models';

@Injectable({
  providedIn: 'root'
})
export class PostsService {
  
  BASE_URL='https://jsonplaceholder.typicode.com';

  constructor(private client:HttpClient ) { }

  // getPosts(){
  //   return of(POSTS);
  // }
  
  // getPost(id:number){
  //   const post=POSTS.find((x)=>x.id===id)
  //   return of(post);
  // }



  getPosts(): Observable<Post[]>{
    return this.client.get<Post[]>(`${this.BASE_URL}/albums`);
  }
  
  getPost(id:number):Observable<Post>
  {
    return this.client.get<Post>(`${this.BASE_URL}/albums/${id}`);
  }


  addPost(post:Post):Observable<any>
  {
    return this.client.post(`${this.BASE_URL}/posts`,post);
  }



  updatePost(post:Post):Observable<Post>
  {
     return this.client.put<Post>(`${this.BASE_URL}/posts/${post.id}`,post);
    }

  deletePost(id:number):Observable<any> 
  {
    return this.client.delete(`${this.BASE_URL}/posts/${id}`);
  }
  albumsPhotos(id:number):Observable<Photos[]>
  {
    return this.client.get<Photos[]>(`${this.BASE_URL}/posts/${id}/photos`);
  }
}
