from rembg import remove
from PIL import Image
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import Tk

janela = Tk()
janela.geometry("250x250")
janela.title("Back Remove")



#def one_click():
#input = Image.open("lucas.jpg")
#output = remove(input)
#output.save("lucas1.png")

#def btn_select():
#Tk().withdraw() # Isto torna oculto a janela principal
#filename = askopenfilename() # Isto te permite selecionar um arquivo
#print(filename) # printa o arquivo selecionado

infoImage = Label(text="Arquivo de imagem")
infoImage.place(x=50, y=10)

btnSelect = Button(width=15, text="Selecionar Imagem")
btnSelect.place(x=100, y=65)

btnTransformar = Button(width=10, text="Operar")
btnTransformar.place(x=50, y=150)


janela.mainloop()