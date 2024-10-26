#!/usr/bin/python3
import requests

def top_ten(subreddit):
    # Define the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    # Set the User-Agent to avoid blocking by Reddit's API
    headers = {'User-Agent': 'python:subreddit.hot.posts:v1.0 (by /u/yourusername)'}
    
    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the request was successful and there was no redirect
        if response.status_code == 200:
            data = response.json().get('data', {}).get('children', [])
            # Print the titles of the first 10 posts
            for post in data[:10]:
                print(post['data'].get('title'))
        else:
            # Print None if the subreddit is invalid or redirected
            print(None)
    except Exception as e:
        print(None)
