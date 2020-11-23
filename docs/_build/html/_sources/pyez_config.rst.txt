pyez_config.rst
===============

1. Begin by importing your method::

    from nornir_pyez.plugins.tasks import pyez_config

2. Now you will need to decide which serialization that you want to send the data in with. 'text' is the default. Payload must be passed as a string
A text payload example::

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

Take notice of the XML payload's ability to use attributes like operation="replace" This will remove and replace this subtree of the candidate config.
An XML payload example::

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

Note JSON is also a valid payload with data_format='json' set

3. Next you need to decide if you want to commit the changes now, or create a new task to view the diff

Example of NO commit now::

    send_result = task.run(
        task=pyez_config, payload=xml_payload, data_format='xml')

Example of commit now::

    send_result = task.run(
        task=pyez_config, payload=xml_payload, data_format='xml', commit_now=True)

Full example::

    from nornir_pyez.plugins.tasks import pyez_config
    import os
    from nornir import InitNornir
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
