pyez_get_arp
=========

Use this task to get the arp entry from a device

Example::

    from nornir_pyez.plugins.tasks.pyez_arp_noresolve import pyez_get_arp
    import os
    from nornir import InitNornir
    from rich import print

    script_dir = os.path.dirname(os.path.realpath(__file__))

    nr = InitNornir(config_file=f"{script_dir}/config.yml")

    response = nr.run(
        task=pyez_get_arp,
        no_resolve=False
    )

    print_result(response)
