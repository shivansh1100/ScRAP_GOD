
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
    client_id='cid',
    client_secret='shhh',
    user_agent='makeapi',
    username='uname',
    password='*****')

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


