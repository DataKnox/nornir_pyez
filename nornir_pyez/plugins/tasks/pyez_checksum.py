from nornir.core.task import Result, Task

from nornir_pyez.plugins.connections import CONNECTION_NAME

from jnpr.junos.utils.fs import FS

def pyez_checksum(task: Task, filepath: str, calc: str,
        ) -> Result:
    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    fs = FS(device)
    checksum = fs.checksum(filepath, calc)
    return Result(host=task.host, result=f"{checksum}")
