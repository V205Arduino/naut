
'''
Fills data/urls.json with some example URLs for when I accidentally delete it.

'''

import json



URLs = [
    {
        "type":"URL",
        "data": "https://example.com",
        "title": "https://example.com",
        "timestamp": 1234590,
    },
    {
        "type":"URL",
        "data": "https://purplebubble.org",
        "title": "https://purplebubble.org",
        "timestamp": 1234567,
    },
    {
        "type":"URL",
        "data": "https://kieranklukas.com",
        "title": "https://kieranklukas.com",
        "timestamp": 1234560,
    },
    
]

#["https://example.com", "https://example.org", "https://purplebubble.org", "https://kieranklukas.com","https://stackoverflow.com","https://hardfork.ngo"]



# Save the list as JSON in a file called data.json
with open("data/urls.json", "w") as f:
    json.dump(URLs, f)
