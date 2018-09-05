#features: have a story, have inputs, replace blanks with inputs
#ex: Once upon a time, there was an __________ (reptile).

# THIS CAN BE USED LATER...
# def begins_with_vowel(word):
#     if word.lower()[0] == 'a' or word.lower()[0] == 'e' or word.lower()[0] == 'i' or word.lower()[0] == 'o' or word.lower()[0] == "u":
#         return True
#     else:
#         return False

def mad_libs():
    
    print("Welcome to the game of Mad Libs! Where you will build your vocabulary and be entertained for hours!")

    #a list of nouns, verbs, adjectives used in the GAME OF MADLIBS!

    reptile = input("REPTILE: ")
    adjective = input("ADJECTIVE: ")
    number = input("NUMBER: ")
    noun = input("PLURAL NOUN: ")
    adverb = input("ADVERB: ")

    #REFACTORED INTO A FUNCTION CALLED begins_with_vowel
    # if reptile.lower()[0] == 'a' or reptile.lower()[0] == 'e' or reptile.lower()[0] == 'i' or reptile.lower()[0] == 'o' or reptile.lower()[0] == "u":
    #     print("Once upon a time, there was an %s" % (reptile))
    # else:
    #     print("Once upon a time, there was a %s" % (reptile))

    # if begins_with_vowel(reptile):

    print("Once upon a time, there was a(n) %s. It was a very %s %s. It had %s %s. It lived %s ever after." %(reptile, adjective, reptile, str(number), noun, adverb))

    # else:
    #     print("Once upon a time, there was a %s." %(reptile))

def test():
    mad_libs()

test()

#python modules
#system modules
#was the input a noun?
