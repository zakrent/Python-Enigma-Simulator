#!/usr/bin/python3

from classes import Enigma, dictionaries
import tkinter as tk

class GUI(tk.Frame):


	def __init__(self, master, enigma):
		super().__init__(master)
		self.pack()
		self.master.title('Enigma simulator')
		self.master.resizable(False, False)

		self.enigma = enigma

		self.textOutput = tk.Text(master, height = 5, width = 50, state = tk.NORMAL, bg = '#E0E0E0')
		self.textOutput.pack( side = tk.BOTTOM)

		self.textInput = tk.Text(master, height = 5, width = 50)
		self.textInput.pack( side = tk.BOTTOM)

		self.letters = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z')

		self.rotorsPositions = []
		for i in range(3):
			self.rotorsPositions.append(tk.Spinbox(master,values = self.letters, width = 1, command=self.changeRotorPos))
			self.rotorsPositions[i].pack(side = tk.LEFT)

		self.encryptButton = tk.Button(master, text ="Encrypt", height = 1, command = self.encrypt)
		self.encryptButton.pack(side = tk.RIGHT)

		self.encryptButton = tk.Button(master, text ="Set crosover(INOP)", height = 1, command = None)
		self.encryptButton.pack(side = tk.RIGHT)


	def changeRotorPos(self):
		for i in range(3):
			position = self.rotorsPositions[i].get()
			position = dictionaries.CharToInt[position]
			self.enigma.setRotorPos(i,position)

	def encrypt(self):
		self.changeRotorPos()
		text = self.textInput.get(1.0, tk.END)
		text = text[:len(text)-1]
		text = list(filter((lambda text: text.upper() in self.letters), text.upper()))
		text = "".join(text)
		text = self.enigma.encrypt(text)
		#self.textOutput.config(state = tk.NORMAL)
		self.textOutput.delete(1.0,tk.END)
		self.textOutput.insert(tk.END, text)
		#self.textOutput.config(state = tk.DISABLED)

def main():
	root = tk.Tk()
	enigma = Enigma([1,2,3])
	app = GUI(root, enigma)
	app.mainloop()

if __name__ == '__main__':
	main()
