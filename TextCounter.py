import docx2txt
import re
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

filename = str(input("Enter file name: "))
def counter(extension):

    if extension.__contains__('.docx') or extension.__contains__('.doc'):
        doc = docx2txt.process(filename)  # extract docx to text
        logic(doc)
    elif extension.__contains__(".pdf"):
        logic(extract_text(filename))

def extract_text_by_page(filename):
    with open(r""+filename, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)

            text = fake_file_handle.getvalue()
            yield text

            # close open handles
            converter.close()
            fake_file_handle.close()


def extract_text(filename):
    for page in extract_text_by_page(filename):
        return page
def logic(string):

    words = {}
    remove = re.sub('[!,*)@#%(&$_?.\]\[^]', '', string).lower()# tanggal special character
    #remove = " ".join(re.findall(r"[a-zA-Z0-9]+", string)).lower()
    for word in remove.split():  # para kada space isang word
        words[word] = words.get(word, 0) + 1  # transform file to dict # dict kasi para makuha yung key example (2:"the") means two time lumabas yung the

    for w, c in words.items():  # print lang pero di to gagawin graph dapat
        if len(w) > 1 or (len(w) > 0 and (w==('a'.lower()) or w == ('i').lower())): # if less than 3 letter sya #note:pwede to tanggalin kung ano na lng trip nyo
            print("%s: %d times" % (w, c))



counter(filename)