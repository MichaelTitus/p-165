from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.geometry("600x600")
root.config(background = "black")

label_image = Label(root, bg="white", highlightthickness=5)
label_image.place(relx=0.5, rely=0.5, anchor=CENTER)

img_path=""
def openFile():
    global img_path
    img_path=filedialog.askopenfilename(title="open image file",filetypes=(("image Files","*.jpg *.gif *.jpeg *.png"),))
    open_image=ImageTk.PhotoImage(Image.open(img_path))
    label_image["image"]=open_image
    open_image.close()

def rotateImage():
    global img_path
    im=Image.open(img_path)
    open_image=ImageTk.PhotoImage(im.rotate(270))
    label_image["image"]=open_image
    open_image.close()

   
btn=Button(root,text="Open Image",font= ("Times New Roman0", 12),bg="grey",fg="white", command=openFile, relief=SOLID, padx=15, pady=10)
btn.place(relx=0.5,rely=0.1,anchor=CENTER)

btn1=Button(root,text="Rotate Image",font= ("Times New Roman0", 12),bg="grey",fg="white", command=rotateImage, relief=SOLID, padx=15, pady=10)
btn1.place(relx=0.5,rely=0.85,anchor=CENTER)

label_footer = Label(root,text="Created by whitehatjr team", bg="black", fg="white")
label_footer.place(relx=0.5, rely=0.95, anchor=CENTER)




root.mainloop()
  