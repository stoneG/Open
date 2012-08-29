"http://hellositong.tumblr.com/post/30372655913/write-like-lewis-carroll-literally"

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import random
namefile = '...alice.txt'

wordDict = {}

# wordDict will be populated with all the file's words as keys, and then
# a list of tuples (word that directly proceeds the key word, # of occurrences of that word) as values.
# For example, a prominent key from Alice's Adventures in Wonderland and the
# corresponding value might be something like this:
# wordDict['Alice'] --> [('went', 10), ('raced', 3), ... , ('was', 34)]
# which states that 'raced' directly followed 'Alice' three times in the text file.

def mimicDict(filename):
  """Builds wordDict, mapping each word (call it 'keyWord') from input text file
     to a list of mimicTuples in the form (mimicWord, # of times mimicWord follows keyWord)"""
  f = open(filename, 'rU')
  book = f.read()
  words = book.split()
  for i in range(0, len(words) - 1): # End before the last word
    keyWord = words[i]
    mimicWord = words[i+1]
    if keyWord in wordDict.keys(): # If keyWord is already a key
      mimicInDict = 0
      for mimicTuple in wordDict[keyWord]: # Check over all of keyWord's mimicTuple's
        if mimicWord in mimicTuple: # If mimicWord already exists in mimicTuple
          wordDict[keyWord] = wordPlusPlus(mimicWord, wordDict[keyWord])
          mimicInDict = 1
          break
      if mimicInDict == 0:
        wordDict[keyWord].append((mimicWord, 1))
    else: # If keyWord is not yet in keys
      wordDict[keyWord] = [(mimicWord, 1)]
  return 'DONE'

def wordPlusPlus(word, mimicList):
  """Given the mimicWord that we want to increment, reconstruct the mimicList
     with the mimicWord incremented by 1"""
  for i in range(0, len(mimicList)):
    if word in mimicList[i]:
      mimicList[i] = (mimicList[i][0], mimicList[i][1] + 1) # Incrementing occurrence of mimicWord
  return mimicList

def mimicRandomizer(mimicList):
  """Given list of mimicTuples, find the total number of mimic occurrences,
     generate a random number, empirically select a mimic tuple based on the random
     number, and finally: return the list ordering of the selected mimic tuple.
     For example, if the program selects the 6th tuple, it will return 5"""
  n = 0
  for mimicTuple in mimicList:
    n += mimicTuple[1] # n is the total number of mimicWord occurrences associated with keyWord
  mimicIntervals = [0]
  for i in range(0, len(mimicList)):
    mimicIntervals += [mimicList[i][1] + mimicIntervals[i]] # builds mimicWord occurrence intervals on [0,n)
  mimicChoice = int(random.random()*n) # mimicChoice is a random variable uniformly distributed [0,n)
  for j in range(0, len(mimicIntervals)):
    if mimicIntervals[j] <= mimicChoice and mimicChoice <= mimicIntervals[j + 1]:
      return j # Use mimicChoice to decide on which mimicWord to select, then return the mimicTuple's list order

def printMimic(mimic_dict, word, howLong):
  """Given mimic dict and starting word, print a certain number of words."""
  if howLong != 0:    
    elemLen = len(mimic_dict[word])
    nextWord = mimic_dict[word][mimicRandomizer(mimic_dict[word])][0]
    return word + ' ' + printMimic(mimic_dict, nextWord, howLong - 1)
  else: return ''

mimicDict(namefile)
print printMimic(wordDict, 'Alice', 200)
