from fastapi import FastAPI, Response
from mock_server import ConfigParser, ServerBuilder


app = FastAPI()


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    # The include_in_schema=False part is to prevent this endpoint
    # from showing up in your auto-generated API docs (e.g., /docs).
    return Response(status_code=204)

@app.get("/test")
def read_test():
    return {"status": "ok"}



