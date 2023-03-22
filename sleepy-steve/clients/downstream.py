class DownstreamClient:
    def __init__(self, hostname: str, port: int) -> None:
        self._server_process = None
        self._hostname = hostname
        self._port = port

    # def start_server(self) -> bool:
    #     pass

    def server_online(self) -> bool:
        if self._server_process is not None:
            # TODO: Actually check with protocol client
            return True
        return False
