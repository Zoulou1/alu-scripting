#!/usr/bin/python3
"""DOCS"""
import requests

def top_ten(subreddit):
    """Docs"""
    reddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Fetch subreddit data with redirects disabled
    response = requests.get(reddit_url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        for post in data[:10]:
            print(post['data'].get('title'))
        return "OK"
    else:
        print(None)
        return None
