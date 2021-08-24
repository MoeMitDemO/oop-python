import praw, requests, re, time

reddit = praw.Reddit('bot1')





#posts = subreddit.search(query="reeves", sort='new', syntax='lucene', time_filter='all')
posts = reddit.subreddit("aww").search(query='kitty', time_filter='all', limit=100, params={'include_over_18': 'on'})

allPosts = ''
postCount = 1

for post in posts:
    # print("Title: ", post.title)
    # print("Text: ", post.selftext)
    # print("Score: ", post.score)
    url = (post.url)
    file_name = url.split("/")
    print(file_name)
    if len(file_name) == 0:
         file_name = re.findall("/(.*?)", url)
    file_name = file_name[-1]
    if "." not in file_name:
        continue
    print(file_name)
    r = requests.get(url)

    with open('./pics/' + file_name,"wb") as f:
        f.write(r.content)
    # print("---------------------------------\n")
    # if post.over_18:

    allPosts+= str(postCount) + ' ' + post.title+'\n'+post.url+'\n\n'
    postCount += 1

    # time.sleep(2)
with open('result', 'w', encoding='utf-8') as f:
    f.write(str(postCount) + " Inhalte gefunden\n\n" + allPosts)
print(str(postCount) + " Inhalte gefunden\n\n" + allPosts)

# PyFuBot
# web app
# T-VYrrTnA_WsLqG6Hb14kA
# change icon
# secret	yvDtgIu4MONMZOJevl63EKJEToz3FQ
# name	
# PyFuBot
# description	
# about url	
# redirect uri	
# http://127.0.0.1
# update app
# developers	
# MoeWithTheO (that's you!) remove

# add developer:

