/opt/local/bin/xmlsec1 encrypt --pubkey-cert-pem ../example/sp/pki/mycert.pem \
    --session-key aes128-cbc --xml-data pre_saml2_response.xml \
    --node-xpath '/*[local-name()="Response"]/*[local-name()="Assertion"]/*[local-name()="Subject"]/*[local-name()="EncryptedID"]/text()' \
    enc-element-aes128-cbc-rsa-oaep-mgflp.tmpl > enc.out