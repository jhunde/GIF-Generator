from moviepy.editor import VideoFileClip

# Load video file
video = VideoFileClip("your_video.mp4")

# Define the start and time of GIF
start = 5
end = 10

# Extract video clip
clip = video.subclip(start, end)

# Save extracted video as GIF
clip.write_gif("output.gif", fps=10)
