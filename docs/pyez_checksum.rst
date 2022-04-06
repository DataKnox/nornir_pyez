pyez_checksum
===========

Use this task to calculate the checksum (md5, sha or sha256) of a file in the remote Juniper device.

Example::

    from nornir_pyez.plugins.tasks import pyez_checksum
    import os
    from nornir import InitNornir
    from nornir_utils.plugins.functions import print_result

    script_dir = os.path.dirname(os.path.realpath(__file__))
    filename = "<your_filename>"
    path = "<your_path>"

    nr = InitNornir(config_file=f"{script_dir}/config.yml"

    response = netbox_inventory.run(
        task=pyez_checksum, filepath=f"{path}/{filename}", calc="sha256",
    )
    print_result(response)
    for key in response.keys():
        remote_hash = response[key][0].result

    return remote_hash
