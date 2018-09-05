#!/usr/local/bin/python3

from textblob import TextBlob
#Tentative Steps
#import noun dictionary

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


#AND TAKES OUT ALL NOUNS

txt = """Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics concerned with the inter
actions between computers and human (natural) languages."""

blob = TextBlob(txt)
print(blob.noun_phrases)

#REPLACES WITH RANDOM NOUNS FROM THE DICITONARY


# def mad_libs():
#     print("Welcome to the game of Mad Libs! Where you will build your vocabulary and be entertained for hours!")
#     reptile = input("REPTILE: ")
#     if reptile.lower()[0] == 'a' or reptile.lower()[0] == 'e' or reptile.lower()[0] == 'i' or reptile.lower()[0] == 'o' or reptile.lower()[0] == "u":
#         print("Once upon a time, there was an %s" % (reptile))
#     else:
#         print("Once upon a time, there was a %s" % (reptile))
#
# def test():
#     mad_libs()
#
# test()
