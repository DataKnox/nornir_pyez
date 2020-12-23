# PyEZ Plugins for Nornir

## Plugins

Connections - Pyez

## Description

This plugin is used to leverage the power of Juniper's PyEZ with the Nornir framework to offer quicker and more stable delivery of network services while also simplifying and abstracting network inventory

## Installation

```
pip install nornir-pyez==0.0.10
```

## Update

```
pip3 install --upgrade nornir_pyez
```

## Read the Documentation

https://nornir-pyez.readthedocs.io/en/latest/

## Usages

pyez get facts:

```python
from nornir_pyez.plugins.tasks import pyez_facts
import os
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from rich import print

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

```

PyEZ Get Config

```python
from nornir_pyez.plugins.tasks import pyez_get_config
import os
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from rich import print

script_dir = os.path.dirname(os.path.realpath(__file__))


nr = InitNornir(config_file=f"{script_dir}/config.yml")

response = nr.run(
    task=pyez_get_config
)

# response is an AggregatedResult, which behaves like a list
# there is a response object for each device in inventory
devices = []
for dev in response:
    print(response[dev].result)

```
Get Configs with Args

```python
from nornir_pyez.plugins.tasks import pyez_get_config
import os
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from rich import print

script_dir = os.path.dirname(os.path.realpath(__file__))


nr = InitNornir(config_file=f"{script_dir}/config.yml")

xpath = 'interfaces/interface'
xml = '<interfaces></interfaces>'
database = 'committed'

response = nr.run(
    task=pyez_get_config, filter_xml=xpath, database=database
)

# response is an AggregatedResult, which behaves like a list
# there is a response object for each device in inventory
devices = []
for dev in response:
    print(response[dev].result)
```

Set text config
```python
from nornir_pyez.plugins.tasks import pyez_config
import os
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from rich import print

script_dir = os.path.dirname(os.path.realpath(__file__))


nr = InitNornir(config_file=f"{script_dir}/config.yml")

payload = """interfaces {
    lo0 {
        unit 0 {
            family inet {
                address 3.3.3.3/32;
            }
        }
    }
}
"""

response = nr.run(
    task=pyez_config, payload=payload
)

# response is an AggregatedResult, which behaves like a list
# there is a response object for each device in inventory
devices = []
for dev in response:
    print(response[dev].result)
```

Full test with Operation of Replace Config using XML
```python
from nornir_pyez.plugins.tasks import pyez_config, pyez_diff, pyez_commit
import os
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from rich import print

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
                                    <name>3.3.3.4/32</name>
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
```

Show Interfaces Terse
```python
from nornir_pyez.plugins.tasks import pyez_int_terse
import os
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from rich import print

script_dir = os.path.dirname(os.path.realpath(__file__))

nr = InitNornir(config_file=f"{script_dir}/config.yml")

response = nr.run(
    task=pyez_int_terse
)

# response is an AggregatedResult, which behaves like a list
# there is a response object for each device in inventory
devices = []
for dev in response:
    print(response[dev].result)

```
Get Route Information
```python
from nornir_pyez.plugins.tasks import pyez_route_info
import os
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from rich import print

script_dir = os.path.dirname(os.path.realpath(__file__))

nr = InitNornir(config_file=f"{script_dir}/config.yml")

response = nr.run(
    task=pyez_route_info
)

# response is an AggregatedResult, which behaves like a list
# there is a response object for each device in inventory
devices = []
for dev in response:
    print(response[dev].result)

```

## Contacts

- https://dataknox.dev
- https://twitter.com/data_knox
- https://youtube.com/c/dataknox
- https://learn.gg/dataknox
