pyez_get_arp
=========

Use this task to get the optics diag info from a device

Example::

    from nornir_pyez.plugins.tasks.pyez_optics_diag import pyez_get_int_optics_diag_info
    import os
    from nornir import InitNornir
    from rich import print

    script_dir = os.path.dirname(os.path.realpath(__file__))

    nr = InitNornir(config_file=f"{script_dir}/config.yml")

    response = nr.run(
        task=pyez_get_int_optics_diag_info
    )

    print_result(response)
