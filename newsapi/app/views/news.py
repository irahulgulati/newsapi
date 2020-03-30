from newsapi import NewsApiClient as news
from dotenv import load_dotenv
import os
#load the env library to load the environement variable api key
load_dotenv()

newsapi = news(api_key='78e38455f729433993998925f7104f5f')
class getnews_:
    def headlines(self,query):
        self.headlines = newsapi.get_top_headlines(q=query,
                                            language='en',
                                            

                                            )
        return self.headlines
    def all(self,query):
        self.articles    =   newsapi.get_everything(q=query,
                                                language='en',
                                                sort_by='relevancy',
                                                )
        return self.articles