import requests
from io import BytesIO
from pytube import YouTube

class Handler:

    def __init__(self, link):
        self.link = link
        self.id = link.split("=")[1]
        self.img = f"https://img.youtube.com/vi/{self.id}/default.jpg"
        self.yt = YouTube(self.link)

    def getThumbnail(self):
        return BytesIO(requests.get(self.img).content)
    
    def downloadVideo(self):
        try:
            video = self.yt.streams.get_highest_resolution()
            video.download()
        except:
            print("lol")

    def downloadAudio(self):
        try:
            audio = self.yt.streams.filter(only_audio=True, file_extension="mp3").order_by("abr").desc().first()
            audio.download()
        except:
            audio = self.yt.streams.filter(only_audio=True).first()
            audio.download()



