from matplotlib import pyplot as plt

def countWords(file):
    x = []
    y = []
    words = {}
    i = 0
    for line in file:
        w = line.split(" ") #output list
        for b in line.split():
            words[b] = words.get(b, 0) + 1


        for w,c in words.items():
            plt.scatter(w,c)
    plt.show()












file = open("mytext.txt", "r")
print(countWords(file))


