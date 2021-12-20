pyez_commit
===========

Use this task to commit the candidate datastore to the committed datastore. You can add an optional comment. Note this performs a commit check first and performs a Rollback upon failure

Example::

    from nornir_pyez.plugins.tasks import pyez_diff
    import os
    from nornir import InitNornir
    from nornir_utils.plugins.functions import print_result
    from rich import print

    script_dir = os.path.dirname(os.path.realpath(__file__))

    nr = InitNornir(config_file=f"{script_dir}/config.yml")

    response = nr.run(
        task=pyez_commit, comment="Your comment"
    )

    print_result(response)
