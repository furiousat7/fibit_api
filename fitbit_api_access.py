import urllib2
import urllib
import base64
import fitbit_keys

tokens = fitbit_keys.tokens
client_codes = fitbit_keys.client_codes


oAuthUrl = 'https://api.fitbit.com/oauth2/token'

def checkIfTokenIsValid(url):
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
		import json
		json_output = json.loads(response)
		update_tokens(json_output)
		response = doApiCall(url)
		print response
	except urllib2.URLError as e:
		print e.code
		print e.read()

def update_tokens(json_output):
	tokens['access_token'] = json_output.get('access_token')
	tokens['refresh_token'] = json_output.get('refresh_token')
	fitbit_keys.tokens = tokens	


def doApiCall(url):
	request = urllib2.Request(url)
	request.add_header('Authorization', 'Bearer ' +  tokens.get('access_token'))
	response = urllib2.urlopen(request).read()			
	return response

if __name__ == '__main__':

	# checkIfTokenIsValid()
	url = "https://api.fitbit.com/1/user/-/profile.json"
	try:		
		doApiCall(url)		
	except urllib2.URLError as e:
		HTTPErrorMessage = e.read()
		if e.code -- 401 and 'Access token expired' in HTTPErrorMessage:
			checkIfTokenIsValid(url)


