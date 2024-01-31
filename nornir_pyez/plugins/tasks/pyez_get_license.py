import copy
from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyez.plugins.connections import CONNECTION_NAME
from lxml import etree
import xmltodict
import json


def pyez_get_license_info(
    task: Task,
    brief: bool = False,
    detail: bool = False,
    installed: bool = False,
    keys: bool = False,
    usage: bool = False
) -> Result:

    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    cmd_args = {}
    if brief is True:
        cmd_args["brief"]=True
    elif detail is True:
        cmd_args["detail"]=True

    if installed is True:
        data = device.rpc.get_license_information()
    elif keys is True:
        data = device.rpc.get_license_key_information()
    elif usage is True:
        data = device.rpc.get_license_usage_summary()
    else:
        data = device.rpc.get_license_summary_information(**cmd_args)
    data = etree.tostring(data, encoding='unicode', pretty_print=True)
    parsed = xmltodict.parse(data)
    clean_parse = json.loads(json.dumps(parsed))
    return Result(host=task.host, result=clean_parse)
