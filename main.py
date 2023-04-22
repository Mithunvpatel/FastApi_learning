from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange





app = FastAPI()
#uvicorn main:app --reload --port 5000
#just in case "chrome://net-internals/#sockets"
# utilize CRUD 
#request Get method url: "/"
#routes and pathways matter in the hierarchy of the procedural delivery of code
#order matters



class Post(BaseModel):
    title: str
    content: str
    published: bool = True



my_posts = [{"title":"title of post 1", "content": "content of post 1", "id": 1},{"title":"title of post 2", "content": "content of post 2", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

#function
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get("/")
def root():
    return {"message": "Hello World"}


#get all posts
@app.get("/posts")
def get_posts():
    return {"data": my_posts}


#creating a single post
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

#title str, content str, 


#getting an individual post
@app.get("/posts/{id}")
def get_post(id: int, reponse: Response):
    post = find_post(id)
    #add update to user when {1} does not exist
    if not post:
        #cleaner
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail = f"post with id: {id} was not found") 
        ##hardcoded expection being passed
        #reponse.status_code = status.HTTP_404_NOT_FOUND
        #return {'message': f"post with id: {id} was not found"}
    #print(post)
    return {"post_detail": post}


#delete posts
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    #find the index in the array that has required ID
    #my_post.pop(index)
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id} does not exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


#update posts
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    print(post)
    return {'message': "updated post"}

