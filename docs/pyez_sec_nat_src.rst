pyez_sec_nat_src
================

This is equivalent to running "show security nat source rule" on a Juniper SRX. Execution of this function will send the RPC call over the NETCONF API on your firewall, and handle the XML-to-JSON translation of the returned data.

Example::

    from nornir_pyez.plugins.tasks import pyez_sec_nat_src
    from nornir import InitNornir

    import os
    
    # create an object that stores the path of working directory (pwd) of your script
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # instantiate Nornir as an object named nr, point to your config file with 
    nr = InitNornir(config_file=f"{script_dir}/config.yaml")

    # filter for a network device with the name of "katy"
    firewall = nr.filter(name="katy")

    # create the nornir task, storing the output our RPC function in an object named "response"
    response = firewall.run(
        task=pyez_sec_nat_src
    )

    # response is an AggregatedResult, which behaves like a list
    # there is a response object for each device in inventory
    for dev in response:
        print(response[dev].result)


If you would like to specify a rule by it's name, pass the argument when your task is created. If this is omitted from the task, the assumption is that you want all rules returned.

Example::

    from nornir_pyez.plugins.tasks import pyez_sec_nat_src
    from nornir import InitNornir

    import os
    
    script_dir = os.path.dirname(os.path.realpath(__file__))

    nr = InitNornir(config_file=f"{script_dir}/config.yaml")

    firewall = nr.filter(name="katy")

    response = firewall.run(
        task=pyez_sec_nat_src,
        rule="r1"
    )

    for dev in response:
        print(response[dev].result)
