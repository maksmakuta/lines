from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routes.auth_routes import auth_router
from app.routes.feed_routes import feed_router
from app.routes.post_routes import post_router
from app.routes.user_routes import user_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # remove that for prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(feed_router)
app.include_router(user_router)
app.include_router(post_router)



# COMMENTS
@app.post("/comments")
def new_comment():
    pass

@app.get("/comments/{comment_id}")
def get_comment(comment_id: int):
    pass

@app.delete("/comments/{comment_id}")
def delete_comment(comment_id: int):
    pass


# LIKES
@app.post("/likes")
def new_like():
    pass

@app.delete("/likes/{like_id}")
def delete_like(like_id: int):
    pass


# SUBSCRIPTIONS
@app.post("/subscriptions")
def new_subscribe():
    pass

@app.delete("/subscriptions/{subscription_id}")
def unsubscribe(subscription_id: int):
    pass
