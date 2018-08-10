import os
from twitter import *

t = Twitter(
    auth=OAuth(
        os.environ['TWITTER_API_ACCESS_TOKEN'], 
        os.environ['TWITTER_API_ACCESS_SECRET_TOKEN'], 
        os.environ['TWITTER_API_KEY'], 
        os.environ['TWITTER_API_SECRET_KEY']))

# Get your "home" timeline
homeTimeline = t.statuses.home_timeline()

print(homeTimeline)