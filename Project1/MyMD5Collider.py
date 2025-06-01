from hashlib import md5

hashes =[md5(b'HTBUser132'), md5(b'JohnMarcus')]

characters = """1234567890-=_+qwertyuiop[\]{}|QWERTYUIOPasdfghjklASDFGHJKL;':"zxcvbnmZXCVBNM<>?,./ZXCVBNM"""

test = b''

while True:
    for i in characters:
        test_hash = md5(test + i)