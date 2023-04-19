from fastapi import FastAPI, status
from schemas import Post



app = FastAPI()

db =[]


@app.post('/posts/', status_code=status.HTTP_201_CREATED)
def create_product(product: Post):
    try:
        db.append(product.dict())
        return db
    except:
        return {'msg':'not created'}

@app.get("/posts/")
def read_posts():
    try:
        return db
    
    except:
        return {'msg':'no posts'}

@app.get("/posts/{post_title}")
def read_post(post_title: str):
    try:
        for post in db:
            if post['title'] == post_title:
                return post
    
    except:
        return {'msg': 'not found'}

@app.put("/posts/{post_title}")
def update_post(post_title: str, post: Post):
    
    try:
        for post_db in db:
            post = post.dict()
            if post_db['title'] == post_title:
                post_db['content'] = post['content']
                return post_db
    except:
        return {'msg':'not found'}
    

@app.delete("/posts/{post_title}")
def delete_post(post_title: str):

    try:
        for post_db in db:
            if post_db['title'] == post_title:
                db.remove(post_db)
        return db
    
    except:
        return {'message': 'error'}