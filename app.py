from docarray import Document
from jina import Flow

f = Flow.load_config('config.yml')

with f:
    f.post(on='/bar', inputs=Document(), on_done=print)