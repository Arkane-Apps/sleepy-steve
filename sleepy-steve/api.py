from typing import List
from fastapi import FastAPI

from clients import IntString, MinecraftServerDaemon, RoutesModel


def sleepy_steve_api_factory(live_server_daemon: MinecraftServerDaemon):
    api = FastAPI()

    @api.get("/server/routes")
    def get_server_routes() -> List[RoutesModel]:
        return [
            RoutesModel(
                host="0.0.0.0",
                port=IntString("35565"),
                weight=IntString("1"),
                priority=IntString("1"),
            )
        ]

    @api.get("/server/status")
    def get_status() -> bool:
        return live_server_daemon.server_online()

    return api
