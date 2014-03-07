/opt/local/bin/xmlsec1 decrypt --privkey-pem ../example/sp/pki/mykey.pem \
  --node-xpath '/*[local-name()="Response"]/*[local-name()="Assertion"]/*[local-name()="Subject"]/*[local-name()="EncryptedID"]' \
  --print-debug \
  --trusted-pem ../example/sp/pki/mycert.pem enc_out.xml