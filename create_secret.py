import jwt
from datetime import datetime
from datetime import timedelta

key_file = 'key.txt' # file where you stored your private key

# fill in
team_id = ''
client_id = ''
key_id = ''

file = open(key_file)

ecdsa_key = file.read()

headers = {
        'kid': key_id
    }

claims = {
	'iss': team_id,
	'iat': datetime.now(),
	'exp': datetime.now() + timedelta(days=180),
	'aud': 'https://appleid.apple.com',
	'sub': client_id,
    }

token = jwt.encode(claims, ecdsa_key, algorithm='ES256', headers=headers)

file.close()

print token
