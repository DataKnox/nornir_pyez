pyez_sec_nat_dest
===============

This is the equivalent to running "show security nat destination rule all" and receiving the result as a Dict

Example::

    from nornir_pyez.plugins.tasks import pyez_sec_nat_dest
    from nornir import InitNornir

    import os
    
    script_dir = os.path.dirname(os.path.realpath(__file__))

    nr = InitNornir(config_file=f"{script_dir}/config.yaml")

    firewall = nr.filter(name="katy")

    response = firewall.run(
        task=pyez_sec_nat_dest
    )

    # response is an AggregatedResult, which behaves like a list
    # there is a response object for each device in inventory
    devices = []
    for dev in response:
        print(response[dev].result)
