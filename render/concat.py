import os 
import subprocess

def concat_videos(width=1280, height=720):
    '''
    File paths should be relative to the root directory of the project.
    Regardless of where you call this function, subprocess.run() will always
    assume that you are calling it from the root directory of the project.
    '''
    
    ffmpeg_command = [
        "ffmpeg",
        "-f", "concat",
        "-safe", "0",
        "-i", "input.txt",
        "-filter_complex", f"[0:v]scale=w={width}:h={height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,setsar=1",
        "-c:a", "copy",
        "-y", # Overwrite existing output file without asking
        "videos/output.mp4"
    ]

    subprocess.run(ffmpeg_command)
