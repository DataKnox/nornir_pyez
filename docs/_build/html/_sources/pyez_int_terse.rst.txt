pyez_int_terse
==============

This is the equivalent to running "show interfaces terse" and receiving the result as a Dict

Example::

    from nornir_pyez.plugins.tasks import pyez_int_terse
    import os
    from nornir import InitNornir
    from rich import print

    script_dir = os.path.dirname(os.path.realpath(__file__))

    nr = InitNornir(config_file=f"{script_dir}/config.yml")

    response = nr.run(
        task=pyez_int_terse
    )

    # response is an AggregatedResult, which behaves like a list
    # there is a response object for each device in inventory
    devices = []
    for dev in response:
        print(response[dev].result)
