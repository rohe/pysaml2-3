echo "xmldsig"
../../tools/parse_xsd2.py -d defs_xmldsig.py xmldsig-core-schema.xsd > xd.py
echo "xenc"
../../tools/parse_xsd2.py -i xd xenc-schema.xsd > xe.py
echo "saml assertion"
../../tools/parse_xsd2.py -i xd -i xe -d defs_saml.py saml-schema-assertion-2.0.xsd > sa.py
echo "saml protocol"
../../tools/parse_xsd2.py -i xd -i xe -i sa -d defs_samlp.py saml-schema-protocol-2.0.xsd > sp.py
echo "saml metadata"
../../tools/parse_xsd2.py -i xd -i xe -i sa saml-schema-metadata-2.0.xsd > sm.py
echo "saml metadata ui"
../../tools/parse_xsd2.py -i xd -i xe -i sa -i sm sstc-saml-metadata-ui-v1.0.xsd > mdui.py
echo "dri"
../../tools/parse_xsd2.py -i xd -i xe -i sa -i sm -i mdui dri.xsd > dri.py
echo "metadata attr"
../../tools/parse_xsd2.py -i xd -i xe -i sa sstc-metadata-attr.xsd > mdattr.py
echo "shib metadata"
../../tools/parse_xsd2.py -i xd shibboleth-metadata-1.0.xsd > shb.py
echo "wsdl"
../../tools/parse_xsd2.py wsdl.xml > wsdl.py
echo "soap"
../../tools/parse_xsd2.py -i wsdl soap.xml > soap.py
echo "soap envelope"
../../tools/parse_xsd2.py -i wsdl envelope.xml > soapenv.py
echo "poas"
../../tools/parse_xsd2.py -i wsdl -i soap -i soapenv liberty-schema-paos-1.1.xsd > paos.py
echo "ecp"
../../tools/parse_xsd2.py -i wsdl -i soapenv -i xd -i xe -i sa -i sp saml-schema-ecp-2.0.xsd.xml > ecp.py
echo "idpdisc"
../../tools/parse_xsd2.py -i xd -i xe -i sa -i sm idpdisc.xml > idpdisc.py
echo "mdrpi"
../../tools/parse_xsd2.py -i xd -i xe -i sa -i sm saml-metadata-rpi-v1.0-wd06.xsd > mdrpi.py
