```
import requests

def get_token(auth_url, client_id, scope, client_secret, grant_type='client_credentials'):
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'client_id': client_id,
        'scope': scope,
        'client_secret': client_secret,
        'grant_type': grant_type
    }
    
    r = requests.post(url=auth_url, data=data, headers=headers)
    return r.json(), r.status_code

# 配置信息
auth_url = 'https://login.microsoftonline.com/e0fd434d-ba64-497b-90d2-859c472e1a92/oauth2/v2.0/token'
client_id = 'your_client_id_here'
client_secret = 'your_client_secret_here'
scope = 'https://azsvc-<subscription_name>-stitt-app.hsbc.com/.default'
api_url = 'https://<project_name>-nonprod-<region_code>-stitt-01.azurewebsites.net'

# 获取访问令牌
token_response, status_code = get_token(auth_url, client_id, scope, client_secret)

if status_code == 200:
    access_token = token_response['access_token']
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    # 准备OpenAI GPT-4 Turbo API请求的数据
    data = {
        "model": "gpt-4-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What are the latest advancements in AI?"}
        ],
        "max_tokens": 100
    }
    
    # 发送请求到OpenAI模型API
    response = requests.post(api_url + '/v1/chat/completions', headers=headers, json=data)
    
    if response.status_code == 200:
        print("API Response:", response.json())
    else:
        print(f"API call failed with status code {response.status_code}: {response.text}")
else:
    print(f"Failed to obtain token, status code {status_code}: {token_response}")

```
