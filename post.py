from fastapi import FastAPI
import blog.schemas as schemas, blog.models as models
from blog.database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)

#Post
@app.post('/blog')
def create_blog(request: schemas.Blog):
    if request.published_at: return {
        "response" : {
            "blog created" : {
                "title" : request.title,
                "body": request.body
            }
        }
    } 
    else: return {
        "response" : {
            "blog created" : "Not created"
        }
    }   