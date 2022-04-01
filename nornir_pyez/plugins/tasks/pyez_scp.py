from nornir.core.task import Result, Task

from nornir_pyez.plugins.connections import CONNECTION_NAME

from jnpr.junos.utils.scp import SCP

def pyez_scp(task: Task, file: str, path: str,
                ) -> Result:
    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    device.timeout = 300
    with SCP(device, progress=True) as scp:
        print(scp.put(file, path))
    return Result(host=task.host, result=f"Successfully copied")
