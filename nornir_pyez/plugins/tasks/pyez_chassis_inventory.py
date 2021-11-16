import copy
from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyez.plugins.connections import CONNECTION_NAME
from lxml import etree
import xmltodict
import json


def pyez_chassis_inventory(
    task: Task,
    models: str = False
) -> Result:

    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    if models:
        data = device.rpc.get_chassis_inventory(models=True)
    else:
        data = device.rpc.get_chassis_inventory(models=False)
    data = etree.tostring(data, encoding='unicode', pretty_print=True)
    parsed = xmltodict.parse(data)
    clean_parse = json.loads(json.dumps(parsed))
    return Result(host=task.host, result=clean_parse)
