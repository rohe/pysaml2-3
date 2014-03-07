foo = {'https://connect.sunet.se/shibboleth': {'spsso': [{










































































































































































                                                         'single_logout_service': [
                                                             {
                                                             'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:SOAP',
                                                             '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&SingleLogoutService',
                                                             'location': 'https://connect.sunet.se/Shibboleth.sso/SLO/SOAP'},
                                                             {
                                                             'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect',
                                                             '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&SingleLogoutService',
                                                             'location': 'https://connect.sunet.se/Shibboleth.sso/SLO/Redirect'},
                                                             {
                                                             'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST',
                                                             '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&SingleLogoutService',
                                                             'location': 'https://connect.sunet.se/Shibboleth.sso/SLO/POST'},
                                                             {
                                                             'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact',
                                                             '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&SingleLogoutService',
                                                             'location': 'https://connect.sunet.se/Shibboleth.sso/SLO/Artifact'}],
                                                         '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&SPSSODescriptor',
                                                         'protocol_support_enumeration': 'urn:oasis:names:tc:SAML:2.0:protocol urn:oasis:names:tc:SAML:1.1:protocol urn:oasis:names:tc:SAML:1.0:protocol',
                                                         'assertion_consumer_service': [
                                                             {'index': '1',
                                                              'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST',
                                                              '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&AssertionConsumerService',
                                                              'location': 'https://connect.sunet.se/Shibboleth.sso/SAML2/POST'},
                                                             {'index': '2',
                                                              'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST-SimpleSign',
                                                              '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&AssertionConsumerService',
                                                              'location': 'https://connect.sunet.se/Shibboleth.sso/SAML2/POST-SimpleSign'},
                                                             {'index': '3',
                                                              'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact',
                                                              '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&AssertionConsumerService',
                                                              'location': 'https://connect.sunet.se/Shibboleth.sso/SAML2/Artifact'},
                                                             {'index': '4',
                                                              'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:PAOS',
                                                              '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&AssertionConsumerService',
                                                              'location': 'https://connect.sunet.se/Shibboleth.sso/SAML2/ECP'},
                                                             {'index': '5',
                                                              'binding': 'urn:oasis:names:tc:SAML:1.0:profiles:browser-post',
                                                              '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&AssertionConsumerService',
                                                              'location': 'https://connect.sunet.se/Shibboleth.sso/SAML/POST'},
                                                             {'index': '6',
                                                              'binding': 'urn:oasis:names:tc:SAML:1.0:profiles:artifact-01',
                                                              '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&AssertionConsumerService',
                                                              'location': 'https://connect.sunet.se/Shibboleth.sso/SAML/Artifact'}],
                                                         'attribute_consuming_service': [
                                                             {'index': '0',
                                                              'service_description': [
                                                                  {'lang': 'en',
                                                                   'text': 'SUNET E-Meeting Service (Adobe Connect Pro)',
                                                                   '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&ServiceDescription'}],
                                                              '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&AttributeConsumingService',
                                                              'requested_attribute': [
                                                                  {
                                                                  '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&RequestedAttribute',
                                                                  'name': 'urn:oid:1.3.6.1.4.1.5923.1.1.1.6',
                                                                  'name_format': 'urn:oasis:names:tc:SAML:2.0:attrname-format:uri'},
                                                                  {
                                                                  '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&RequestedAttribute',
                                                                  'name': 'urn:oid:0.9.2342.19200300.100.1.3',
                                                                  'name_format': 'urn:oasis:names:tc:SAML:2.0:attrname-format:uri'},
                                                                  {
                                                                  '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&RequestedAttribute',
                                                                  'name': 'urn:oid:2.5.4.42',
                                                                  'name_format': 'urn:oasis:names:tc:SAML:2.0:attrname-format:uri'},
                                                                  {
                                                                  '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&RequestedAttribute',
                                                                  'name': 'urn:oid:2.5.4.4',
                                                                  'name_format': 'urn:oasis:names:tc:SAML:2.0:attrname-format:uri'},
                                                                  {
                                                                  '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&RequestedAttribute',
                                                                  'name': 'urn:oid:1.3.6.1.4.1.5923.1.1.1.9',
                                                                  'name_format': 'urn:oasis:names:tc:SAML:2.0:attrname-format:uri'}],
                                                              'service_name': [
                                                                  {'lang': 'en',
                                                                   'text': 'SUNET E-Meeting Service',
                                                                   '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&ServiceName'}]}],
                                                         'extensions': {
                                                         '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&Extensions',
                                                         'extension_elements': [
                                                             {'index': '1',
                                                              'binding': 'urn:oasis:names:tc:SAML:profiles:SSO:idp-discovery-protocol',
                                                              '__type__': 'urn:oasis:names:tc:SAML:profiles:SSO:idp-discovery-protocol&DiscoveryResponse',
                                                              'location': 'https://connect.sunet.se/Shibboleth.sso/DS/ds.swamid.se'},
                                                             {'index': '1',
                                                              'binding': 'urn:oasis:names:tc:SAML:profiles:SSO:idp-discovery-protocol',
                                                              '__type__': 'urn:oasis:names:tc:SAML:profiles:SSO:idp-discovery-protocol&DiscoveryResponse',
                                                              'location': 'https://connect.sunet.se/Shibboleth.sso/DS/ds.sunet.se'},
                                                             {'index': '1',
                                                              'binding': 'urn:oasis:names:tc:SAML:profiles:SSO:idp-discovery-protocol',
                                                              '__type__': 'urn:oasis:names:tc:SAML:profiles:SSO:idp-discovery-protocol&DiscoveryResponse',
                                                              'location': 'https://connect.sunet.se/Shibboleth.sso/DS/kalmar2'}]},
                                                         'key_descriptor': [{
                                                                            'key_info': {
                                                                            'key_name': [
                                                                                {
                                                                                'text': 'connect01.acp.sunet.se',
                                                                                '__type__': 'http://www.w3.org/2000/09/xmldsig#&KeyName'},
                                                                                {
                                                                                'text': 'https://connect.sunet.se/shibboleth',
                                                                                '__type__': 'http://www.w3.org/2000/09/xmldsig#&KeyName'}],
                                                                            'x509_data': [
                                                                                {
                                                                                'x509_subject_name': {
                                                                                'text': 'CN=connect01.acp.sunet.se',
                                                                                '__type__': 'http://www.w3.org/2000/09/xmldsig#&X509SubjectName'},
                                                                                'x509_certificate': {
                                                                                'text': 'MIIDLjCCAhagAwIBAgIJALJTE8wpfDmAMA0GCSqGSIb3DQEBBQUAMCExHzAdBgNV\n                        BAMTFmNvbm5lY3QwMS5hY3Auc3VuZXQuc2UwHhcNMDkwOTAyMTIwNTIwWhcNMTkw\n                        ODMxMTIwNTIwWjAhMR8wHQYDVQQDExZjb25uZWN0MDEuYWNwLnN1bmV0LnNlMIIB\n                        IjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzaNMBLHGgzRrAHLQDUiM+xu6\n                        ghKwdRqBcg171qVDeA4wSoVJLVeAY2xWKjudYzXtcwqL7qkDcHD3wOd0FLQSFfxE\n                        o67z4chBMNrkK9b9NgdHWp/Nb8gsdYNZt2ZjJVOD/oWTFXRHZDJhqkXFvVjL1gKu\n                        E3a2vDK6LRqYCLx5cyFleuRoqBvMrDxKLHvmqxo+Qt2e+ntL1sDVyKeMxgZc2s0/\n                        xGYFFzSVDT08XrWlgpN0AmxhfC0ULDb8YzQiJxsdeZ3C57RnC0InabCCvzPQsy9t\n                        c1VU/TNXkkXQn3H5aC+LUu8olnYndtFac56k/OaAUPe15/1MQVXvL8vbGG6JkQID\n                        AQABo2kwZzBGBgNVHREEPzA9ghZjb25uZWN0MDEuYWNwLnN1bmV0LnNlhiNodHRw\n                        czovL2Nvbm5lY3Quc3VuZXQuc2Uvc2hpYmJvbGV0aDAdBgNVHQ4EFgQUxPAGA++l\n                        tPOMkUezKJJrwSNAz/0wDQYJKoZIhvcNAQEFBQADggEBADJJgcI6VADyB8749iGB\n                        UbK97Zav6/YoX3jMH21tpO0+iZyPlfCxlDmNIBSSrHmNIs7g8sBSi+z8ko2IaSKS\n                        Ya0fI0N+cvBoi+3Wfszq0LpUSu/5pMWiw3DacOCNesR76h+FKD/UPgUL+LDw7ebz\n                        K3aeVvtsIjPijrcCaUKrZg5dv/5CRx/oQLbV20L3xk5UTTO/RNrR1gef37yEowDd\n                        d8hQaQgw5uujjjdkr/6u03kjO6rEZAySsiBPGcpBDXAbk4lnJVQltP0MBE4pu+es\n                        0oZu+lC7LltiBjJxdh/7SaqdLbn7G7cApwQKqXHVFITX9ncVMM04FtM9MzMc9d4y\n                        bUs=',
                                                                                '__type__': 'http://www.w3.org/2000/09/xmldsig#&X509Certificate'},
                                                                                '__type__': 'http://www.w3.org/2000/09/xmldsig#&X509Data'}],
                                                                            '__type__': 'http://www.w3.org/2000/09/xmldsig#&KeyInfo'},
                                                                            'use': 'signing',
                                                                            '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&KeyDescriptor'},
                                                                            {
                                                                            'key_info': {
                                                                            'key_name': [
                                                                                {
                                                                                'text': 'connect01.acp.sunet.se',
                                                                                '__type__': 'http://www.w3.org/2000/09/xmldsig#&KeyName'},
                                                                                {
                                                                                'text': 'https://connect.sunet.se/shibboleth',
                                                                                '__type__': 'http://www.w3.org/2000/09/xmldsig#&KeyName'}],
                                                                            'x509_data': [
                                                                                {
                                                                                'x509_subject_name': {
                                                                                'text': 'CN=connect01.acp.sunet.se',
                                                                                '__type__': 'http://www.w3.org/2000/09/xmldsig#&X509SubjectName'},
                                                                                'x509_certificate': {
                                                                                'text': 'MIIDLjCCAhagAwIBAgIJALJTE8wpfDmAMA0GCSqGSIb3DQEBBQUAMCExHzAdBgNV\n                        BAMTFmNvbm5lY3QwMS5hY3Auc3VuZXQuc2UwHhcNMDkwOTAyMTIwNTIwWhcNMTkw\n                        ODMxMTIwNTIwWjAhMR8wHQYDVQQDExZjb25uZWN0MDEuYWNwLnN1bmV0LnNlMIIB\n                        IjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzaNMBLHGgzRrAHLQDUiM+xu6\n                        ghKwdRqBcg171qVDeA4wSoVJLVeAY2xWKjudYzXtcwqL7qkDcHD3wOd0FLQSFfxE\n                        o67z4chBMNrkK9b9NgdHWp/Nb8gsdYNZt2ZjJVOD/oWTFXRHZDJhqkXFvVjL1gKu\n                        E3a2vDK6LRqYCLx5cyFleuRoqBvMrDxKLHvmqxo+Qt2e+ntL1sDVyKeMxgZc2s0/\n                        xGYFFzSVDT08XrWlgpN0AmxhfC0ULDb8YzQiJxsdeZ3C57RnC0InabCCvzPQsy9t\n                        c1VU/TNXkkXQn3H5aC+LUu8olnYndtFac56k/OaAUPe15/1MQVXvL8vbGG6JkQID\n                        AQABo2kwZzBGBgNVHREEPzA9ghZjb25uZWN0MDEuYWNwLnN1bmV0LnNlhiNodHRw\n                        czovL2Nvbm5lY3Quc3VuZXQuc2Uvc2hpYmJvbGV0aDAdBgNVHQ4EFgQUxPAGA++l\n                        tPOMkUezKJJrwSNAz/0wDQYJKoZIhvcNAQEFBQADggEBADJJgcI6VADyB8749iGB\n                        UbK97Zav6/YoX3jMH21tpO0+iZyPlfCxlDmNIBSSrHmNIs7g8sBSi+z8ko2IaSKS\n                        Ya0fI0N+cvBoi+3Wfszq0LpUSu/5pMWiw3DacOCNesR76h+FKD/UPgUL+LDw7ebz\n                        K3aeVvtsIjPijrcCaUKrZg5dv/5CRx/oQLbV20L3xk5UTTO/RNrR1gef37yEowDd\n                        d8hQaQgw5uujjjdkr/6u03kjO6rEZAySsiBPGcpBDXAbk4lnJVQltP0MBE4pu+es\n                        0oZu+lC7LltiBjJxdh/7SaqdLbn7G7cApwQKqXHVFITX9ncVMM04FtM9MzMc9d4y\n                        bUs=',
                                                                                '__type__': 'http://www.w3.org/2000/09/xmldsig#&X509Certificate'},
                                                                                '__type__': 'http://www.w3.org/2000/09/xmldsig#&X509Data'}],
                                                                            '__type__': 'http://www.w3.org/2000/09/xmldsig#&KeyInfo'},
                                                                            'use': 'encryption',
                                                                            '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&KeyDescriptor'}],
                                                         'manage_name_id_service': [
                                                             {
                                                             'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:SOAP',
                                                             '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&ManageNameIDService',
                                                             'location': 'https://connect.sunet.se/Shibboleth.sso/NIM/SOAP'},
                                                             {
                                                             'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect',
                                                             '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&ManageNameIDService',
                                                             'location': 'https://connect.sunet.se/Shibboleth.sso/NIM/Redirect'},
                                                             {
                                                             'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST',
                                                             '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&ManageNameIDService',
                                                             'location': 'https://connect.sunet.se/Shibboleth.sso/NIM/POST'},
                                                             {
                                                             'binding': 'urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact',
                                                             '__type__': 'urn:oasis:names:tc:SAML:2.0:metadata&ManageNameIDService',
                                                             'location': 'https://connect.sunet.se/Shibboleth.sso/NIM/Artifact'}]}]}}
