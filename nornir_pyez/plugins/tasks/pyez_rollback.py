import copy
from typing import Any, Dict, List, Optional
from jnpr.junos.utils.config import Config
from nornir.core.task import Result, Task

from nornir_pyez.plugins.connections import CONNECTION_NAME


def pyez_rollback(task: Task, rollback_number: int = 0) -> Result:
    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    config = Config(device)
    if rollback_number != 0:
        config.lock()
    config.rollback(rollback_number)
    if rollback_number == 0:
        config.unlock()
    return Result(
        host=task.host,
        result="Successfully emptied config DB and unlocked config"
        if rollback_number == 0
        else f"Successfully rollbacked {rollback_number} commit/s, now you may need to commit",
    )
