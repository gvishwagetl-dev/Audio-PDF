from tkinter.filedialog import askopenfilename
import pyttsx3
import pypdf 

book = askopenfilename()
reader = pypdf.PdfReader(book)
player = pyttsx3.init()


for page in reader.pages:
  text = page.extract_text()
  if text:  
    player.say(text)
    player.runAndWait()