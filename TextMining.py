def countWords(file):
    words = {}
    i = 0
    for line in file:
        w = line.split(" ") #output list
        for b in line.split():
            words[b] = words.get(b,0) + 1


        for w,c in words.items():
            print("%s: %d times" % (w,c))









file = open("mytext.txt", "r")
countWords(file)


