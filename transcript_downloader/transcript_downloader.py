#https://oauth.groupme.com/oauth/authorize?client_id=CLIENT_ID

#access token: 	284988d0a1120131fd7746de321d195f

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import requests
import time
import json
from urllib import URLopener, urlretrieve

def onRequestError(request):
    print(request.status_code)
    print(request.headers)
    print(request.text)
    sys.exit(2)

def main():
    """groupme_image_downloader.py group_id access_token save_transcript(yes or no)
    
Creates a folder called "group_id_images" and downloads all images in the given group's gallery to that folder.

If a folder by that name already exists, this will update the folder with any new images added to the gallery since the previous download.
    """

    if len(sys.argv) != 3:
        print(main.__doc__)
        sys.exit(1)
    
    group_id = sys.argv[1]
    access_token = sys.argv[2]
    sys.argv[3]
    url = 'https://api.groupme.com/v3/groups?token=' + access_token
    
    r = requests.get(url, params=params, headers=headers)
    response = r.json()
    messages = response[u'response'][u'messages']
    
    image = urllib.URLopener()
    image.retrieve("")

