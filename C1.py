# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))