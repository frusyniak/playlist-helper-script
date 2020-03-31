"""
If this actually took three strings, this would be a working standalone
module sort of:

    1. path to csv
    2. string for song header row
    3. string for artist header row


Checklist for making this a django-integratable module

    * requests are not going to happen here. Instead, this module needs
        to be written such that it recieves response data that has
        already been returned, and just parses it.

    * the api currently doesn't work, but we have cached api responses
        that we can test with. However, if we are going to use a
        different api anyway, we should probably just refactor the
        module to take outside api requests right away.

    * ultimately, remove pyinputplus and dependencies from
        requirements.txt
"""

