from fastapi import FastAPI, Response
import uvicorn,typer
from mock_server import ConfigParser, ServerBuilder
from pathlib import Path


class APIServer:



    def __init__(self, file_name: str):
        self.config_file = Path(file_name)
        self.app: FastAPI | None = None



    def build_app(self):

        if not self.config_file.exists():
            print(f"Error: Configuration file not found at '{self.config_file}'")
            raise typer.Exit(code=1)

        print(f"Loading configuration from '{self.config_file}'...")
        parser = ConfigParser(str(self.config_file))
        parser.parse()

        builder = ServerBuilder(parser.endpoints)
        self.app = builder.build()

        @self.app.get("/")
        async def root():
            return {"message": "Welcome to the Mock API Server! Your server is running. Enter your desired endpoint."}
        

        @self.app.get("/favicon.ico")
        async def favicon():
            return Response(status_code=204) 
        
        print("✅ Application built successfully.")



    def run(self, host: str, port: int):
        if not self.app:
            self.build_app()

        print(f"🚀 Starting server on http://{host}:{port}")
        print("Press CTRL+C to stop")
        uvicorn.run(self.app, host=host, port=port)





app = typer.Typer(
    name="Mock Server CLI",
    help="Builds and runs a mock API server from a configuration file.",
    add_completion=False
)




@app.command()
def main(
    config_file: Path = typer.Argument(
        ...,  # The '...' makes this argument required.
        exists=True,
        file_okay=True,
        dir_okay=False,
        readable=True,
        help="The path to the configuration file (e.g., api.yaml)."
    ),
    host: str = typer.Option(
        "127.0.0.1",
        "--host",
        "-h",
        help="The host address to run the server on."
    ),
    port: int = typer.Option(
        8000,
        "--port",
        "-p",
        help="The port to run the server on."
    )
):

    server = APIServer(file_name=str(config_file))
    server.run(host=host, port=port)


if __name__ == "__main__":
    app()



