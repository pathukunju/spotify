import requests
from urllib.parse import urlencode
import base64
import webbrowser


client_id = "363d6dedc92e40d08185ad520d13b399" 
client_secret = "26ae681e4e484353a2ca7722ac39b36c"


# auth_headers = {
#     "client_id": client_id,
#     "response_type": "code",
#     "redirect_uri": "http://localhost:7777/callback",
#     "scope": "user-library-read"
# }

# webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

code="AQCYo0Wjv6ePSpnLFg7FLd-UaYVocTaddig2z3I4S7YAj2JYE138uOxSoNmde0QCCuOOWBYU3KnZzmLxQQ8UjIoOf2aV5YFdVOXt_fgusmmoELc5L4ETcKuKQpoo3CPRDewFphZ8suIvrHc5O9jO9cRVtf6qoOjW_Cel1NgyhofC0jqMTZxSaWcaXRXjALFMExGEIJU"
encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

token_headers = {
    "Authorization": "Basic " + encoded_credentials,
    "Content-Type": "application/x-www-form-urlencoded"
}

token_data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": "http://localhost:7777/callback"
}

r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)

token = r.json()

print(token)

# token = 'BQCMfm9PvfaOdlelNbRmFw2oLz80K41xBYrdu6gca6L9B_zZ2R1zObYgG7Eb0R0KgGat6Eo3d_KMOpUwH3xIRQ8QJ2w8E-fDayLb8XbjbSeb6v5WmmoKTbT9_QPUG1dIhJzjk_17fA2QGa3ayMRyUIAXn92t7TfmTkxnSdSvnii6p6J4ALkxbmAeEe1EDSn-ZHC4SQoYMgMSrFu1nUQ'
# user_headers = {
#     "Authorization": "Bearer " + token,
#     "Content-Type": "application/json"
# }

# user_params = {
#     "limit": 50
# }

# user_tracks_response = requests.get("https://api.spotify.com/v1/me/tracks", params=user_params, headers=user_headers)

# print(user_tracks_response.json())