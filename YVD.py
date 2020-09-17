import tkinter
from tkinter import *
from pytube import YouTube

root= Tk()

root.geometry("400x300")

root.title("Youtube Video Downloader Application")

def download():
    try:
        myVar.set("Downloading...")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("Video downloaded successsfully")
    except Exception as e:
        myVar.set("Mistake")
        root.update()
        link.set("Enter Correct Link")
        
Label(root, text="Welcome to youtube\nDownloader Application", font="Consolas 15 bold").pack()

myVar=StringVar()

myVar.set("Enter the link below")

Entry(root, textvariable=myVar, width=30).pack(pady=10)

link=StringVar()

Entry(root, textvariable=link, width=50).pack(pady=10)

Button(root, text="Download Video", command=download).pack()

my=StringVar()
my.set("khao peeo aish karo")
Label(root, textvariable=my, font="Helvetica").pack(pady=30)

Label(root, text="by Divyanshu", font="Helvetica").pack()

root.mainloop()

#YouTube("https://www.youtube.com/watch?v=1FeuE6Uqm9Y").streams.first().download()
