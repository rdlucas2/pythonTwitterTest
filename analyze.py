import os
import json
import twitter
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

for file in os.listdir("./"):
    if file.endswith(".json"):
        jsonFile = open(file)
        jsonString = jsonFile.read()
        tweetsJSON = json.loads(jsonString)
        tweets = twitter.api.TwitterDictResponse(tweetsJSON)

        generator = (item['text'] for item in tweets['statuses'])
        text = ''
        for i in generator:
            text+=re.sub(r"http\S+", "", i.replace("RT", ""))
        #print(text)

        hashtagList = (re.findall(r"#(\w+)", text))
        hashtags = ' '.join(hashtagList)
        #print(hashtags)

        seen, result = set(), []
        for item in hashtagList:
            if item.lower() not in seen:
                seen.add(item.lower())
                result.append(item)
        #print(result)

        # idsUsed = {}
        # for item in tweets['statuses']:
        #     if(item['id'] in idsUsed):
        #         idsUsed[item['id']] += 1
        #     else:
        #         idsUsed[item['id']] = 1
        # print(idsUsed)

        timesUsed = {}
        for item in hashtagList:
            if item.lower() in timesUsed:
                timesUsed[item.lower()] += 1
            else:
                timesUsed[item.lower()] = 1

        print(timesUsed)

        # # Display the generated image:
        # # the matplotlib way:
        # # lower max_font_size
        # wordcloud = WordCloud(max_font_size=40).generate(text)
        # plt.imshow(wordcloud, interpolation="bilinear")
        # plt.axis("off")
        print(len(hashtags))
        if len(hashtags) >= 1:
            hashcloud = WordCloud(max_font_size=40).generate(hashtags)
            plt.figure()
            plt.imshow(hashcloud, interpolation="bilinear")
            plt.axis("off")

plt.show()