from nornir_pyez.plugins.tasks import pyez_facts
import os
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from rich import print
from nornir.core.plugins.connections import ConnectionPluginRegister
from nornir_pyez.plugins.connections import Pyez


ConnectionPluginRegister.register("pyez", Pyez)


script_dir = os.path.dirname(os.path.realpath(__file__))


nr = InitNornir(config_file=f"{script_dir}/config.yml")

response = nr.run(
    pyez_facts
)

# response is an AggregatedResult, which behaves like a list
# there is a response object for each device in inventory
devices = []
for dev in response:
    print(response[dev].result)
