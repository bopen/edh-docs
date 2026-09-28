from pathlib import Path

from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

here_path = Path(__file__).parent.resolve()
build_path = here_path / ".." / "build"

routes = [
    Mount("/docs", app=StaticFiles(directory=build_path.resolve()), name="docs"),
]

app = Starlette(routes=routes)
