from saml2 import BINDING_SOAP
from saml2.saml import NAMEID_FORMAT_TRANSIENT
from saml2.samlp import NameIDPolicy
from saml2.server import Server
from saml2.client import Saml2Client
from saml2.time_util import in_a_while

__author__ = 'rolandh'


def test_handle_logout_soap():
    sp = Saml2Client(config_file="servera_conf")
    idp = Server(config_file="idp_all_conf")

    policy = NameIDPolicy(format=NAMEID_FORMAT_TRANSIENT,
                          sp_name_qualifier=sp.config.entityid,
                          allow_create="true")

    name_id = idp.ident.construct_nameid("subject", name_id_policy=policy)

    binding, destination = idp.pick_binding("single_logout_service",
                                            [BINDING_SOAP],
                                            entity_id=sp.config.entityid)

    request = idp.create_logout_request(destination, idp.config.entityid,
                                        name_id=name_id)
    args = idp.apply_binding(BINDING_SOAP, "%s" % request, destination)

    # register the user
    session_info = {
        "name_id": name_id, "issuer": idp.config.entityid,
        "not_on_or_after": in_a_while(minutes=15),
        "ava": {
            "givenName": "Anders",
            "surName": "Andersson",
            "mail": "anders.andersson@example.com"
        }
    }
    sp.users.add_information_about_person(session_info)

    reply_args = sp.handle_logout_request(args["data"], name_id, binding,
                                          sign=False)

    print(reply_args)
    assert reply_args["method"] == "POST"
    assert reply_args["headers"] == [('content-type', 'application/soap+xml')]


#if __name__ == "__main__":
#    test_handle_logout_soap()