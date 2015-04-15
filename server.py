#import Highton
from highton import Highton
from datetime import datetime, date
import time

#initialize it
high = Highton(
    api_key = 'f4075d9e048c00bda63ec55794d02831',
    user = 'puaberg@froxy'
)

people = high.get_people()
#iterate over all people
for person in people:
#choose one of the attributes from below
    print(person.first_name)

# deals = high.get_deals_since('20150415133000')

# for deal in deals:
#     print(deal.name)

lastchecked = datetime.now()


while True:
	s = lastchecked.strftime("%Y%m%d%H%M%S")
	lastchecked = datetime.now()
	deals = high.get_deals_since(s)
	if deals != False:
		for deal in deals:
			print(deal.name)
	else:
		print("Inget nytt")

	time.sleep(5)
	pass