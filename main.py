import os 
from render import render

'''
videos_dir = './videos'
video_files = os.listdir(videos_dir)

with open('input.txt', 'w') as f:
    for video_file in video_files:
        f.write(f"file '{videos_dir}/{video_file}'\n")
'''

render.concat_videos()