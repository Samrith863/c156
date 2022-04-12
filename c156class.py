from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.title("Dice Game")
root.geometry("600x400")
img1=ImageTk.PhotoImage(Image.open("dice4.jpg"))

label_player1=Label(root,text="Player 1",bg="blue",fg="white")
label_player2=Label(root,text="Player 2",bg="blue",fg="white")
label_player1_score=Label(root,bg="blue",fg="white")
label_player2_score=Label(root,bg="blue",fg="white")
label_show_score=Label(root,bg="orange",fg="white")

label_player1.place(relx=0.1,rely=0.3,anchor=CENTER)
label_player2.place(relx=0.9,rely=0.3,anchor=CENTER)
label_player1_score.place(relx=0.1,rely=0.4,anchor=CENTER)
label_player2_score.place(relx=0.9,rely=0.4,anchor=CENTER)
label_show_score.place(relx=0.5,rely=0.2,anchor=CENTER)

root.mainloop()

