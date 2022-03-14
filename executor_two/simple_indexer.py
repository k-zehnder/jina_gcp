import os
from jina import Flow, Document, DocumentArray
from jina import Executor, Flow, requests
from docarray import DocumentArray, Document



class SimpleIndexer(Executor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # print(os.path.join(self.workspace, 'index.db'))
        # self._index = DocumentArray(
        #     storage='sqlite',
        #     config={
        #         'connection': os.path.join(self.workspace, 'index.db'),
        #         'table_name': 'clip',
        #     },
        # )
        self._index = DocumentArray()

    @requests(on='/index')
    def index(self, docs: DocumentArray, **kwargs):
        self._index.extend(docs)
        
    @requests(on='/search')
    def search(self, docs: DocumentArray, **kwargs):
        docs.match(self._index)
