'''

import json
import requests
api="https://randomuser.me/api"

def callApi(api):
    res=requests.get(api)
    res_text=json.loads(res.text)
    # print(res_text)
    fname=res_text['results'][0]['name']['first']
    lname=res_text['results'][0]['name']['last']
    print(f'the first name is:{fname}')
    print(f'the first name is:{lname}')
    

if __name__ == "__main__":
    callApi(api)

'''