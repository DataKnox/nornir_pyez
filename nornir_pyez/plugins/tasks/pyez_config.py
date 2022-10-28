import copy
from typing import Any, Dict, List, Optional
from jnpr.junos.utils.config import Config
from nornir.core.task import Result, Task

from nornir_pyez.plugins.connections import CONNECTION_NAME


def pyez_config(
    task: Task,
    payload: str = None,
    update: bool = False,
    data_format: str = 'text',
    template_path: str = None,
    template_vars: str = None,
    commit_now: bool = False,
    first_loading: bool = True
) -> Result:

    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    config = Config(device)
    if first_loading:
        config.lock()
    if template_path:
        config.load(template_path=template_path,
                    template_vars=template_vars, format=data_format)
    else:
        if data_format == 'text':
            if update:
                config.load(payload, format='text', update=True)
            else:
                config.load(payload, format='text', update=False)
        else:
            if update:
                config.load(payload, format=data_format, update=True)
            else:
                config.load(payload, format=data_format, update=False)
    if commit_now:
        if config.commit_check() == True:
            config.commit()
        else:
            config.rollback()
        config.unlock()

    return Result(host=task.host, result=f"Successfully deployed config \n {payload} \nNow you may need to commit or rollback 0")
