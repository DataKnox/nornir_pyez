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
            "conn_timeout": extras["conn_timeout"] if "conn_timeout" in extras.keys() else None,
            "rpc_timeout": extras["rpc_timeout"] if "rpc_timeout" in extras.keys() else None,
            "optional_args": {},
            "ssh_config": extras["ssh_config"] if "ssh_config" in extras.keys() else None,
            "ssh_private_key_file": extras["ssh_private_key_file"] if "ssh_private_key_file" in extras.keys() else None,
        }

        connection = Device(**parameters)

        if parameters["conn_timeout"]:
            connection.open(auto_probe=parameters["conn_timeout"])
        else:
            connection.open()
        
        if parameters["rpc_timeout"]:
            connection.timeout = parameters["rpc_timeout"]
        else:
            connection.timeout = 300
            
        self.connection = connection

    def close(self) -> None:
        self.connection.close()
