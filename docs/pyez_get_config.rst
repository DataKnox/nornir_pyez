pyez_get_config
===============

1. Import pyez_get_config::

    from nornir_pyez.plugins.tasks import pyez_get_config

2. This function can be sent naked in order to get the entire running config. The response is returned as a Dict::

    from nornir_pyez.plugins.tasks import pyez_get_config
    import os
    from nornir import InitNornir
    from rich import print

    script_dir = os.path.dirname(os.path.realpath(__file__))

    nr = InitNornir(config_file=f"{script_dir}/config.yml")

    response = nr.run(
        task=pyez_get_config
    )

    # response is an AggregatedResult, which behaves like a list
    # there is a response object for each device in inventory
    devices = []
    for dev in response:
        print(response[dev].result)

3. This function can be provided with parameters database and filter_xml , just as you would with PyEZ::

    from nornir_pyez.plugins.tasks import pyez_get_config
    import os
    from nornir import InitNornir
    from rich import print

    script_dir = os.path.dirname(os.path.realpath(__file__))

    nr = InitNornir(config_file=f"{script_dir}/config.yml")
    # Can use either an XPath or a Subtree
    xpath = 'interfaces/interface'
    xml = '<interfaces></interfaces>'
    database = 'committed'

    response = nr.run(
        task=pyez_get_config, filter_xml=xpath, database=database
    )

    # response is an AggregatedResult, which behaves like a list
    # there is a response object for each device in inventory
    devices = []
    for dev in response:
        print(response[dev].result)
