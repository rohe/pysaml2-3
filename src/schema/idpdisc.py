#!/usr/bin/env python

#
# Generated Sun Oct 21 15:45:53 2012 by parse_xsd.py version 0.4.
#

import saml2
from saml2 import SamlBase

import sm as md

NAMESPACE = 'urn:oasis:names:tc:SAML:profiles:SSO:idp-discovery-protocol'

class DiscoveryResponse(md.IndexedEndpointType_):
    """The urn:oasis:names:tc:SAML:profiles:SSO:idp-discovery-protocol:DiscoveryResponse element """

    c_tag = 'DiscoveryResponse'
    c_namespace = NAMESPACE
    c_children = md.IndexedEndpointType_.c_children.copy()
    c_attributes = md.IndexedEndpointType_.c_attributes.copy()
    c_child_order = md.IndexedEndpointType_.c_child_order[:]
    c_cardinality = md.IndexedEndpointType_.c_cardinality.copy()

def discovery_response_from_string(xml_string):
    return saml2.create_class_from_xml_string(DiscoveryResponse, xml_string)


ELEMENT_FROM_STRING = {
    DiscoveryResponse.c_tag: discovery_response_from_string,
}

ELEMENT_BY_TAG = {
    'DiscoveryResponse': DiscoveryResponse,
}


def factory(tag, **kwargs):
    return ELEMENT_BY_TAG[tag](**kwargs)

