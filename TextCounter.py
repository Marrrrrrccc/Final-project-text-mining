import docx2txt
import re

filename = str(input("Enter file name"))
def counter(extension):

    if extension.__contains__('.docx') or extension.__contains__('.doc'):
        # open connection to Word Document
        doc = docx2txt.process(filename)
        words = {}
        remove =" ".join(re.findall(r"[a-zA-Z0-9]+", doc)).lower()
        for remove in remove.split():
            words[remove] = words.get(remove, 0) + 1  # dict kasi para makuha yung key example (2:"the") means two time lumabas yung the

            for w, c in words.items():
                print("%s: %d times" % (w, c))

    elif extension.__contains__(".txt"):

        file = open(filename, "r")
        words = {}

        for line in file:
            remove = " ".join(re.findall(r"[a-zA-Z0-9]+", line)).lower()
            for b in remove.split():  # transform file to dict
                words[b] = words.get(b,0) + 1  # dict kasi para makuha yung key example (2:"the") means two time lumabas yung the

            for w, c in words.items():
                print("%s: %d times" % (w, c))


counter(filename)