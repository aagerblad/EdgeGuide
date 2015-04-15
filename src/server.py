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

    r = ibm.post_activity(payload)

    # TODO this is temp
    print 'Got request with status code:', r.status_code
    # import json
    # print json.dumps(json.loads(r.text), sort_keys=True, indent=4, separators=(',', ': '))


def post(title, content):
    print 'Trying to post with title:', title

    t = threading.Thread(
        target=threaded_post,
        args=({
            "title": title,
            "content": content
        }, )
    )
    t.daemon = True
    t.start()

def post_daily_task():
    # TODO get from highrise
    post('Daily tasks', '<none>')


def post_deal(deal):

    if deal.id in ALREADY_POSTED['deals'] and ALREADY_POSTED['deals'][deal.id] == deal.updated_at:
        return
    ALREADY_POSTED['deals'][deal.id] = deal.updated_at

    if deal.created_at != deal.updated_at:
        title = 'Updated deal: %s' % deal.name 
        content = '<updated deal content>'
    else:
        title = 'New deal created: %s' % deal.name
        content = '<nde deal content>'
    post(title, content)


def post_company(deal):
    if True:
        title = 'Company cond 1'
        content = '<company conent 1>'
    else:
        title = 'Company cond 2'
        content = '<company content 2>'
    post(title, content)

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

    print lastchecked'Getting deals since %s...')
    deals = high.get_deals_since(s)
    for deal in (deals or []):
        post_deal(deal)

    print 'Getting companies...'
    companies = high.get_companies_since(s)
    for company in (companies or []):
        post_company(company)

    time.sleep(2)

