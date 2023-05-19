import requests
import tkinter as tk
from tkinter import *
from handler import Handler
from PIL import ImageTk, Image

root = Tk()
root.resizable(False,False)
root.title("YouTube Downloader")

width = 1000
height = 300

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

def start():
        
    textEntry = tk.Entry(root, width=50, text="Enter URL", font="Arial 18", bd=4)
    textEntry.place(relx=0.2,rely=0.5)
    global searchButton
    searchButton = tk.Button(root, height=1, width=5, text="Search", font="Arial 14", command=lambda: search(textEntry.get()))
    searchButton.place(relx=0.875,rely=0.5)

def search(url):

    if urlValid:
        try:
            handler = Handler(url)
            image = ImageTk.PhotoImage(Image.open(handler.getThumbnail()))
            display = tk.Label(root, image=image)
            display.image = image # reference to stop garbage collection
            display.place(relx=0.5, rely=0.1)

            videoVal = tk.Label(root, text="Video Found!!", font="Arial 14")
            videoVal.place(relx=0.5, rely=0.35)

            searchButton.destroy()

            # Init download options
            downloadAudioButton = tk.Button(root, height=1, width=15, text="Download Audio", font="Arial 14", command=lambda: handler.downloadAudio())
            downloadAudioButton.place(relx=0.4,rely=0.7)
            downloadVideoButton = tk.Button(root, height=1, width=15, text="Download Video", font="Arial 14", command=lambda: handler.downloadVideo())
            downloadVideoButton.place(relx=0.6,rely=0.7)

            # Start again Button
            searchAgainButton = tk.Button(root, height=1, width=7, text="Try Again", font="Arial 14", command=lambda: print("3"))
            searchAgainButton.place(relx=0.875,rely=0.5)
        except:
            displayError()
    else:
        displayError()

def urlValid(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def displayError():
    errorText = tk.Label(root, text="Something went wrong, try again", font="Arial 12")
    errorText.place(relx=0.1, rely=0.1)
    root.after(2000, errorText.destroy)

start()
root.mainloop()
