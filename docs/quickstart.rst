quickstart
==========

1) Install Nornir_PyEZ::

    pip install nornir-pyez==0.2.1


2) Import the Task you care about, such as collecting facts::

    from nornir_pyez.plugins.tasks import pyez_facts


3) Use in a script::

    from nornir_pyez.plugins.tasks import pyez_facts
    from nornir import InitNornir
    from rich import print
    import os

    script_dir = os.path.dirname(os.path.realpath(__file__))

    nr = InitNornir(config_file=f"{script_dir}/config.yml")

    response = nr.run(
        pyez_facts
    )

    # response is an AggregatedResult, which behaves like a list
    # there is a response object for each device in inventory
    devices = []
    for dev in response:
        print(response[dev].result)


See Contacts for any issues