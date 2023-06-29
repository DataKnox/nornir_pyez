import copy
from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyez.plugins.connections import CONNECTION_NAME
from lxml import etree
import xmltodict
import json


def pyez_chassis_inventory(
    task: Task,
    clei_models: bool = False,
    detail: bool = False,
    extensive: bool = False,
    models: bool = False
) -> Result:

    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    if extras:
        data = device.rpc.get_chassis_inventory(**extras)
    else:
        data = device.rpc.get_chassis_inventory()
    data = etree.tostring(data, encoding='unicode', pretty_print=True)
    parsed = xmltodict.parse(data)
    clean_parse = json.loads(json.dumps(parsed))
    return Result(host=task.host, result=clean_parse)
