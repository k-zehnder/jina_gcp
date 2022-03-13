from docarray.document.pydantic_model import PydanticDocument, PydanticDocumentArray
from fastapi import FastAPI
from docarray import Document, DocumentArray
import uvicorn
from pydantic import BaseModel
from typing import List


app = FastAPI()


class ItemIdOnly(BaseModel):
    id: str

# class ItemIn(PydanticDocument):
#     text: str = "hello"


@app.get('/single', response_model=ItemIdOnly)
async def get_item_no_embedding():
    d = Document(embedding=[1, 2, 3])
    return d.to_pydantic_model()

@app.post('/single', response_model=ItemIdOnly)
async def create_item(item: PydanticDocument):
    d = Document.from_pydantic_model(item)

    # {"text" : "hello"} manually in FastAPI swagger
    # d = Document.from_pydantic_model(ItemIn(**{"text":"hello"}))
    # now `d` is a Document object
    ...  # process `d` how ever you want
    return d.to_pydantic_model()

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=5000, reload=True)


