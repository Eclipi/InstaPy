""" Quickstart script for InstaPy usage """

# imports
import yaml
import os
import random
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import time


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!
session = InstaPy(username="lune_kks", password="rhrbtkd123")

# with smart_run(session):
#     # general settings
#     session.set_dont_include(["friend1", "friend2", "friend3"])

#     # activity
#     session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
#     session.like_by_tags(['맞팔환영', '맞팔'], amount=10, interact=True)    
#     session.follow_by_tags(['맞팔환영', '맞팔'], amount=10)



with smart_run(session):
    hashtags = ['맞팔', '팔로우늘리기', '여행', '맞팔환영', '선팔하면맞팔', '선팔맞팔', '팔로우반사', '좋반', '소통', '소통해요', '인친해요']
    random.shuffle(hashtags)
    my_hashtags = hashtags[:10]

    # general settings
    session.set_dont_like(['sad', 'rain', 'depression', '수익', '제테크', '마케팅', '보험', '판매'])
    session.set_do_follow(enabled=True, percentage=80, times=1)
    session.set_do_comment(enabled=True, percentage=80)
    session.set_comments([
                             u'소통하고 지내요~! :heart_eyes:',
                             u'팔로우 하고 갑니다~~! :heart_eyes: ',
                             u'소통해요 :)',
                             u'소통하고 지내요!! :)',
                             u'소통하고 지내요~! :wink:',
                             u'소통하고 지내요! :heart_eyes:',
                             u'소통해요!:wink:',
                             u'알고리즘에 이끌려서 팔로우하고 갑니다! :heart_eyes:'
                             ],
                         media='Photo')
    session.set_do_like(True, percentage=70)
    session.set_delimit_liking(enabled=True, max_likes=100, min_likes=0)
    session.set_delimit_commenting(enabled=True, max_comments=20, min_comments=0)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=7000,
                                    max_following=7000,
                                    min_followers=50,
                                    min_following=50)

    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "follows"],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_hourly=200,
                                 peak_likes_daily=585,
                                 peak_comments_hourly=80,
                                 peak_comments_daily=182,
                                 peak_follows_hourly=48,
                                 peak_follows_daily=None,
                                 peak_unfollows_hourly=35,
                                 peak_unfollows_daily=402,
                                 peak_server_calls_hourly=None,
                                 peak_server_calls_daily=4700)

    session.set_user_interact(amount=10, randomize=True, percentage=80)

    # activity
    session.like_by_tags(my_hashtags, amount=90, media=None)
    session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="nonfollowers",
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=501)
    session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="all",
                           style="FIFO", unfollow_after=24 * 60 * 60,
                           sleep_delay=501)

    """ Joining Engagement Pods...
    """
    session.join_pods(topic='sports', engagement_mode='no_comments')