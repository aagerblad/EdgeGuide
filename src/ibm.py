import json
import requests
from requests.auth import HTTPBasicAuth

def post_activity(params):
    activity = {
        "actor": {
            "id": "dennis"
        },
        "verb": "post",
        "title": "<title>",
        "content":"<content>",
        # "updated": "2012-01-01T12:00:00.000Z",
        # "object": {
        #     "summary": "First Entry details",
        #     "objectType": "note",
        #     "id": "objectid",
        #     "displayName": "First entry",
        #     "url": "http://myurl.com/myid"
        # }
    }

    for k, v in params.iteritems()  :
        activity[k] = v

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    # r = requests.post(
    #     'http://apps.ce.collabserv.com/connections/opensocial/rest/activitystreams/@me/@all', 
    #     data=json.dumps(activity),
    #     auth=HTTPBasicAuth('puaberg@yahoo.se', 'edge.guide'),
    #     headers=headers
    # )

    r = requests.post(
        'http://192.168.43.139:8888', 
        data=json.dumps(activity),
        auth=HTTPBasicAuth('puaberg@yahoo.se', 'edge.guide'),
        headers=headers
    )

    return r



