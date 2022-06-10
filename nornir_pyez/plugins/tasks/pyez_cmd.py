from nornir.core.task import Result, Task

from nornir_pyez.plugins.connections import CONNECTION_NAME

from jnpr.junos.utils.start_shell import StartShell

def pyez_cmd(task: Task, command: str,
                ) -> Result:
    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    with StartShell(device) as sh:
        got = sh.run(command)
    return Result(host=task.host, result=f"Command launched, output: {got}")
