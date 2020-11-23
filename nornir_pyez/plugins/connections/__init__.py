from typing import Any, Dict, Optional

from jnpr.junos import Device

from nornir.core.configuration import Config

CONNECTION_NAME = "pyez"


class Pyez:
    def open(
        self,
        hostname: Optional[str],
        username: Optional[str],
        password: Optional[str],
        port: Optional[int],
        platform: Optional[str],
        extras: Optional[Dict[str, Any]] = None,
        configuration: Optional[Config] = None,
    ) -> None:
        extras = extras or {}

        parameters: Dict[str, Any] = {
            "host": hostname,
            "user": username,
            "password": password,
            "optional_args": {},
        }

        if port and "port" not in parameters["optional_args"]:
            parameters["optional_args"]["port"] = port

        connection = Device(**parameters)

        connection.open()
        self.connection = connection

    def close(self) -> None:
        self.connection.close()
