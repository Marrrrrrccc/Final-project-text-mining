import docx2txt
import re

filename = str(input("Enter file name"))
def counter(extension):

    if extension.__contains__('.docx') or extension.__contains__('.doc'):
        # open connection to Word Document
        doc = docx2txt.process(filename)#extract docx to text
        words = {}
        remove =" ".join(re.findall(r"[a-zA-Z0-9]+", doc)).lower()# tanggal special character
        for remove in remove.split():#para kada space isang word
            words[remove] = words.get(remove, 0) + 1  # transform file to dict # dict kasi para makuha yung key example (2:"the") means two time lumabas yung the

            for w, c in words.items():#print lang pero di to gagawin graph dapat
                print("%s: %d times" % (w, c))

    elif extension.__contains__(".txt"):

        file = open(filename, "r")
        words = {}

        for line in file:#para kada space isang word
            remove = " ".join(re.findall(r"[a-zA-Z0-9]+", line)).lower()# tanggal special character
            for b in remove.split():
                words[b] = words.get(b,0) + 1 # transform file to dict  # dict kasi para makuha yung key example (2:"the") means two time lumabas yung the

            for w, c in words.items():#print lang pero di to gagawin graph dapat
                print("%s: %d times" % (w, c))


counter(filename)