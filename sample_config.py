HEROKU = True # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["5445530721:AAFI2_zBd_zrhUS0_OHG6iYF9jIT9zn8SNc"]
    ARQ_API_KEY = environ["MXJLGJ-LZCAJQ-VAAAYT-BDDDZK-ARQ"]
    LANGUAGE = environ["id"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "5445530721:AAFI2_zBd_zrhUS0_OHG6iYF9jIT9zn8SNc"
    ARQ_API_KEY = "MXJLGJ-LZCAJQ-VAAAYT-BDDDZK-ARQ"
# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
    LANGUAGE = "id"

# Leave it as it is
ARQ_API_BASE_URL = "https://arq.hamker.in"
