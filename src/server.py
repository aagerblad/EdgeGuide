import threading
import ibm
import schedule
from highton import Highton
from datetime import datetime, date, timedelta
import time

ALREADY_POSTED = {
    'deals': {},
    'companies': {}
}

def threaded_post(payload):
	pass
    # r = ibm.post_activity(payload)
    # print 'Got request with status code:', r.status_code

    # TODO this is temp
    # import json
    # print json.dumps(json.loads(r.text), sort_keys=True, indent=4, separators=(',', ': '))


def post(title, content, url):
    print 'Trying to post with title:', title

    t = threading.Thread(
        target=threaded_post,
        args=({
            "title": title,
            "content": content,
            "gif": url
        }, )
    )
    t.daemon = True
    t.start()

def post_daily_task():
    # TODO get from highrise
    post('Daily tasks', '<none>', '')


def post_deal(deal):

    if deal.highrise_id in ALREADY_POSTED['deals'] and ALREADY_POSTED['deals'][deal.highrise_id] == deal.updated_at:
        return
    ALREADY_POSTED['deals'][deal.highrise_id] = deal.updated_at

    if deal.created_at != deal.updated_at:
    	if deal.status == "won":
    		title = 'Won deal: %s' % deal.name 
        	content = deal.background
        	gif = 'http://i.giphy.com/YFIn0ICJFwGNa.gif'	
    	elif deal.status == "lost":
    		title = 'Lost deal: %s' % deal.name 
        	content = deal.background
        	gif = 'http://i.giphy.com/8boMf1VXVHoJy.gif'
        else:
        	title = 'Updated deal: %s' % deal.name 
        	content = deal.background
        	gif = ''
    else:
        title = 'New deal created: %s' % deal.name
        content = deal.background
        gif = ''
    post(title, content, gif)


def post_company(deal):
    if True:
        title = 'Company cond 1'
        content = '<company conent 1>'
        gif = ''
    else:
        title = 'Company cond 2'
        content = '<company content 2>'
        gif = ''
    post(title, content, gif)

# Initialize it
high = Highton(
    api_key = 'f4075d9e048c00bda63ec55794d02831',
    user = 'puaberg@froxy'
)

lastchecked = datetime.now()

# Schedule daily
schedule.every().day.at("10:30").do(post_daily_task)

while True:
    
    s = (lastchecked - timedelta(hours=2)).strftime("%Y%m%d%H%M%S")
    lastchecked = datetime.now()

    
    deals = high.get_deals_since(s)
    for deal in (deals or []):
        post_deal(deal)

    print 'Getting companies...'
    companies = high.get_companies_since(s)
    for company in (companies or []):
        post_company(company)

    time.sleep(2)

