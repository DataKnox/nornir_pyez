import copy
from typing import Any, Dict, List, Optional
from nornir.core.task import Result, Task
from nornir_pyez.plugins.connections import CONNECTION_NAME
from lxml import etree
import xmltodict
import json


def pyez_get_mpls_lsp_info(
    task: Task,
    abstract_computation: bool = False,  # get-mpls-lsp-abstract-computation
    autobandwidth: bool = False,  # get-mpls-lsp-autobandwidth
    bidirectional: bool = False,
    brief: bool = False,
    bypass: bool = False,
    count_active_routes: bool = False,
    defaults: bool = False,  # get-mpls-lsp-defaults-information
    descriptions: bool = False,
    detail: bool = False,
    down: bool = False,
    egress: bool = False,
    extensive: bool = False,
    externally_controlled: bool = False,
    externally_provisioned: bool = False,
    ingress: bool = False,
    locally_provisioned: bool = False,
    p2mp: bool = False,
    reverse_statistics: bool = False,
    statistics: bool = False,
    terse: bool = False,
    transit: bool = False,
    unidirectional: bool = False,
    up: bool = False,
    logical_system: str = "DEFAULT",
    instance: str = "all",
    name: str = "all",
) -> Result:

    cmd_args = {}
    if logical_system is not "DEFAULT":
        cmd_args["logical_system"]=logical_system
    if instance is not "all":
        cmd_args["instance"]=instance
    if name is not "all":
        cmd_args["regex"]=name

    if bidirectional is True:
        cmd_args["bidirectional"]=bidirectional
    if brief is True:
        cmd_args["brief"]=brief
    if bypass is True:
        cmd_args["bypass"]=bypass
    if count_active_routes is True :
        cmd_args["count_active_routes"]=count_active_routes
    if descriptions is True :
        cmd_args["descriptions"]=descriptions
    if detail is True:
        cmd_args["detail"]=detail
    if down is True:
        cmd_args["down"]=down
    if egress is True:
        cmd_args["egress"]=egress
    if extensive is True:
        cmd_args["extensive"]=extensive
    if externally_controlled is True:
        cmd_args["externally_controlled"]=externally_controlled
    if externally_provisioned is True:
        cmd_args["externally_provisioned"]=externally_provisioned
    if ingress is True:
        cmd_args["ingress"]=ingress
    if locally_provisioned is True:
        cmd_args["locally_provisioned"]=locally_provisioned
    if p2mp is True:
        cmd_args["p2mp"]=p2mp
    if reverse_statistics is True:
        cmd_args["reverse_statistics"]=reverse_statistics
    if statistics is True:
        cmd_args["statistics"]=statistics
    if terse is True:
        cmd_args["terse"]=terse
    if transit is True:
        cmd_args["transit"]=transit
    if unidirectional is True:
        cmd_args["unidirectional"]=unidirectional
    if up is True:
        cmd_args["up"]=up

    # Connect to Device
    device = task.host.get_connection(CONNECTION_NAME, task.nornir.config)

    if defaults:
        this_cmd_args = {}
        # instance and logical_system ONLY
        if instance is not "all":
            this_cmd_args["instance"]=instance
        if logical_system is not "DEFAULT":
            this_cmd_args["logicalsystem"]=logical_system
        data = device.rpc.get_mpls_lsp_defaults_information(**this_cmd_args)
    elif abstract_computation:
        # brief, detail, extensive, logical_system, and name ONLY
        if logical_system is not "DEFAULT":
            this_cmd_args["logical_system"]=logical_system
        if name is not "all":
            this_cmd_args["regex"]=name
        if brief is True:
            this_cmd_args["brief"]=brief
        elif extensive is True:
            this_cmd_args["extensive"]=extensive
        elif detail is True:
            this_cmd_args["detail"]=detail
        data = device.rpc.get_mpls_lsp_abstract_computation(**this_cmd_args)
    elif autobandwidth:
        # brief, detail, extensive, logical_system, and name ONLY
        if logical_system is not "DEFAULT":
            this_cmd_args["logical_system"]=logical_system
        if name is not "all":
            this_cmd_args["regex"]=name
        if brief is True:
            this_cmd_args["brief"]=brief
        elif extensive is True:
            this_cmd_args["extensive"]=extensive
        elif detail is True:
            this_cmd_args["detail"]=detail
        data = device.rpc.get_mpls_lsp_autobandwidth(**this_cmd_args)
    else:
        data = device.rpc.get_mpls_lsp_information(**cmd_args)
    data = etree.tostring(data, encoding='unicode', pretty_print=True)
    parsed = xmltodict.parse(data)
    clean_parse = json.loads(json.dumps(parsed))
    return Result(host=task.host, result=clean_parse)
  
