from pytube import YouTube
import os


class VideoYT:
    def __init__(self, video_link):
        self.video_link = video_link
        self.video = YouTube(video_link)

    def download_video(self, video_name, i_tag, choice):
        if choice == '1':
            self.video.streams.get_by_itag(i_tag).download(filename=video_name)
        else:
            tmp_file = self.video.streams.get_by_itag(i_tag).download(filename=video_name)
            os.rename(tmp_file, video_name + '.mp3')

    def get_video_resolutions(self):
        return self.video.streams.filter(type="video")

    def get_sound_only(self):
        return self.video.streams.filter(type="audio")
