import eventful
import unicodecsv as csv
import codecs
import random
api = eventful.API('mhRcqWrPnjbF86T2')
file_name = raw_input('Enter category you want to search:') + '.csv'
count=0
img=1

with open(file_name,'rb') as csvfile:
	with open('data1.csv','a+') as csvfile1:
		fieldnames = ['id', 'title', 'venue_name', 'number_of_likes', 'number_of_comments', 'key']
		datawriter = csv.DictWriter(csvfile1, fieldnames=fieldnames)
		data = csv.reader(csvfile)
		for row in data:
			key=''.join(row)
			i=0
       
			events = api.call('/events/search', q=key, l='San Diego')
			num_of_pages = int(events['page_count'])
			try: 
				for i in range(0, num_of_pages):
					events = api.call('/events/search', q=key, l='San Diego', page_number=i)
					for event in events['events']['event']:
						print "%s at %s of %s" % (event['title'], event['venue_name'],key)
						comm = random.randint(10, 50) 
						likes = random.randint(500, 1000) 
						count=count+1
						print count
    						datawriter.writerow({'id': event['id'], 'title': event['title'], 'venue_name': event['venue_name'], 'number_of_likes':likes, 'number_of_comments':comm, 'key': key})
			except:
				print 'excpetion'



