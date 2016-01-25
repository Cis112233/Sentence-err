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
            retData.append(ln.replace("\n", ""))

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
    numNouns = len(re.findall("\<noun\>", template))
    randNouns = pickNRandom(numNouns, data["nouns"])

    # Step B: Pick some verbs
    numVerbs  = len(re.findall("\<verb\>", template))
    randVerbs = pickNRandom(numVerbs, data["verbs"])

    # Step C: Pick some adjectives
    numAdject  = len(re.findall("\<adjective\>", template))
    randAdject = pickNRandom(numAdject, data["adjectives"])

    # Step D: Pick some adverbs
    numAdverb  = len(re.findall("\<adverb\>", template))
    randAdverb = pickNRandom(numAdverb, data["adverbs"])

    # Step E: Pick some prepositions
    numPreps  = len(re.findall("\<preposition\>", template))
    randPreps = pickNRandom(numPreps, data["prepositions"])

    # Step F: Generate a sentence
    ## Step F1: Replace nouns
    for i in range(0, numNouns):
        sentence = sentence.replace("<noun>", pickRandom(randNouns), 1)

    ## Step F2: Replace verbs
    for i in range(0, numVerbs):
        sentence = sentence.replace("<verb>", pickRandom(randVerbs), 1)

    ## Step F3: Replace adjectives
    for i in range(0, numAdject):
        sentence = sentence.replace("<adjective>", pickRandom(randAdject), 1)

    ## Step F4: Replace adverbs
    for i in range(0, numAdverb):
        sentence = sentence.replace("<adverb>", pickRandom(randAdverb), 1)

    ## Step F5: Replace prepositions
    for i in range(0, numPreps):
        sentence = sentence.replace("<preposition>", pickRandom(randPreps), 1)

    # Step G: Return the new sentence
    return sentence

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
