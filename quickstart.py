""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import time


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!
session = InstaPy(username="lovely_lune3", password="Rhrntkd12#")

# with smart_run(session):
#     # general settings
#     session.set_dont_include(["friend1", "friend2", "friend3"])

#     # activity
#     session.set_user_interact(amount=3, randomize=True, percentage=100, media='Photo')
#     session.like_by_tags(['맞팔환영', '맞팔'], amount=10, interact=True)    
#     session.follow_by_tags(['맞팔환영', '맞팔'], amount=10)



with smart_run(session):
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=200000,
                                    max_following=200000,
                                    min_followers=30,
                                    min_following=30)
    session.set_user_interact(amount=1, randomize=True, percentage=70,
                              media='Photo')
    session.set_do_like(enabled=True, percentage=80)
    session.set_do_comment(enabled=True, percentage=3)
    session.set_comments(
        ['Nice shot! @{}', 'I love your profile! @{}', '@{} Love it!',
        '@{} :heart::heart:',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
         '@{}:revolving_hearts::revolving_hearts:', '@{}:fire::fire::fire:'],
        media='Photo')

    # unfollow activity
    # session.unfollow_users(amount=126, nonFollowers=True, style="RANDOM",
    #                        unfollow_after=42 * 60 * 60, sleep_delay=300)

    # follow activity
    ammount_number = 500
    # session.follow_user_followers(['chrisburkard', 'danielkordan'],
    #                               amount=ammount_number, randomize=False,
    #                               interact=True, sleep_delay=240)
    
    time.sleep(3)
    session.follow_by_tags(['맞팔환영'], interact= True, amount=1, randomize=False)
    """ Joining Engagement Pods...
    """
    # session.join_pods(topic='entertainment', engagement_mode='no_comments')
