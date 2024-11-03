import requests
import requests

# REPLACE the following variables with your Client ID and Client Secret
CLIENT_ID = "3671e9ffa9b7c3923efc"
CLIENT_SECRET = "997cf9ba04ce988bc3bd58b6d21e3cd7bb5de4e6"

# REPLACE the following variable with what you added in the
# "Authorization callback URL" field
REDIRECT_URI = "http://www.iscale.cc"

def create_oauth_link():
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "user",
        "response_type": "code",
    }
    endpoint = "https://github.com/login/oauth/authorize"
    response = requests.get(endpoint, params=params)
    url = response.url
    return url

def exchange_code_for_access_token(code=None):
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": code,
    }
    headers = {"Accept": "application/json"}
    endpoint = "https://github.com/login/oauth/access_token"
    response = requests.post(endpoint, params=params, headers=headers).json()
    return response["access_token"]

def print_user_info(access_token=None):
    print("This is starting of the function")
    headers = {"Authorization": f"token {access_token}"}
    endpoint = "https://api.github.com/user"
    response = requests.get(endpoint, headers=headers).json()
    print (response)
    name = response["name"]
    username = response["login"]
    # private_repos_count = response["total_private_repos"]
    print(
        f"{name} ({username}) | private repositories: "
    )

link = create_oauth_link()
print(f"Follow the link to start the authentication with GitHub: {link}")
code = input("GitHub code: ")
access_token = exchange_code_for_access_token(code)
print(f"Exchanged code {code} with access token: {access_token}")
print_user_info(access_token=access_token)