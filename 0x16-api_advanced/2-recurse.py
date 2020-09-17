#!/usr/bin/python3
""" Function that returns a list containing the titles
    of all hot articles for a given subreddit"""
from requests import request


def recurse(subreddit, hot_list=[], after=""):
    """ recursive function that returns all hot articles """
    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {'User-agent': 'URL'}
    response = request("GET", url, headers=headers).json()
    try:
        hotlist = response['data']['children']
        aft = response['data']['after']
        for item in hotlist:
            hot_list.append(item['data']['title'])
        if aft is None:
            return hot_list
        return recurse(subreddit, hot_list, aft)
    except Exception:
        return None
