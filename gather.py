import os
import json
import datetime as dt
import twitter
from twitter import OAuth

t = twitter.api.Twitter(
    auth=OAuth(
        os.environ['TWITTER_API_ACCESS_TOKEN'], 
        os.environ['TWITTER_API_ACCESS_SECRET_TOKEN'], 
        os.environ['TWITTER_API_KEY'], 
        os.environ['TWITTER_API_SECRET_KEY']),
    retry=True)

hashtags = ['leadership', 'leadershipdevelopment', 'leadershipskills', 'juniorleadership', 'leadershippodcast', 'hr', 'womeninleadership', 'theleadershipgap', 'servantleadership', 'gls18', 'unconciousbias']

for tag in hashtags:
    f = open(str(dt.datetime.now().date())+'_popular_'+tag+'.json', 'w')
    f.write(json.dumps(t.search.tweets(q="#"+tag, result_type="popular", count=100, lang='en')))
    f.close()

##This worked well for leadership - but the other hashtags didn't have enough results - so switched to popular##
# dates = []
# for tag in hashtags:
#     for x in range(0,7):
#         dates.append(str((dt.datetime.now() - dt.timedelta(days=x)).date()))
#     dates.reverse() #start with oldest dates
#     tweetDictionaries = []
#     for index, d in enumerate(dates):
#         print('getting data for '+ d+'_'+tag+'.json')
#         print(index)
#         if(index == 0):
#             tweetDictionaries.append(t.search.tweets(q="#"+tag, result_type="mixed recent", count=100, lang='en', until=d))
#         else:
#             print(tweetDictionaries[index-1]['search_metadata']['max_id'])
#             tweetDictionaries.append(t.search.tweets(q="#"+tag, result_type="mixed recent", count=100, lang='en', until=d, since_id=tweetDictionaries[index-1]['search_metadata']['max_id']))
#         f = open(d+'_'+tag+'.json', 'w')
#         f.write(json.dumps(tweetDictionaries[index]))
#         f.close()