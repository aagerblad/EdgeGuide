import ibm

r = ibm.post_activity(
    {
        "title": "Test apa title",
        "content":"this is content",
    }
)


import json
print json.dumps(json.loads(r.text), sort_keys=True, indent=4, separators=(',', ': '))

