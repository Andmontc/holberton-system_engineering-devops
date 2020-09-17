#!/usr/bin/python3
""" function that queries the Reddit API and returns
    the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ Return the subs """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-agent': 'URL'}
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        return 0
    subs = response.json().get('data')
    return subs.get('subscribers')
