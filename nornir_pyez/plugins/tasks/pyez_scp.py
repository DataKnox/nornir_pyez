from nornir.core.task import Result, Task

from nornir_pyez.plugins.connections import CONNECTION_NAME
from typing import Dict
from jnpr.junos.utils.scp import SCP


def pyez_scp(
    task: Task,
    file: str,
    path: str,
    scpargs: Dict = {"progress": True},
    direction: str = "put",
) -> Result:
    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    with SCP(device, **scpargs) as scp:
        if direction == "put":
            # File: local file name - path: remote path
            scp.put(file, path)
        elif direction == "get":
            # File: remote file name - path: local path
            scp.get(file, path)
        else:
            raise ValueError("Direction must be either put or get")

    return Result(
        host=task.host, result=f"{direction.upper()} file operation successful"
    )
