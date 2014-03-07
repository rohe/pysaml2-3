from saml2 import BINDING_HTTP_POST
from pathutils import full_path

__author__ = 'rolandh'

BASE = "http://idp.com/sso"

CONFIG = {
    "entityid": "http://idp.com/sso/ssoHandler.cfm",
    "service": {
        "idp": {
            "endpoints": {
                "single_sign_on_service": [
                    ("%s/sso" % BASE, BINDING_HTTP_POST)],
            },
        },
    },
    "cert_file": full_path("test.pem"),
}
