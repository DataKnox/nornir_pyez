import copy
from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyez.plugins.connections import CONNECTION_NAME
from lxml import etree
import xmltodict
import json


def pyez_rpc(
    task: Task,
    func: str,
    extras: Dict = None,
) -> Result:

    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    function = getattr(device.rpc, func)
    if extras:
        data = function(**extras)
    else:
        data = function()
    if isinstance(data, bool):
        data = f'''<nornir_pyez_notification>This is a known error for some RPC, this RPC request didn't return a well 
        formed XML message, but: {data}</nornir_pyez_notification>'''
    else:
        data = etree.tostring(data, encoding='unicode', pretty_print=True)
    parsed = xmltodict.parse(data)
    clean_parse = json.loads(json.dumps(parsed))
    return Result(host=task.host, result=clean_parse)
