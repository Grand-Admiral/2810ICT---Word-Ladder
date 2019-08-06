import re

def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t]) # return len(c) and then finding c A ZIP takes a iterable var it stops when the shortest iter is used.

#make touple give back a touple
# item is word on atm
# target is where i need to go
# will return a list of touples which compare the first letter value of the words side, seek [(s,s),(s,e),(s,e),(s,k)]
# if c == t return len(c)

def build(pattern, words, seen, list): #Build up words and give to list to compare
  #build the graph / network lists
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and # re.search searches for a pattern that matches the string
                    word not in list]


def find(word, words, seen, target, path):#word: 
  global maxMatch
  maxMatch = 0
  #build a list
  list = []
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list) #start of word + . + end of word #Builds a list of all the words neighbors 
  if len(list) == 0: # if dead end move on
    return False
  list = sorted([(same(w, target), w) for w in list], reverse = True)#same function in touple the touple is in a list that is sorted
  # returns the number of same letters of word and target
  #print(list)
  
  #loop put items in seen list
  for (match, item) in list: 
    if match >= len(target) - 1:# if the current word is close to target word
      if match == len(target) - 1: # target total number of the word or item
        path.append(item)# add item to path
      return True
    seen[item] = True

  # recursion to implement main function
  
  # keep searching depth wise until hit dead end then pop
  for (match, item) in list:
    if short == "y": #If the user chose to use shortest path
      #if item in 
      if match >= maxMatch: #If the new word has more matches than before:  
        path.append(item) #Append it to the list
        if find(item, words, seen, target, path):
          return True
        if match <= maxMatch:
          path.pop()#Searching for path
        maxMatch = match
      else:
        path.pop() #pop if it does not have sufficient matches

    if short == "n": #If user chose not to use shortest path
      path.append(item) #Append it to the list
      if find(item, words, seen, target, path):
        return True
      path.pop()#Searching for path
      maxMatch = match


    


#--------------------------------------

#create fail safes try except
while True: # Try to open file
  while True:
    try:
      fname = input("Enter dictionary name: ")
      file = open(fname)
      lines = file.readlines()
      break
    except:
      print("file does not exist")
      continue
    
  #Ask for words
  while True: 
    start = input("Enter start word: ").lower()
    words = []
    for line in lines: #Regenerate word list
      word = line.rstrip()
      if len(word) == len(start): #with words that are same length as Start word
        words.append(word) 
    target = input("Enter target word: ").lower()
    if (start == target): #if both inputs are same, error and loop
        print('Error. Start and target words cannot be the same. Try again.')
        continue
      
    if (len(target) != len(start)) or (len(target) == 0 or len(start)== 0): 
      print("Word lengths do not match")
      continue
    break

  #Ask for forbidden words
  forbiddenList = [] 
  while True:
    forbidInput = input("Enter any forbidden words, per line. Leave empty for none: ")
    if (start == forbidInput) or (forbidInput == target):
      print("Cannot equal the target or start word")
      continue
    elif (forbidInput != ""): #will always run until user inputs empty string
      forbiddenList.append(forbidInput)
    else:
      print("Forbidden words: "+str(forbiddenList)) #Show list of current forbidden words
      break
    
  #Remove forbidden words from list words 
  for s in forbiddenList: #For every forbidden word check every word in the dictionary...
    for d in words: 
      if (d == s): #and if it's the same as a forbidden word, remove it
        words.remove(s)

  #Ask if user wants shortest path
  while True:
    short = input("Do you want to show the shortest path? y/n: ").lower()
    if (short == "y") or (short == "n"):
      break
    else:
      print('Invalid input!')
      


  path = [start]
  seen = {start : True}

    #path searching wk 5
    #1. current searching vertex
    #2. queue (vertexes neighbors)
    #3. visited(set)
    # A = BC / b = A / C = DE
    #4. path(say path), start(where we begin), target(where to finish)

  #network of random words  
  if find(start, words, seen, target, path):
    path.append(target)
    print(len(path) - 1, path)
  else:
    print("No path found")

  print("Done.")
  another = input("Enter (y) to match another word, any other input to exit: ").lower() #Ask if user wishes to restart program
  if another == "y": 
    print('\n') #newline for neatness
    continue #continue main loop
  else:
    exit()
    break #break main loop

