import base64


encoded = 'RG8gbm90IHNldCBzZWNyZXRzIGluIGltYWdlcw=='
decoded = base64.b64decode(encoded)
print(decoded)
