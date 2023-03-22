from __future__ import annotations

import os
from typing import Type

from pydantic import BaseModel


class SleepySteveConfig(BaseModel):
    live_server_hostname: str
    live_server_port: int
    sleep_server_hostname: str
    sleep_server_port: int

    @classmethod
    def load_env_config(cls: Type[SleepySteveConfig]) -> SleepySteveConfig:
        """Loads config from the environment

        live_server_hostname:  SS_LIVE_HOST (default: 0.0.0.0)
        live_server_port:      SS_LIVE_PORT (default: 25565)
        sleep_server_hostname: SS_SLEEP_HOST (default: 0.0.0.0)
        sleep_server_port:     SS_SLEEP_PORT (default: 35565)

        Returns:
            SleepySteveConfig: Config object loaded from env
        """
        return cls(
            live_server_hostname=os.getenv("SS_LIVE_HOST", "0.0.0.0"),
            live_server_port=int(os.getenv("SS_LIVE_PORT", "25565")),
            sleep_server_hostname=os.getenv("SS_SLEEP_HOST", "0.0.0.0"),
            sleep_server_port=int(os.getenv("SS_SLEEP_PORT", "35565")),
        )
