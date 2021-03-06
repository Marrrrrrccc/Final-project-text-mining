import docx2txt
import re
import io
import matplotlib.pyplot as plt
import random
import pandas as pd
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

def counter(extension):
    global decision
    global filename

    if extension.__contains__('.docx'):#checks if the extension is docx
        try: #Used to check if file exists or not
            doc = docx2txt.process(filename)  # extract docx to text
            logic(doc)
        except FileNotFoundError as error:   
            print("File does not exist. Enter an existing file.")
            filename = ""
            decision = 1

    elif extension.__contains__(".pdf"):#checks if the extension is pdf
        logic(extract_text(filename))
    elif extension.__contains__('.docx') == False or extension.__contains__(".pdf") == False: #Checks if the format of entered value is correct
        print("Please enter a valid filename along with its extension.")
        decision = 1

def extract_by_page(filename):
    try: #Used to check if file exists or not
        with open(r""+filename, 'rb') as fh:
            for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
                res_manager = PDFResourceManager()
                fake_file = io.StringIO()
                convert = TextConverter(res_manager, fake_file)
                interpreter = PDFPageInterpreter(res_manager, convert)
                interpreter.process_page(page)

                text = fake_file.getvalue()
                yield text

                # close open handles
                convert.close()
                fake_file.close()
    except FileNotFoundError as error:
        global decision
        print("File does not exist. Enter an existing file.")
        filename = ""
        decision = 1
        

def extract_text(file):
    noOfPage = ''
    for page in extract_by_page(file):
        noOfPage += page
    return noOfPage

def logic(document):
    global words
    try: #Ignores the Exception found when handling another exception which is displayed when the program ends
        remove = re.sub('[!,\???*)@#%\"(&$_/?.\]\[^]', '', document).lower()# remove special character
        for word in remove.split():  # 1 word per space
            words[word] = words.get(word, 0) + 1  # Each word that can be seen the counter adds one
        if words:
            df = pd.DataFrame(list(words.items()),columns = ['Words','Count'])#dictionary to dataframe
            print(df)
            print("\nGenerating Graph...")
    except:
        pass

def displayGraphs():
    global words
    x = []
    y = []
    rgb = []
    for Word, Count in words.items():
        x.append(Word) # put the words to x axis
        y.append(Count) # put the count to y axis
        rgb.append([random.random(), random.random(), random.random()]) #Generates a random numbers for the colors of the plots
        

    bar = plt.figure(1)
    ax = bar.add_subplot(111)
    plt.bar(x, y, color = rgb) #Bar Graph
    plt.title('Bar Graph for the File', fontsize = 18)
    plt.ylabel('Amount of times the words are repeated', fontsize = 18)
    plt.xlabel('Words found in the File', fontsize = 18)
    plt.xticks(fontsize=9, rotation=60, ha="right")
    plt.margins(x=0)
    plt.tight_layout()
    plt.xlim(0,50)
    plt.ylim(0, 100)
    ymax = max(y) #max value
    xpos = y.index(ymax) #x pos ng max
    xmax = x[xpos]  
    ax.annotate('Highest word count', xy=(xmax, ymax), xytext=(xmax, ymax+7),
    arrowprops=dict(arrowstyle="->"))
    mng = plt.get_current_fig_manager()
    mng.resize(1920, 1080)
    
    bar.show()

decision = 0
filename = ""
words = {}
print("\nHey there! Welcome to the Word Frequency Generator")
while True:
    filename = str(input("\nPlease Enter your file name: "))
    counter(filename)
    if decision != 1: #Helps determine if the filename entered is wrong or not and repeats the entering of file name if necessary
        pass
    else:
        decision = 0
        continue
    
    displayGraphs()
    words = {}

    while True:
        outcome = str(input("\nWould you like to enter another? (Y,N): ")).lower()
        try:
            assert(outcome in ['y', 'n'])
            break
        except:
            print('\nInvalid Input. Please enter only Y or N.')

    if (outcome == 'y'):
        continue

    elif (outcome == 'n'):
        print("\n\n     Thank you for using our program. \n\n\t-------------------------\n\t|Made by:\t\t| \n\t|Marc Ricafort\t\t| \n\t|Stanley Orong III\t| \n\t|Patricia Valenzuela\t| \n\t|Cyril Verdad\t\t| \n\t|From 3-ITG\t\t| \n\t-------------------------\n")
        break
    
