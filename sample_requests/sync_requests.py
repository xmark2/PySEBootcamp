import requests
import json


def get_and_parse_user(base_url: str, endpoint_prefix: str, user_id: int):
    url = base_url + endpoint_prefix + str(user_id)
    response = requests.get(url)
    post_response = requests.post(url)
    return post_response.json()

#
# response = requests.get("http://127.0.0.1:8000/user/0", headers={})
# print("status_code:", response.status_code)
# response_headers = response.headers
# print("headers:", response.headers)
# print("rate limit info:", response_headers['x-app-rate-limit'])
# response_data = response.json()
# print("return data:", response_data)
# print("short_description:", response_data['short_description'])
#
# sample_data_to_send = {
#   "name": "bob",
#   "liked_posts": [
#     0, 1, 2
#   ],
#   "short_description": "some short description",
#   "long_bio": "some long bio"
# }
# json_data = json.dumps(sample_data_to_send)
# # print("json_data", json_data, type(json_data))
# # print("original data", sample_data_to_send, type(sample_data_to_send))
# post_response = requests.post("http://127.0.0.1:8000/user/", headers={}, json=sample_data_to_send)
