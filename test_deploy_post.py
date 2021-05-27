#!/usr/bin/env python

import ipaddress
from suzieq.sqobjects import get_sqobject

SPINES = ['spine01', 'spine02']
NEW_LEAF = "leaf03"
LEAF_IF = ["Ethernet1", "Ethernet2"]
SPINE_IFNAME = 'Ethernet3'
NEW_SVI_PREFIX = '172.16.3.0/24'


def test_spine_leaf_connected():
    # Validate that the peer host is correct
    assert (get_sqobject('lldp')()
            .get(hostname=SPINES, ifname=SPINE_IFNAME)
            .peerHostname == NEW_LEAF) \
            .all()
    # Validate that the peer interface is correct
    assert (get_sqobject('lldp')()
            .get(hostname=NEW_LEAF, ifname=LEAF_IF)
            .peerIfname == SPINE_IFNAME) \
            .all()

def test_new_svi_prefix_is_assigned():
    assert (get_sqobject('address')()
            .get(address=[NEW_SVI_PREFIX]).hostname == NEW_LEAF).all()

def test_all_svi_prefixes_are_on_all_leafs():
    for node in get_sqobject('device')().get().hostname:
        for svi_prefix in get_sqobject('interfaces')() \
                          .get(hostname=[node], type='vlan').ipAddressList:
            for prefix in svi_prefix:
                ip_pfx = str(ipaddress.ip_network(prefix, strict=False))
                assert (get_sqobject('routes')()
                        .get(hostname=[node], prefix=[ip_pfx])
                        .prefix == ip_pfx).all()
