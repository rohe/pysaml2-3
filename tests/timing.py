#!/usr/bin/env python

import time
from urllib.parse import parse_qs
from saml2 import BINDING_HTTP_REDIRECT
from saml2.client import Saml2Client
from saml2.server import Server
from saml2.saml import AUTHN_PASSWORD

__author__ = 'rolandh'

IDENTITY = {"eduPersonAffiliation": ["staff", "member"],
            "surName": ["Jeter"], "givenName": ["Derek"],
            "mail": ["foo@gmail.com"],
            "title": ["shortstop"]}

sp = Saml2Client(config_file="servera_conf")
idp = Server(config_file="idp_all_conf")

dest = sp._sso_location(entityid="urn:mace:example.com:saml:roland:idp",
                        binding=BINDING_HTTP_REDIRECT)

authn_request = sp.create_authn_request(destination=dest)
htargs = sp.apply_binding(BINDING_HTTP_REDIRECT, "%s" % authn_request, dest,
                          "abcd")

_dict = parse_qs(htargs["headers"][0][1].split('?')[1])


def main():
    for i in range(1000):
        req = idp.parse_authn_request(_dict["SAMLRequest"][0],
                                      BINDING_HTTP_REDIRECT)

        _sp_entity_id = req.message.issuer.text
        authn_context = (AUTHN_PASSWORD, "http://www.example.com/login")

        name_id = idp.ident.persistent_nameid("id12", _sp_entity_id)

        binding, destination = idp.pick_binding("assertion_consumer_service",
                                                entity_id=_sp_entity_id)

        _ = idp.create_authn_response(IDENTITY, "id12", destination,
                                      _sp_entity_id, name_id=name_id,
                                      authn=authn_context)

#import cProfile
#cProfile.run('main()')

start = time.time()
main()
print((time.time() - start))