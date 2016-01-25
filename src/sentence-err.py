#
# sentence-err.py
#
# Defines the entry point for the application
# Created by Brynden "Gigabyte Giant" Bielefeld on 01/25/2015
#
import re     # Regular Expression Library
import sys    # System Library
import random # Random Number Generator Library

def getLineList(file):
    retData = []

    for ln in open(file, "r"):
        if ln != "":
            retData.append(ln)

    return retData

def pickRandom(data):
    return data[random.randrange(len(data))]

def pickNRandom(n, data):
    retData = []
    i = 0

    while i < n:
        retData.append(pickRandom(data))
        i += 1

    return retData

def generateSentence(data, template):
    sentence = template

    # Step A: Pick some nouns
    randNouns = pickNRandom(len(re.findall("\<noun\>", template)), data["nouns"])

    # Step B: Pick some verbs
    randVerbs = pickNRandom(len(re.findall("\<verb\>", template)), data["verbs"])

    # Step C: Pick some adjectives
    randAdject = pickNRandom(len(re.findall("\<adjective\>", template)), data["adjectives"])

    # Step D: Pick some adverbs
    randAdverb = pickNRandom(len(re.findall("\<adverb\>", template)), data["adverbs"])

    # Step E: Pick some prepositions
    randPreps = pickNRandom(len(re.findall("\<prepositions\>", template)), data["prepositions"])

    # Step F: Generate a sentence
    ## TODO (Gigabyte Giant): ...

def main(argc, argv):
    if argc < 2:
        print("ERROR: Not enough command-line arguments!")

        return 1
    else:
        # Step 0: Get data from data directory
        DATA_DIR_PATH = argv[1]

        # TODO (Gigabyte Giant): Get rid of this horrid stuff
        DATA_PATHS = {
            "templates"   : DATA_DIR_PATH + "/templates.txt",
            "nouns"       : DATA_DIR_PATH + "/nouns.txt",
            "verbs"       : DATA_DIR_PATH + "/verbs.txt",
            "adjectives"  : DATA_DIR_PATH + "/adjectives.txt",
            "adverbs"     : DATA_DIR_PATH + "/adverbs.txt",
            "prepositions": DATA_DIR_PATH + "/prepositions.txt"
        }

        # TODO (Gigabyte Giant): Stop relying on the above dict
        DATA = {
            "templates"   : getLineList(DATA_PATHS["templates"]),
            "nouns"       : getLineList(DATA_PATHS["nouns"]),
            "verbs"       : getLineList(DATA_PATHS["verbs"]),
            "adjectives"  : getLineList(DATA_PATHS["adjectives"]),
            "adverbs"     : getLineList(DATA_PATHS["adverbs"]),
            "prepositions": getLineList(DATA_PATHS["prepositions"])
        }

        # Step 1: Pick a random sentence template
        sentenceTemplate = pickRandom(DATA["templates"])

        # Step 2: Generate a sentence
        finalSentence = generateSentence(DATA, sentenceTemplate)

        # Step 3: Print the generated sentence out
        print(finalSentence)

    return 0

main(len(sys.argv), sys.argv)
