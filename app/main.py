from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routes.auth_routes import auth_router
from app.routes.comment_routes import comment_router
from app.routes.feed_routes import feed_router
from app.routes.like_routes import like_router
from app.routes.post_routes import post_router
from app.routes.subscription_routes import sub_router
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
app.include_router(comment_router)
app.include_router(feed_router)
app.include_router(like_router)
app.include_router(post_router)
app.include_router(sub_router)
app.include_router(user_router)
