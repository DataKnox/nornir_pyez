pyez_cmd
===========

Use this task to execute single command on your devices.
You can just display the whole result or parse it.  Depending
on various factors, you may need to wrap the command in
'cli -c' as if you are operating within the shell instead of
JunOS.

Example::

    from nornir_pyez.plugins.tasks import pyez_scp
    import os
    from nornir import InitNornir
    from nornir_utils.plugins.functions import print_result
    from rich import print

    script_dir = os.path.dirname(os.path.realpath(__file__))

    command = "show system information"

    nr = InitNornir(config_file=f"{script_dir}/config.yml")

   response = task.run(
        task=pyez_cmd,
        command=command
    )

    # Print the whole result
    print_result(response)

    # Or parse it (and do whatever you want)
    for key in response.keys():
        result = response[key][1].result

StartShell command example::

    command = 'cli -c "show system information"'
