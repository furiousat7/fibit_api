import urllib2
import urllib
import base64
import fitbit_keys

tokens = fitbit_keys.tokens
client_codes = fitbit_keys.client_codes


oAuthUrl = 'https://api.fitbit.com/oauth2/token'

def checkIfTokenIsValid():
	# requestBody = {
	# 	'code': client_codes.get('code'),
	# 	'redirect_uri': client_codes.get('redirect_uri'),
	# 	'client_id': client_codes.get('client_id'),
	# 	'grant_type': 'authorization_code'
	# }
	import pdb; pdb.set_trace()	
	requestBody = {
	 	'grant_type' : 'refresh_token',
        'refresh_token' : tokens.get('refresh_token')
    }

	try:
		encodedRequestBody = urllib.urlencode(requestBody)
		request = urllib2.Request(oAuthUrl, encodedRequestBody)

		request.add_header('Authorization', 'Basic ' + base64.b64encode(client_codes.get('client_id')  +  ":" + client_codes.get('client_secret')))
		request.add_header('Content-Type', 'application/x-www-form-urlencoded')

		response = urllib2.urlopen(request).read()

		print response
	except urllib2.URLError as e:
		print e.code
		print e.read()

if __name__ == '__main__':

	# checkIfTokenIsValid()
	import pdb; pdb.set_trace()	
	url = "https://api.fitbit.com/1/user/-/profile.json"

	request = urllib2.Request(url)
	request.add_header('Authorization', 'Bearer ' +  tokens.get('access_token'))
	response = urllib2.urlopen(request).read()
	print response

