import pyttsx3
import PyPDF2

#Add the name of the pdf book that needs to be read
book = open('object_oriented_python_tutorial.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
for num in range(7, pages):
    page = pdfReader.getPage(7)
    text = page.extractText()
    engine.say(text)
    engine.runAndWait()
