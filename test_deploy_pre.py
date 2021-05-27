#!/usr/bin/env python

import ipaddress
from suzieq.sqobjects import get_sqobject

SPINES = ['spine01', 'spine02']
SPINE_IFNAME = 'Ethernet3'
NEW_SVI_PREFIX = '172.16.3.0/24'


def test_spines_are_all_alive():
    assert (get_sqobject('device')()
            .get(hostname=SPINES)
            .status == "alive") \
            .all()


def test_spine_port_is_free():
    # The port maybe already cabled to leaf03, but not configured
    # So verify that the LLDP peering is empty because LLDP has not
    # been configured on the new leaf
    assert (get_sqobject('lldp')()
            .get(hostname=SPINES, ifname=SPINE_IFNAME)
            .peerHostname == '') \
            .all()

def test_new_svi_prefix_is_unused():
    assert (get_sqobject('address')()
            .get(address=[NEW_SVI_PREFIX]).empty)
