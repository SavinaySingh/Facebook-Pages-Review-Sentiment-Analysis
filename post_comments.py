import json
import facebook
import ast
from textblob import TextBlob
if __name__=='__main__':
    # token=os.environ.get('FACEBOOK_TEMP_TOKEN')
    # token='EAAGfzQMI8twBANZC7ymoYfGNscWWSpNygPVv7f3HTcjtSCisNhhCC9tdhqperhq7G8tY4MMLaB4Lzqkhwn2NhdI3dUnoMTZCfFNNmPxbNnINQcpCYOGBqFGb92sza9eLZB8IQaYbZCspdJuiRjxEHwHPLNrJnm9WZCZA5RBSozBwZDZD'
    token='EAACEdEose0cBAAH1PZBQhbi47gohAbNK4KFAfeRNMH9ISSeT4BwzaaRLUDZC2kUITk8RvwTptAv7rIqsJs9yeovKDnTYmiIq5UZAzGFW8LX6tlHLvK7nGAC6FAkYCuyri0myOi0rbJMs32oEgauFOqKmuQmQR1vKJE8IgL3H8Dts2l6Q4lHfG25OdK485G3fTvkHvZCLswZDZD'
    graph=facebook.GraphAPI(token)
    profile=graph.get_object('131919650173343',fields='name,posts{comments.limit(200)}')
    print(json.dumps(profile,indent=4))


