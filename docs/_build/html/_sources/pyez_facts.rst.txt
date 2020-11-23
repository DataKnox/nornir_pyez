pyez_facts
==========

1. Import the Task you care about, such as collecting facts::

    from nornir_pyez.plugins.tasks import pyez_facts


2. Use in a script::

    from nornir_pyez.plugins.tasks import pyez_facts
    from nornir import InitNornir
    from rich import print
    import os

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


Output::

    {'2RE': False,
    'HOME': '/var/home/knox',
    'RE0': {'last_reboot_reason': '0x1:power cycle/failure',
            'mastership_state': 'master',
            'model': 'RE-SRX300',
            'status': 'OK',
            'up_time': '1 day, 26 minutes, 46 seconds'},
    'RE1': None,
    'RE_hw_mi': False,
    'current_re': ['master',
                    'node',
                    'fwdd',
                    'member',
                    'pfem',
                    'backup',
                    'fpc0',
                    're0',
                    'fpc0.pic0'],
    'domain': None,
    'fqdn': 'Srx',
    'hostname': 'Srx',
    'hostname_info': {'re0': 'Srx'},
    'ifd_style': 'CLASSIC',
    'junos_info': {'re0': {'object': junos.version_info(major=(19, 3), type=R, minor=1, 
    build=8),
                            'text': '19.3R1.8'}},
    'master': 'RE0',
    'model': 'SRX300',
    'model_info': {'re0': 'SRX300'},
    'personality': 'SRX_BRANCH',
    're_info': {'default': {'0': {'last_reboot_reason': '0x1:power cycle/failure',
                                'mastership_state': 'master',
                                'model': 'RE-SRX300',
                                'status': 'OK'},
                            'default': {'last_reboot_reason': '0x1:power '
                                                            'cycle/failure',
                                        'mastership_state': 'master',
                                        'model': 'RE-SRX300',
                                        'status': 'OK'}}},
    're_master': {'default': '0'},
    'serialnumber': 'CV3216AF0510',
    'srx_cluster': False,
    'srx_cluster_id': None,
    'srx_cluster_redundancy_group': None,
    'switch_style': 'VLAN_L2NG',
    'vc_capable': False,
    'vc_fabric': None,
    'vc_master': None,
    'vc_mode': None,
    'version': '19.3R1.8',
    'version_RE0': '19.3R1.8',
    'version_RE1': None,
    'version_info': junos.version_info(major=(19, 3), type=R, minor=1, build=8),
    'virtual': False}


See contacts for support