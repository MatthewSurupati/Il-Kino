import tkinter

window = tkinter.Tk()
label = tkinter.Label(window, text='IlKino \n Nansenstrasse 22 \n 12047 Berlin \n SCREEN')
tombol = tkinter.Button(window, text='Booking')
tombol1 = tkinter.Button(window, text='Find By Name')
tombol2 = tkinter.Button(window, text='Report')
tombol3 = tkinter.Button(window, text='Exit')

label.pack()
tombol.pack()
tombol1.pack()
tombol2.pack()
tombol3.pack()
window.mainloop()