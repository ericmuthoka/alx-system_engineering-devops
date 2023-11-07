#!/usr/bin/python3
"""Retrieve Reddit subreddit subscriber count."""
import requests


def get_subreddit_subscribers(subreddit):
    """Get subscriber count for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        return 0
    except Exception:
        return 0


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 script.py <subreddit>")
    else:
        subscribers = get_subreddit_subscribers(sys.argv[1])
        print(f"Subscribers: {subscribers}")
