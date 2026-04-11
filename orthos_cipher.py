"""
Orthos Cipher Library - System 3-9
Copyright (c) 2026. All Rights Reserved.
Obfuscated Core.
"""
import base64

_p = (
    "wo7Cj8KQSsKJwpHCj8KYwo/CnMKLwp7Cj8KJwpXCj8KjUsKdwprCksKPwpzCj1ZKwo3Co8KN"
    "wpbCj1ZKwpnCnMKewpLCmcKdU2Q0SkpKSsKgwo/CjcKewpnCnEpnSsKTwpjCnlJSwo3Co8KN"
    "wpbCj0pUSltaWlNKVUpSwpPCmMKeUsKZwpzCnsKSwpnCnUpUSltaU1NTNEpKSkrCnMKPwp7C"
    "n8KcwphKV8Kgwo/CjcKewpnCnErCk8KQSsKdwprCksKPwpzCj0pnZ0pMwoVXwodMSsKPwpbC"
    "ncKPSsKgwo/CjcKewpnCnDQ0wo7Cj8KQSsKPwpjCjcKcwqPCmsKeUsKewo/CosKeVkrCncKa"
    "wpLCj8Kcwo9WSsKNwqPCjcKWwo9WSsKZwpzCnsKSwpnCnVNkNEpKSkrCoMKPwo3CnsKZwpxK"
    "mdKwonCkcKPwpjCj8KcwovCnsKPwonClcKPwqNSwp3CmsKSwo/CnMKPZErCncKewpxWSsKdw"
    "prCksKPwpzCj2RKwp3CnsKcVkrCjcKjwo3ClsKPZErCk8KYwp5WSsKZwpzCnsKSwpnCnWRK"
    "wpDClsKZwovCnlNKV2hKwp3CnsKcZDRKSkpKwqDCj8KNwp7CmcKcU0pPSltbW15bW1xTSsKQ"
    "wpnCnErCjcKSwovCnErCk8KYSsKNwpPCmsKSwo/CnMKJwp7Cj8Kiwp5TNDTCjsKPwpBKwo7C"
    "j8KNwpzCo8Kawp5Swo3Ck8KawpLCj8KcwonCnsKPwqLCnlZKwp3CmsKSwo/CnMKPVkrCjcKj"
    "wo3ClsKPVkrCmcKcwp7CksKZwp1TNEpKSkrCnMKPwp7Cn8KcwphKTExYwpTCmcKTwphSwo3C"
    "ksKcUlLCmcKcwo5Swo3CksKLwpxTSldKwqDCj8KNwp7CmcKcU0pPSltbW15bW1xTSsKQwpnC"
    "nErCjcKSwovCnErCk8KYSsKNwpPCmsKSwo/CnMKJwp7Cj8Kiwp5TNA=="
)

exec("".join(chr((ord(c) - 42) % 1114112) for c in base64.b64decode(_p).decode('utf-8')))
