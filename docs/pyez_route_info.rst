pyez_route_info
===============

This is the equivalent to running "show route" and receiving the result as a Dict

Example::

    from nornir_pyez.plugins.tasks import pyez_route_info
    import os
    from nornir import InitNornir
    from rich import print

    script_dir = os.path.dirname(os.path.realpath(__file__))

    nr = InitNornir(config_file=f"{script_dir}/config.yml")

    response = nr.run(
        task=pyez_route_info
    )

    # response is an AggregatedResult, which behaves like a list
    # there is a response object for each device in inventory
    devices = []
    for dev in response:
        print(response[dev].result)
