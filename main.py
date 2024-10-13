from typing import Union

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

import random

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}





data = [
      {
        "timestamp": 12345,
        "type" : "book",
        "icon": "📖",
        "title": "Command and Control",
        "author": "Someone",
        "stars": 5
      },
      {
        "timestamp": 54321,
        "type" : "book",
        "icon": "📖",
        "title": "The Art of Invisibility",
        "author": "Kevin Mitnick",
        "stars": 4
      },
      {
        "timestamp": 54320,
        "type" : "github",
        "sub-type" : "commit",
        "icon": "git",
        "title": "Commits in [repo1], [repo2], [privaterepo]",
        "author": "v205"
      },
]


randomURLs = ["https://example.com", "https://example.org", "https://purplebubble.org", "https://kieranklukas.com","https://stackoverflow.com"]



@app.get("/feed")#{showAmount}")
def read_feed():
    return data



@app.get("/random")
def read_feed():
    return RedirectResponse(randomURLs[random.randint(0,len(randomURLs)-1)])

