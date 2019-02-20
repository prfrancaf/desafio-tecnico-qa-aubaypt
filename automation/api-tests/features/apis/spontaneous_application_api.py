from json import dumps
from requests import post

def post_spontaneous_candidate(base_url, spontaneous_candidate_form):
    url = base_url + "Home/PostSpontaneousCandidateApi"
    headers = {"Content-Type": "application/json"}
    response = post(url, data=dumps(spontaneous_candidate_form), headers=headers)
    return response
