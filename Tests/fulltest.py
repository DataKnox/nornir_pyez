from nornir_pyez.plugins.tasks import pyez_config, pyez_diff, pyez_commit
import os
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from rich import print
from nornir.core.plugins.connections import ConnectionPluginRegister
from nornir_pyez.plugins.connections import Pyez


ConnectionPluginRegister.register("pyez", Pyez)


script_dir = os.path.dirname(os.path.realpath(__file__))


nr = InitNornir(config_file=f"{script_dir}/config.yml")

xml_payload = """
<configuration>
          <interfaces>
                   <interface>
                    <name>lo0</name>
                    <unit>
                        <name>0</name>
                        <family operation="replace">
                            <inet>
                                <address>
                                    <name>3.3.3.3/32</name>
                                </address>
                            </inet>
                        </family>
                    </unit>
                </interface>
            </interfaces>
</configuration>
"""


def mega_runner(task):
    send_result = task.run(
        task=pyez_config, payload=xml_payload, data_format='xml')
    if send_result:
        diff_result = task.run(task=pyez_diff)
        if diff_result:
            task.run(task=pyez_commit)


response = nr.run(task=mega_runner)
print_result(response)
