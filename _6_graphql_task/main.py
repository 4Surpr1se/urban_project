import base64

from strawberry.asgi import GraphQL
from fastapi.responses import HTMLResponse
import asyncio
from typing import AsyncGenerator, AnyStr, NewType
from moviepy.video.io.VideoFileClip import VideoFileClip

import strawberry
from fastapi import FastAPI, Request, Response, Header
from pathlib import Path

from strawberry.scalars import Base64

app = FastAPI()
CHUNK_SIZE = 1024


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "world"


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self, start: int = 0) -> AsyncGenerator[Base64, None]:
        video_path = Path("rocket.mp4")
        with open(video_path, "rb") as video:
            video.seek(start)
            while True:
                data = video.read(CHUNK_SIZE)
                if not data:
                    break
                yield Base64(data)


@app.get("/")
async def read_root():
    return HTMLResponse("""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Video Streaming</title>
        </head>
        <body>
            <video width="600" controls>
                <source src="ws://localhost:8000/graphql" type="video/mp4">
            </video>
        </body>
    </html>
    """)


@app.get("/video")
async def video_endpoint(range: str = Header(None)):
    start, end = 0, None
    if range:
        start, end = range.replace("bytes=", "").split("-")
        start = int(start)
        end = int(end) if end else start + CHUNK_SIZE
    video_path = 'rocket.mp4'
    with open(video_path, "rb") as video:
        video.seek(start)
        data = video.read(end - start) if end else video.read(CHUNK_SIZE)
        filesize = str(video_path.stat().st_size)
        headers = {
            'Content-Range': f'bytes {start}-{end if end else filesize}/{filesize}',
            'Accept-Ranges': 'bytes',
            'Content-Length': str(len(data)),
            'Content-Type': 'video/mp4',
        }
        return Response(data, status_code=206, headers=headers)


schema = strawberry.Schema(query=Query, subscription=Subscription)

graphql_app = GraphQL(schema)

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
