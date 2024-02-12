pyez_scp
===========

Use this task to scp files onto or from your devices. Default's to PUT operation i.e. send local file to the device (unfortunately there is no way 
to check if the copy was successful or not, you will have to check manually)

Example::

    from nornir_pyez.plugins.tasks import pyez_scp
    import os
    from nornir import InitNornir
    from nornir_utils.plugins.functions import print_result

    script_dir = os.path.dirname(os.path.realpath(__file__))
    filename = "<your_filename>"
    # Default is put if argument is omitted
    direction = "<get_or_put>"

    nr = InitNornir(config_file=f"{script_dir}/config.yml")

    response = task.run(
        task=pyez_scp,
        direction=direction,
        file=f"{script_dir}./files/{filename}",
        path=path,
    )

    print_result(response)
