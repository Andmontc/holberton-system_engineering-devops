#!/usr/bin/python3
""" Function that prints the titles of the first 10 hot posts
    listed for a given subreddit """
import requests


def top_ten(subreddit):
    """ return the top ten posts """
    url = "https://api.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    headers = {'User-agent': 'URL'}
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        print("None")
        return 0
    posts = response.json().get('data')
    for post in posts.get("children"):
        print (post.get('data').get('title'))
