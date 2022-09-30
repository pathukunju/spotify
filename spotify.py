from flask import Flask,render_template, request
import requests

app = Flask("spotify")

@app.route('/',methods= ['GET','POST'])
def index():
    if request.method == 'POST':
        data = request.form.get('spot')
        print(data)
        option = request.form.get('option')
        

        token ='BQAzCH3SbDNwlj-aXhOCu7LiqkUPbz4XFUl6F6_On4Z0Q-FDpoYQ19Z3jRQN3BlQDqsPL862w_kzjLkl91lOL3pbTp104WayBGh2jlYwioectA7AxQtZrwZ0_Cf-TB8uVRwu0riglXzsQDne29aPBcbHUAZS0ATSYKmLSH2U3UgMFShxhGXClu-uzWOACeNfs3WIvGS2S5LR46H1Fas'
        user_headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        user_params = {
            "limit": 50
        }
        user_profile_response = requests.get(f"https://api.spotify.com/v1/me",params=user_params, headers=user_headers)
        user_dict = user_profile_response.json()
        
        

        user_tracks_response = requests.get(f"https://api.spotify.com/v1/search?q={data}&type={option}", params=user_params, headers=user_headers)
        


        # print(user_tracks_response.json())
        api_response = user_tracks_response.json()
        account= user_dict['display_name']
        profile_pic = user_dict['images'][0]['url']
        print(api_response)

        print(user_dict)

        return render_template('index.html',data = api_response, account = account,user_dict = user_dict, profile_pic = profile_pic,option = option)

    else:
        return render_template('index.html')

        

    

app.run()

