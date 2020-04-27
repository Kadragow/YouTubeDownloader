from pytube import YouTube
import os
import subprocess


class VideoYT:
    def __init__(self, video_link):
        self.video_link = video_link
        self.video = YouTube(video_link)

    def download_video(self, video_name, i_tag, choice):
        if choice == '1':
            video_to_download = self.video.streams.get_by_itag(i_tag)
            if not video_to_download.includes_audio_track:
                self.video.streams.get_by_itag(i_tag).download(filename="tmp_" + video_name)
                # next to file must exist path to ffmpeg
                ffpath = "ffmpeg\\bin\\ffmpeg.exe"
                self.video.streams.filter(type="audio").first().download(filename=(video_name+"-audio"))
                video_file = "tmp_" + video_name + ".mp4"
                audio_file = video_name + "-audio.mp4"
                out_file = video_name + ".mp4"
                if os.path.isfile(out_file):
                    out_file += "(1)"
                cmd = "{0} -i {1} -i {2} -c copy {3}".format(ffpath, video_file, audio_file, out_file)
                subprocess.run(cmd)
                os.remove("tmp_" + video_name + ".mp4")
                os.remove(video_name + "-audio.mp4")
            else:
                self.video.streams.get_by_itag(i_tag).download(filename=video_name)
        else:
            tmp_file = self.video.streams.get_by_itag(i_tag).download(filename=video_name)
            os.rename(tmp_file, video_name + '.mp3')

    def get_video_resolutions(self):
        return self.video.streams.filter(type="video", file_extension='mp4')

    def get_sound_only(self):
        return self.video.streams.filter(type="audio")
