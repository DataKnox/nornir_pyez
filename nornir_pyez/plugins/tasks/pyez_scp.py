from nornir.core.task import Result, Task

from nornir_pyez.plugins.connections import CONNECTION_NAME
from typing import Dict
from jnpr.junos.utils.scp import SCP


def pyez_scp(
    task: Task,
    file: str,
    path: str,
    scpargs: Dict = {"progress": True},
) -> Result:
    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    with SCP(device, **scpargs) as scp:
        scp.put(file, path)
    return Result(host=task.host, result=f"Successfully copied")
