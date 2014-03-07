echo "authn_context"
../../tools/parse_xsd2.py saml-schema-authn-context-2.0.xsd > authn_context.py
echo "authn_context_types"
../../tools/parse_xsd2.py saml-schema-authn-context-types-2.0.xsd > authn_context_types.py
echo "mobiletwofactor"
../../tools/parse_xsd2.py saml-schema-authn-context-mobiletwofactor-reg-2.0.xsd > mobiletwofactor.py
echo "ippword"
../../tools/parse_xsd2.py saml-schema-authn-context-ippword-2.0.xsd.xml > ippword.py
echo "pword"
../../tools/parse_xsd2.py saml-schema-authn-context-pword-2.0.xsd.xml > pword.py
echo "ppt"
../../tools/parse_xsd2.py saml-schema-authn-context-ppt-2.0.xsd.xml > ppt.py
echo "sslcert"
../../tools/parse_xsd2.py saml-schema-authn-context-sslcert-2.0.xsd.xml > sslcert.py
