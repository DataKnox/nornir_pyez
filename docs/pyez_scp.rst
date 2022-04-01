pyez_scp
===========

Use this task to scp files on your devices (unfortunately there is no way 
to check if the copy was successfull or not, you will have to check manually)

Example::

    from nornir_pyez.plugins.tasks import pyez_scp
    import os
    from nornir import InitNornir
    from nornir_utils.plugins.functions import print_result
    from rich import print

    script_dir = os.path.dirname(os.path.realpath(__file__))
    filename = "<your_filename>"

    nr = InitNornir(config_file=f"{script_dir}/config.yml")

    response = task.run(
        task=pyez_scp,
        file=f"{script_dir}./files/{filename}",
        path=path,
    )

    print_result(response)
