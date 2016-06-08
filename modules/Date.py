# -*- coding: utf-8-*-
import datetime
import re
from client.app_utils import getTimezone
from semantic.dates import DateService

WORDS = ["DAY"]


def handle(text, mic, profile):
    """
        Reports the current date based on the user's timezone.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
               number)
    """

    tz = getTimezone(profile)
    now = datetime.datetime.now(tz=tz)
#    service = DateService()
#    response = service.convertTime(now)
    day = now.day
    month = now.month
    year = now.year
    
    if month == 1:
        smonth = "January"

    elif month == 2:
        smonth = "February"

    elif month == 3:
        smonth = "March"

    elif month == 4:
        smonth = "April"

    elif month == 5:
        smonth = "May"

    elif month == 6:
        smonth = "June"

    elif month == 7:
        smonth = "July"

    elif month == 8:
        smonth = "August"

    elif month == 9:
        smonth = "September"

    elif month == 10:
        smonth = "October"

    elif month == 11:
        smonth = "November"

    elif month == 12:
        smonth = "December"
    
    else:
        smonth = "e"


    mic.say("Today is %s of %s of %s ." % (day, smonth, year) )


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bday\b', text, re.IGNORECASE))
