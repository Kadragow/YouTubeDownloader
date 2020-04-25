from VideoYT import VideoYT

vid = VideoYT(input("Enter video URL: "))

choice = input("If you want to download video, please enter '1', if only sound enter something else: ")
if choice == '1':
    for x in vid.get_video_resolutions():
        print("itag: {0} {1}\n".format(x, vid.get_video_resolutions().get(x)))
    # print(vid.get_video_resolutions())
else:
    print(vid.get_sound_only())
vid.download_video(input("Enter video/sound name: "), input('Enter video/sound itag: '), choice)

# video = YouTube('https://www.youtube.com/watch?v=7CVtTOpgSyY')

