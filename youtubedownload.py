#importing all the modules
from tkinter import *
import os
from tkinter.ttk import *
from tkinter.messagebox import *
from pytube import YouTube

root = Tk()
root.geometry("300x300")

#checking if the folder exists or not , if does not exists then creating a new folder
newpath = r"C:\Downlaoded Videos"
if not os.path.exists(newpath):
    os.makedirs(newpath)

#function to download videos
def download():
    yt = YouTube(e1.get())
    yt1 = yt.streams.get_by_resolution(c1.get())
    showinfo("Notification" , "Downloading the Video")
    yt1.download(newpath)
    showinfo("NOtification" , "Downloaded the Video in C:\Downloaded Videos")

#creating the Widgets and main screen
root.title("Youtube Video Downloader")
l1 = Label(root , text = "Enter Link")
l1.grid(row=0 , column=0)
l2 = Label(root , text = "Resolution")
l2.grid(row=1 , column = 0)
e1 = Entry(root , width=35)
e1.grid(row = 0 , column = 1)
c1 = Combobox(root , values = ['360p' , '480p' , '720p'])
c1.grid(row = 1 , column = 1)
b1 = Button(root , text = "Download Video" , command = download)
b1.grid(row = 4 , column = 1)
root.mainloop()

