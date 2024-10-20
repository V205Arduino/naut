from typing import Union

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

import random

from dotenv import load_dotenv
import os

import json
import time

from pydantic import BaseModel


class Item(BaseModel):
    type: str
    data: str 
    title: str
    timestamp: int = None



app = FastAPI()



load_dotenv()

PORT = int(os.getenv('PORT'))


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/urls")
def add_url(item: Item):
  # Load the data from the file

  item.timestamp = int(time.time())  # Get current timestamp
  with open("data/urls.json", "r") as f:
      URLs = json.load(f)
      f.close()
  
  URLs.append(dict(item))
  with open("data/urls.json", "w") as f:
    json.dump(URLs, f)
    f.close()


  # Print the data
  print(URLs)

  print(item)
  return item
#curl -X POST http://127.0.0.1:8000/urls

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




@app.get("/feed")#{showAmount}")
def read_feed():
    return data



@app.get("/random")
def random_URL():
  random.seed()
  with open("data/urls.json", "r") as f:
      URLs = json.load(f)

  randomNum = random.randint(0,len(URLs)-1)
  return RedirectResponse(URLs[randomNum]["data"])


# @app.post("/items/")
# async def create_item(item: Item):
#     return item
