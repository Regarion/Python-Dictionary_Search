# USAGE Example
# python3 word_search.py --string Car --path /home/kitetsu/sample.txt

import argparse
from nltk.corpus import wordnet  # Import wordnet from the NLTK

#required objects
line_number = 0
found = 0

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--string", type=str, required=True, help="Enter the Word to search")
ap.add_argument("-p", "--path", type=str, required=False, help="path to the text file")
args = vars(ap.parse_args())

# load the string, check for the meaning
word = args["string"]
syn = list()
meaning = wordnet.synsets(word)
print("Meaning of the word {} is: {}".format(word, meaning[0].definition()))

# Checking for Lower and Upper case
if word != word.lower():
    syn.append(word.lower())
else:
    syn.append(word)

#if the string is digit no Synonyms
if word.isdigit() == False:
    for synonym in wordnet.synsets(word):
        for lemma in synonym.lemmas():
            if lemma.name() != word and (lemma.name() != word.lower()):
                syn.append(lemma.name())  # add the synonyms
    print('Synonyms: ' + str(syn))

    for i in range(0, len(syn)):
        syn.append(syn[i].upper())
        syn.append(syn[i].capitalize())

#checking if path is provided for search function
if(args["path"]):
    file = open(args["path"], 'r')
    for line in file:
        #print("Line number is {}".format(line_number))
        line_number += 1
        for i in range(0, len(syn)):
            #print(syn[i])
            if syn[i] in line:
                found = 1
                print('{} is Found In Line {}'.format(syn[i], line_number))

    #text is not found
    if found == 0:
        print("{} does not exit in the text file".format(word))

    # closing text file
    file.close()
