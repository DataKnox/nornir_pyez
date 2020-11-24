from nornir_pyez.plugins.tasks import pyez_config, pyez_diff, pyez_commit
import os
from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.data import load_yaml
from rich import print
from nornir.core.plugins.connections import ConnectionPluginRegister
from nornir_pyez.plugins.connections import Pyez


ConnectionPluginRegister.register("pyez", Pyez)


script_dir = os.path.dirname(os.path.realpath(__file__))


nr = InitNornir(config_file=f"{script_dir}/config.yml")


def template_config(task):
    # retrieve data from groups.yml
    data = {}
    data['dns_server'] = task.host['dns_server']
    data['ntp_server'] = task.host['ntp_server']
    print(data)
    response = task.run(
        task=pyez_config, template_path='junos.j2', template_vars=data, data_format='set')
    if response:
        diff = task.run(pyez_diff)
    if diff:
        task.run(task=pyez_commit)


response = nr.run(
    task=template_config)
print_result(response)
