from typing import List
from fastapi import FastAPI

from clients.downstream import DownstreamClient
from clients.gobetween import IntString, RoutesModel


def sleepy_steve_api_factory(downstream_client: DownstreamClient):
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
        return downstream_client.server_online()

    return api
