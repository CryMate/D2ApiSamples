from requests_oauthlib import OAuth2Session
import os
import pickle
import json

API_KEY       = "1a2b3c4d5e6f7g8h9i10" # API key
CLIENT_ID     = "12345" # OAuth client_id
CLIENT_SECRET = "ABC1def2GHI3jkl4MNO5pqr6STU7vwx8YZ9" # OAuth client_secret
TOKEN_PATH    = "token_file"
REDIRECT_URL  = "https://github.com/CryMate"
AUTH_URL      = "https://www.bungie.net/en/OAuth/Authorize"
TOKEN_URL     = "https://www.bungie.net/platform/app/oauth/token/"
API_ROOT_PATH = "https://www.bungie.net/Platform"

def ProcessToken():
    # If you already have token, use that token.
    if os.path.isfile(TOKEN_PATH):
        with open(TOKEN_PATH, 'rb') as f:
            return pickle.load(f)

    session = OAuth2Session(client_id=CLIENT_ID, redirect_uri=REDIRECT_URL)
    authLink = session.authorization_url(AUTH_URL)
    print(f"Authorization link: {authLink[0]}")

    redirectResponse = input(f"Paste url link here: ")

    token = session.fetch_token(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        token_url = TOKEN_URL,
        authorization_response = redirectResponse
    )

    if not os.path.isfile(TOKEN_PATH):
        SaveToken(token)

    return token

def SaveToken(token):
    with open(TOKEN_PATH, 'wb') as f:
        pickle.dump(token, f, protocol=5)
        print('===== token saved =====')

def fetchResourceServer(token):
    session = OAuth2Session(
        client_id = CLIENT_ID,
        redirect_uri = REDIRECT_URL,
        token = token,
        # Use refresh token if access token was expired
        auto_refresh_url = TOKEN_URL,
        auto_refresh_kwargs = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
        token_updater=SaveToken,
    )
    return session

def main():
    token = ProcessToken()

    session = fetchResourceServer(token)

    # User.GetCurrentBungieNetUser
    # destinydevs: http://destinydevs.github.io/BungieNetPlatform/docs/services/User/User-GetCurrentBungieNetUser
    requestHeaders = {'X-API-Key': API_KEY }
    requestEndpoint = "/User/GetCurrentBungieNetUser/"
    response = session.get(url = API_ROOT_PATH + requestEndpoint, headers = requestHeaders)
    print("\n")
    print('endpoint:%s' % requestEndpoint)
    print(json.dumps(response.json(), indent=2))
    bungieId = (response.json())['Response']['uniqueName']
    print(bungieId)
    print('---')

if __name__ == '__main__':
    main()
