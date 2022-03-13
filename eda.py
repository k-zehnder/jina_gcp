from docarray.document.pydantic_model import PydanticDocument, PydanticDocumentArray
from fastapi import FastAPI
from docarray import Document, DocumentArray
from pydantic import BaseModel


class ItemIdOnly(BaseModel):
    id: str

class ItemIn(PydanticDocument):
    text: str = "hello"

if __name__ == "__main__":
    item = ItemIn(**{"text" : "hello"})
    print(f'item: {item}')
    print()

    da = Document.from_pydantic_model(item)
    print(f'da: {da}')
    print()

    pyd = da.to_pydantic_model()
    print(f'pyd: {pyd}')
    print()