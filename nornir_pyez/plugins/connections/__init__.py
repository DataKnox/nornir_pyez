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
        if not port:
            port = 830
        parameters: Dict[str, Any] = {
            "host": hostname,
            "user": username,
            "password": password,
            "port": port,
            "optional_args": {},
            "ssh_config": extras["ssh_config"] if "ssh_config" in extras.keys() else None,
            "ssh_private_key_file": extras["ssh_private_key_file"] if "ssh_private_key_file" in extras.keys() else None,
        }

        connection = Device(**parameters)

        connection.open()
        self.connection = connection

    def close(self) -> None:
        self.connection.close()
