import random

wordlist = ["python", "snake", "viper", "asp"]

#for each randomly selected index in wordlist, print the element which
#occurs at that index, then remove it from the list.

for choice in wordlist:
    choice = random.randrange((len(wordlist)))
    print(wordlist[choice])
    del wordlist[choice]
    #test to see if any elements remain in list
    print(wordlist)
