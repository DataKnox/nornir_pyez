pyez_rpc
========

This task is used to run any ad-hoc RPC using PyEZ

Example::

    from nornir_pyez.plugins.tasks import pyez_rpc
    import os
    from nornir import InitNornir
    from nornir_utils.plugins.functions import print_result
    from rich import print

    script_dir = os.path.dirname(os.path.realpath(__file__))

    nr = InitNornir(config_file=f"{script_dir}/config.yml")

    extras = {
        "level-extra": "detail",
        "interface-name": "ge-0/0/0"
    }


    response = nr.run(
        task=pyez_rpc, func='get-interface-information', extras=extras)

    # response is an AggregatedResult, which behaves like a list
    # there is a response object for each device in inventory
    devices = []
    for dev in response:
        print(response[dev].result)

Of note: the func param takes a string that is the actual RPC name to be run. 
You can find this by typing your command on the Juniper CLI and then piping it to "display xml rpc".
Try it out:

    show interfaces ge-0/0/0 detail | display xml rpc

The results will look like:

    <rpc-reply xmlns:junos="http://xml.juniper.net/junos/18.2R1/junos">
    <rpc>
        <get-interface-information>
                <level-extra>detail</level-extra>
                <interface-name>ge-0/0/0</interface-name>
        </get-interface-information>
    </rpc>
    <cli>
        <banner></banner>
    </cli>
    </rpc-reply>

You will want to use everything contained within the RPC tags. 
If there are additional items to specify, like level-extra and interface-name in this case, you can create a dictionary to contain them. 
These keys and values get unpacked at runtime by passing them in with the extras key:

    response = nr.run(
    task=pyez_rpc, func='get-interface-information', extras=extras)