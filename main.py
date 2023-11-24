
# imports
from instapy import InstaPy
from instapy import smart_run

from user import insta_username, insta_password

""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy import smart_run

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                    want_check_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings

    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_dont_like(["pizza", "#store"])

    # activity
    session.like_by_tags(["bananabread"], amount=10)
