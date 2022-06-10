pyez_route_info
===============

This is the equivalent to running "show route" and receiving the result as a Dict.
You can now add the following variable to filter the route : 
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
    destination: str = ""

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
