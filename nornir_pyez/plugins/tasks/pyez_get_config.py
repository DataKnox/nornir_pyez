import copy
from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyez.plugins.connections import CONNECTION_NAME
from lxml import etree
import xmltodict
import json


def pyez_get_config(
    task: Task,
    database: str = None,
    filter_xml: str = None
) -> Result:

    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)
    if database is not None:
        if filter_xml is not None:
            data = device.rpc.get_config(
                options={'database': database}, filter_xml=filter_xml)
        else:
            data = device.rpc.get_config(options={'database': database})
    else:
        if filter_xml is None:
            data = device.rpc.get_config()
        else:
            data = device.rpc.get_config(filter_xml=filter_xml)
    data = etree.tostring(data, encoding='unicode', pretty_print=True)
    parsed = xmltodict.parse(data)
    clean_parse = json.loads(json.dumps(parsed))
    return Result(host=task.host, result=clean_parse)
