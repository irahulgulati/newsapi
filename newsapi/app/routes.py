from app import application,jsonify
from .views import getnews_,thoughts

@application.route('/headlines/<string:query>', methods=['GET'])
def headlines_(query):
    #Get headlines
    getNews = getnews_()
    try:
        response    =   getNews.headlines(query)
    except:
        response    =   jsonify({'error':"Something's wrong"})
    return response

@application.route('/full/<string:query>',methods=['GET'])
def detailednews_(query):
    #get detailed news
    getDetailedNews = getnews_()
    try:
        response    =   getDetailedNews.all(query)
    except:
        response    =   jsonify({'title': "Something's wrong"})
    return response

@application.route('/thoughtoftheday',methods=['GET'])
def getthoughtoftheday_():
    bringThought =  thoughts()
    return bringThought.getThought()