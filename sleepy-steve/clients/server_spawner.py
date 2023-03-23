import sh


class MinecraftServerDaemon:
    def __init__(
        self, hostname: str, port: int, server_dir: str, server_script_name: str
    ) -> None:
        self._server_process = None
        self._hostname = hostname
        self._port = port
        self._server_dir = server_dir
        self._server_script = sh.Command(server_script_name)

    def start_server(self) -> bool:
        try:
            self._server_process = self._server_script(_cwd=self._server_dir, _bg=True)
        finally:
            return self._server_process is not None and self._server_process.is_alive()

    def server_online(self) -> bool:
        if self._server_process is not None:
            # TODO: Actually check with protocol client
            return True
        return False
