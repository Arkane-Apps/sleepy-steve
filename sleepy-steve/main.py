from uvicorn import run as uvicorn_run

from api import sleepy_steve_api_factory
from clients.downstream import DownstreamClient


def run_api():
    downstream_server = DownstreamClient(hostname="0.0.0.0", port=25565)
    uvicorn_run(
        sleepy_steve_api_factory(downstream_server),
        host="0.0.0.0",
        port=8080,
        log_level="info",
    )


if __name__ == "__main__":
    run_api()