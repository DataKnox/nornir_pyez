import copy
from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyez.plugins.connections import CONNECTION_NAME


def pyez_facts(
    task: Task,
) -> Result:

    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    result = device.facts
    return Result(host=task.host, result=result)
