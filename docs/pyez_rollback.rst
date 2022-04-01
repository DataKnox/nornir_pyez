pyez_rollback
===========

Use this task to rollback to a previous configuration or delete a pending config in the candidate datastore and unlock for next config.

Example::

    from nornir_pyez.plugins.tasks import pyez_rollback
    import os
    from nornir import InitNornir
    from nornir_utils.plugins.functions import print_result
    from rich import print

    script_dir = os.path.dirname(os.path.realpath(__file__))

    nr = InitNornir(config_file=f"{script_dir}/config.yml")

    response = nr.run(
        task=pyez_rollback,
        rollback_number=2
    )

    print_result(response)
