from tkinter import *
from pytube import YouTube

window = Tk()
window.geometry("600x700")
window.config(bg="lightblue")
window.title("YouTube Video Downloader")

youtube_logo = PhotoImage(file="youtube.png")
window.iconphoto(False, youtube_logo)

Label(window, text="HCI Lab Assignment 6", font=("Arial", 18, "bold")).pack(padx=5, pady=5)
Label(window, text="GUI Design using Python", font=("Arial", 12, "bold")).pack(padx=5, pady=5)
Label(window, text="YouTube Video Downloader", font=("Arial", 30, "bold"), bg="red").pack(padx=5, pady=5)

video_link = StringVar()

Label(window, text="Enter the link below:", font=("Arial", 24, "bold"), bg="white").place(x=130, y=200)
Entry_link = Entry(window, width=60, font=35, textvariable=video_link, bd=4).place(x=35, y=300)

def video_download():
    video_url = YouTube(str(video_link.get()))
    videos = video_url.streams.first()
    videos.download()

    Label(window, text="Download completed!", font=("Arial", 20, "bold"), bg="lightgreen", fg="black").place(x=35, y=500)
    Label(window, text="Check your project folder for the downloaded file", font=("Arial", 18), bg="Yellow").place(x=35, y=550)

Button(window, text="Download", font=("Arial", 24, "bold"), bg = "white", command=video_download).place(x=35, y=400)


window.mainloop()
