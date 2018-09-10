#!/usr/local/bin/python3

from textblob import TextBlob
import random

#The point of this is to replace all the nouns in a 'support' article by the nouns in a 'tonal' article to create a mashup of articles

#<----------- THIS IS TRAWLS THE NEWSPAPERS IN NEWSPAPERS.JSON FOR ARTICLES --------------------->
# import json
#
# LIMIT = 1
#
# data = {}
# data['newspapers'] = {}
#
# with open('NewsPapers.json') as data_file:
#     newspaper = json.load(data_file)
#
# print("Building site for ", newspaper)
# paper = newspaper.build(value['link'], memoize_articles = False)
# newsPaper = {
#     "link": value['link'],
#     "articles": []
# }
# noneTypeCount = 0
# for content in paper.articles:
#     if count > LIMIT:
#         break
#     try:
#         content.download()
#         content.parse()
#     except Exception as e:
#         print(e)
#         print("continuing...")
#         continue
#     article = {}
#     article['title'] = content.title
#     article['text'] = content.text
#     article['link'] = content.url
#     print('articles downloaded from', newspaper, "using newspaper, url: ", content.url)


def text_from_news_article():
    #takes in an newspaper url
    #returns in the form of a string the first article of the text
    #CURRENTLY is hardcoded

    txt = """Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics concerned with the inter
    actions between computers and human (natural) languages."""

    return txt

#AND TAKES OUT ALL NOUNS

def take_nouns_from(article):
    #takes all the nouns of the parameter text
    #used to make all the 'tone' of the article
    #also used to take out all the nouns in the support article
    blob = TextBlob(article)
    article_tagged = blob.tags
    indices_of_nouns = []
    tagged_words = [x[1] for x in article_tagged]
    index = 0
    for tag in tagged_words:
        if "NN" == tag:
            indices_of_nouns += [index]
        index += 1
        tagged_words = tagged_words[index:]

    nouns = []
    words = [x[0] for x in article_tagged]


    for num in range(0, len(indices_of_nouns)):
        noun_index = indices_of_nouns[num]
        nouns += [words[noun_index]]

    return nouns

def nounify(support, tonal):
    #take nouns from tonal article to set the tone of the support article
    tonal_nouns = take_nouns_from(tonal)
    support_nouns = take_nouns_from(support)

    #replaces each noun in the support article with a noun from the tonal article

    new_support = support 

    for word in support.split():
        if word in support_nouns:
            random_word = random.choice(tonal_nouns)
            new_support = new_support.replace(word, random_word)

    print(new_support)
    return new_support

def mad_libs():

    print("Welcome to the game of mashup madlibs, where two articles will be mashed up for your delight and entertainment!")

    print("The tonal_text, or the nouns we will use to replace the nouns of the supporting article with, are ooing to be from the below:")

    tonal_text = "Sara was a unicorn. She was a very special unicorn, and her tribe considered her one of the greatest creatures in the world, for Sara had wings, and she could fly. Great big gossamer wings the color of moonlight, could take her soaring into the air above, her white body gleaming in the sun at day, and sparkling in the moon-and star-light at night. She was a happy and good-natured animal and made friends with everyone, even humans. She liked little children, who always stared at her in wonder and delight."

    print("tonal text : " + tonal_text)

    print("The support_text, or the article we will use as the base article will be as below: ")

    support_text = """Hurricane Florence poses an extreme threat to Southeast and Mid-Atlantic: Hurricane Florence is tracking toward the East Coast with invariability rarely seen in storms several days away from landfall. While forecasters were careful to cite “high uncertainty” and “low model confidence” last week, their tone changed after watching the storm’s eventual path barely shift from what they had considered to be the worst-case scenario. On Sunday evening, the National Hurricane Center was forecasting Florence to become a strong Category 4 just prior to making landfall somewhere on the Southeast or Mid-Atlantic coast on Thursday. With each passing flight into the eye of the storm and every new forecast from the global weather models, it is increasingly unlikely Florence will turn out to sea and spare the Eastern Seaboard from potentially devastating storm surge, flooding and wind. There’s even some indication the hurricane will slow or stall out over the Mid-Atlantic later this week, which could lead to a disastrous amount of rain."""

    print("support text : " + support_text)

    print("FINALLY! We shall NOUNIFY!!!")

    nounify(support_text, tonal_text)

def test():
    mad_libs()

test()
