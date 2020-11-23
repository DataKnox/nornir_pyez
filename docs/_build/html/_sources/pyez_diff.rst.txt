pyez_diff
=========

Use this task to return a diff between the candidate datastore and committed datastore

Example::

    from nornir_pyez.plugins.tasks import pyez_diff
    import os
    from nornir import InitNornir
    from rich import print

    script_dir = os.path.dirname(os.path.realpath(__file__))

    nr = InitNornir(config_file=f"{script_dir}/config.yml")

    response = nr.run(
        task=pyez_diff
    )

    print_result(response)
