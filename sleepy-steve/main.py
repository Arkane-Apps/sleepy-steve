from uvicorn import run as uvicorn_run

from api import sleepy_steve_api_factory
from clients import MinecraftServerDaemon


def run_api():
    live_server_daemon = MinecraftServerDaemon(
        hostname="0.0.0.0", port=25565, server_dir="/app", server_script_name="foo.sh"
    )

    uvicorn_run(
        sleepy_steve_api_factory(live_server_daemon),
        host="0.0.0.0",
        port=8080,
        log_level="info",
    )


if __name__ == "__main__":
    run_api()
