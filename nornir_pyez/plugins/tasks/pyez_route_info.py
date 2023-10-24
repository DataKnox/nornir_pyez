import copy
from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyez.plugins.connections import CONNECTION_NAME
from lxml import etree
import xmltodict
import json


def pyez_route_info(
    task: Task,
    all: bool = False,
    best: bool = False,
    brief: bool = False,
    detail: bool = False,
    exact: bool = False,
    hidden: bool = False,
    localization: bool = False, # get-fib-localization-information
    martians: bool = False,     # get-route-martians
    private: bool = False,
    instance_name: str = "all", # get-instance-information
    protocol: str = "all",
    table: str = "all",
    rib_sharding: str = "main",
    destination: str = "",
) -> Result:

    cmd_args = {}
    if destination != "":
        cmd_args["destination"]=destination
        ## TODO: Process route flags (exact, etc)
    if protocol != "all":
        cmd_args["protocol"]=protocol
    if instance_name != "all":
        cmd_args["instance_name"]=instance_name
    if table != "all":
        cmd_args["table"]=table
    if rib_sharding != "main":
        cmd_args["rib-sharding"]=rib_sharding
    if hidden:
        cmd_args["hidden"]=hidden
    if all:
        cmd_args["all"]=all
    if private:
        cmd_args["private"]=private

    # Connect to Device
    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    if martians:
        data = device.rpc.get_route_martians(**cmd_args)
    elif localization:
        data = device.rpc.get_fib_localization_information(**cmd_args)
    elif instance_name != "all":
        ## TODO: Doesn't work - NameError: name 'instance' is not defined
        data = device.rpc.get-instance-information(**cmd_args)
    else:
        data = device.rpc.get_route_information(**cmd_args)
    data = etree.tostring(data, encoding='unicode', pretty_print=True)
    parsed = xmltodict.parse(data)
    clean_parse = json.loads(json.dumps(parsed))
    return Result(host=task.host, result=clean_parse)
