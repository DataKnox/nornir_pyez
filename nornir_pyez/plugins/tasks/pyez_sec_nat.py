import copy
from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyez.plugins.connections import CONNECTION_NAME
from lxml import etree
import xmltodict
import json


def pyez_sec_nat_dest(
    task: Task,
    rule: str = None
) -> Result:

    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    # check to see if the user has passed the argument 'rule' in the call; defaults to all.
    if rule is not None:
        data = device.rpc.get_destination_nat_rule_sets_information(rule_name=rule)
    else:
        data = device.rpc.get_destination_nat_rule_sets_information(all=True)

    data = etree.tostring(data, encoding='unicode', pretty_print=True)
    parsed = xmltodict.parse(data)
    clean_parse = json.loads(json.dumps(parsed))

    return Result(host=task.host, result=clean_parse)

def pyez_sec_nat_src(
    task: Task,
    rule: str = None
) -> Result:

    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    # check to see if the user has passed the argument 'rule' in the call; defaults to all.
    if rule is not None:
        data = device.rpc.get_source_nat_rule_sets_information(rule_name=rule)
    else:
        data = device.rpc.get_source_nat_rule_sets_information(all=True)

    data = etree.tostring(data, encoding='unicode', pretty_print=True)
    parsed = xmltodict.parse(data)
    clean_parse = json.loads(json.dumps(parsed))

    return Result(host=task.host, result=clean_parse)
