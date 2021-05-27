#!/usr/bin/env python

from pybatfish.client.commands import *
from pybatfish.question import load_questions
from pybatfish.question import bfq
import logging

def test_bgp_status():
    assert bfq.bgpSessionStatus() \
              .answer() \
              .frame() \
              .query('Established_Status != "ESTABLISHED"') \
              .empty
    
def test_all_svi_prefixes_are_on_all_leafs():
    # for each prefix set on each vlan interface
    for svi_prefixes in bfq.interfaceProperties(interfaces="/vlan.*/") \
                           .answer() \
                           .frame()['All_Prefixes']:
        for prefix in svi_prefixes:
            # each vlan prefix should be present on each node
            for node in bfq.nodeProperties().answer().frame()['Node']:
                assert not bfq.routes(nodes=node, network=prefix) \
                              .answer() \
                              .frame().empty, \
                              f"Prefix {prefix} is not present on {node}"

def init_bf():
    # contains a folder, configs, that has the config of all the leafs & spines
    SNAPSHOT_DIR = './add-leaf03/'

    logging.getLogger("pybatfish").setLevel(logging.WARN)

    bf_session.host = 'localhost'
    bf_set_network('mydc')
    bf_init_snapshot(SNAPSHOT_DIR, name='add-leaf03', overwrite=True)
    load_questions()


init_bf()


