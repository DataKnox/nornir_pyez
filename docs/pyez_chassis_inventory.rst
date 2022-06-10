pyez_get_arp
=========

Use this task to get the chassis inventory from a device

Example::

    from nornir_pyez.plugins.tasks import pyez_chassis_inventory
    import os
    from nornir import InitNornir
    from rich import print

    script_dir = os.path.dirname(os.path.realpath(__file__))

    nr = InitNornir(config_file=f"{script_dir}/config.yml")

    response = nr.run(
        task=pyez_chassis_inventory,
        models=False
    )

    print_result(response)
