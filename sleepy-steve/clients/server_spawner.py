import sh
import structlog


class MinecraftServerDaemon:
    def __init__(
        self, hostname: str, port: int, server_dir: str, server_script_name: str
    ) -> None:
        self._logger: structlog.BoundLogger = structlog.get_logger(name=self.__class__)
        self._server_process = None
        self._hostname = hostname
        self._port = port
        self._server_dir = server_dir
        self._server_script = sh.Command(f"{server_dir}/{server_script_name}")

    def start_server(self) -> bool:
        try:
            self._server_process = self._server_script(_cwd=self._server_dir, _bg=True)
        except (sh.ErrorReturnCode, sh.CommandNotFound) as err:
            self._logger.error("unable to start server process", err=err)
            return False
        return True

    def server_online(self) -> bool:
        if self._server_process is not None:
            # TODO: Actually check with protocol client
            return True
        return False
