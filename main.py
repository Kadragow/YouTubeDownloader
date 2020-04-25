import re
from VideoYT import VideoYT

pattern_res = r'res="([A-Za-z0-9_\./\\-]*)"'
pattern_itag = r'itag="([A-Za-z0-9_\./\\-]*)"'
pattern_abr = r'abr="([A-Za-z0-9_\./\\-]*)"'
pattern_format = r'mime_type="video/([A-Za-z0-9_\./\\-]*)"'


vid = VideoYT(input("Enter video URL: "))

choice = input("If you want to download video, please enter '1', if only sound enter something else: ")
if choice == '1':
    for x in vid.get_video_resolutions():
        print("Video itag: {0}, resolution: {1}, format: {2}\n"
              .format(
                re.search(pattern_itag, str(x)).group(1),
                re.search(pattern_res, str(x)).group(1),
                re.search(pattern_format, str(x)).group(1)))
else:
    for x in vid.get_sound_only():
        print("Audio itag: {0}, quality: {1}\n".format(re.search(pattern_itag, str(x)).group(1), re.search(pattern_abr, str(x)).group(1)))
vid.download_video(input("Enter video/sound name: "), input('Enter video/sound itag: '), choice)

# my test video 'https://www.youtube.com/watch?v=7CVtTOpgSyY'

