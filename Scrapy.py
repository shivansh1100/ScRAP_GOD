# import csv
# import sys
# import praw
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# from datetime import datetime
# from concurrent.futures import ThreadPoolExecutor, as_completed
# import os
# import Sentiment_Analysis as Sent
#
#
# # Reddit API credentials
# client_id = 'your_client_id'
# client_secret = 'your_client_secret'
# username = 'your_username'
# password = 'your_password'
#
# # Set up Reddit API connection
# reddit = praw.Reddit(
#     client_id='redd_it',
#     client_secret='shh',
#     user_agent='inputt',
#     username='name dalo',
#     password='*******')
#
# def search_subreddits(query):
#     # Searching subreddits based on the input query
#     subreddits = reddit.subreddits.search(query)
#
#     # Store results in a list
#     result_list = []
#     for subreddit in subreddits:
#         result_list.append(subreddit.display_name)
#
#     # Return the list of subreddits
#     return result_list
# def fetch_google_news(topic):
#     url = f"https://news.google.com/search?q={topic.replace(' ', '%20')}&hl=en-US&gl=US&ceid=US%3Aen"
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code != 200:
#         print(f"Failed to fetch news for topic: {topic}")
#         return
#
#     soup = BeautifulSoup(response.content, 'html.parser')
#     articles = soup.find_all('article', class_='IFHyqb DeXSAc')
#
#
#     news_data = []
#     for article in articles:
#         headline = article.find('a', class_='JtKRv')
#         if headline:
#             headline_text = headline.get_text()
#
#
#             time_element = article.find('time', class_='hvbAAd')
#             if time_element and time_element.has_attr('datetime'):
#                 timestamp = time_element['datetime']
#                 time_published = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
#                 formatted_time = time_published.strftime("%Y-%m-%d %H:%M:%S")
#             else:
#                 formatted_time = "Unknown"
#
#             news_data.append({
#                 'topic': topic,
#                 'headline': headline_text,
#                 'time': formatted_time
#             })
#
#     df = pd.DataFrame(news_data)
#     df = df.drop_duplicates(subset=['headline'])
#
#     print(df)
#
#     csv_file = '../sep_pro/nifty_50_companies_news.csv'
#     if os.path.isfile(csv_file):
#         df.to_csv(csv_file, mode='a', header=False, index=False)
#     else:
#         df.to_csv(csv_file, mode='w', header=True, index=False)
#
# def red_dat_scraper(subss):
#     subreddits = reddit.subreddits.search(subss)
#     with open('fix1.csv', 'w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['S_No','Subreddit', 'Post Title', 'Post Text',])  # Header row
#         c = 1
#         for c_name in subss:
#             sub = reddit.subreddit(c_name)
#             hot_posts = sub.hot(limit=5)  # Scrape hot posts
#             for post in hot_posts:
#                 S_No = c
#                 p_title = post.title
#                 p_text = post.selftext
#                 comments = []  # Initialize comments list
#                 # sc = []
#                 # Tag = []
#                 for comment in post.comments.list():  # Scrape comments
#                     if isinstance(comment, praw.models.MoreComments):  # Skip MoreComments objects
#                         continue
#                     comments.append(comment.body)
#
#                     # if 'Nvidia' in comment.body:
#                     #     comments.append(comment.body)
#                 print(comments)
#                 a = ', '.join(comments)[:1000]
#
#                 # sc.append(Sent.sentiment(a))
#                 # for ele in sc:
#                 #     if ele[0]['label'] == 'Neutral':
#                 #         Tag.append(0)
#                 #     if ele[0]['label'] == 'Positive':
#                 #         Tag.append(1)
#                 #     if ele[0]['label'] == 'Negative':
#                 #         Tag.append(-1)
#
#
#                 # for ele in sc:
#                 #     if ele.label == "Neutral":
#                 #         ele.pop()
#
#
#                 writer.writerow([c_name, p_title, p_text[:3]])
#
#
#
#
#
#
#
#
#
import csv
import sys
import praw

# Reddit API credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
username = 'your_username'
password = 'your_password'

# Set up Reddit API connection
reddit = praw.Reddit(
    client_id='b2QgqWP2eHyK6nKu99EoAA',
    client_secret='mq2a-gjuwahia1Ij6dvSiYALM9aSqg',
    user_agent='python:Virtual_Therapist:v1.0 (by /u/hecker1100)',
    username='hecker1100',
    password='amigo123@@@')

def search_subreddits(query):
    # Searching subreddits based on the input query
    subreddits = reddit.subreddits.search(query)

    # Store results in a list
    result_list = []
    for subreddit in subreddits:
        result_list.append(subreddit.display_name)

    # Return the list of subreddits
    return result_list

def red_dat_scraper(subss,pps,tlen,clen,tag,f1,f2):
    subreddits = reddit.subreddits.search(subss)


    # Open two CSV files, one for posts and one for comments
    with open(f1, 'w', newline='', encoding='utf-8') as post_csvfile, \
            open(f2, 'w', newline='', encoding='utf-8') as comment_csvfile:

        post_writer = csv.writer(post_csvfile)
        comment_writer = csv.writer(comment_csvfile)

        # Write headers for both CSVs
        post_writer.writerow(['S_No', 'Subreddit', 'Post Title', 'Post Text'])
        comment_writer.writerow(['S_No', 'Post Text', 'Comment'])

        s_no = 1  # Initialize serial number for each post

        for c_name in subss:
            sub = reddit.subreddit(c_name)
            if tag in sub.public_description:

                hot_posts = sub.hot(limit=pps)  # Scrape hot posts

                for post in hot_posts:
                    post_title = post.title
                    post_text = post.selftext

                    # Write post data to the 'posts.csv'
                    post_writer.writerow([s_no, c_name, post_title, post_text])

                    comments = []  # Initialize comments list

                    for comment in post.comments.list():  # Scrape comments
                        if isinstance(comment, praw.models.MoreComments):  # Skip 'MoreComments' objects
                            continue
                        comments.append(comment.body)

                    # Write comments data to the 'comments.csv'
                    for comment in comments:
                        comment_writer.writerow([s_no, post_text[:tlen], comment[:clen]])

                    s_no += 1  # Increment serial number for the next post


