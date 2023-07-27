import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

# Load and process the animated GIFs
gif_files = ["images/gifs/bench.gif", "images/gifs/incline.gif"]
gif_labels = []
current_gif_index = 0
replay_count = 0
image_frame_list_resized = []
photo_images = []  # Store PhotoImage objects

for file in gif_files:
    frames = Image.open(file)
    original_width, original_height = frames.size

    # Define the desired resized width and height
    desired_width = 200
    desired_height = 200

    # Calculate the new width and height while maintaining the aspect ratio
    aspect_ratio = original_width / original_height
    if original_width > original_height:
        new_width = desired_width
        new_height = int(desired_width / aspect_ratio)
    else:
        new_height = desired_height
        new_width = int(desired_height * aspect_ratio)

    # Resize each frame of the GIF and store them in "image_frame_list_resized"
    image_frames = [frame.resize((new_width, new_height)) for frame in ImageSequence.Iterator(frames)]
    gif_labels.append(image_frames)

# Create PhotoImage objects for all frames of all GIFs and store them in the list
for frames in gif_labels:
    gif_frames = [ImageTk.PhotoImage(frame) for frame in frames]
    photo_images.append(gif_frames)

# Function to display the current GIF frame
def display_frame(count):
    global replay_count
    im = photo_images[current_gif_index][count]

    gif_label.configure(image=im)  # Updates the image displayed in the label "gif_label"
    count += 1
    if count < len(photo_images[current_gif_index]):  # Check if there are more frames to display
        root.after(50, lambda: display_frame(count))  # Schedule the next frame update after 50 milliseconds
    else:
        replay_count += 1
        if replay_count == 1:  # Only enable "Replay" button after the first playthrough
            replay_button.config(state=tk.NORMAL)
        if replay_count == 2:  # Enable "Next" button after the second playthrough
            next_button.config(state=tk.NORMAL)

# Function to replay the current GIF
def replay_gif():
    global replay_count
    replay_count = 0
    replay_button.config(state=tk.DISABLED)  # Disable the "Replay" button until the GIF finishes replaying
    next_button.config(state=tk.DISABLED)  # Disable the "Next" button during replay
    display_frame(0)  # Start displaying frames of the current GIF

# Function to switch to the next GIF
def next_gif():
    global current_gif_index, replay_count
    if current_gif_index < len(gif_files) - 1:
        current_gif_index += 1
        replay_count = 0
        replay_button.config(state=tk.DISABLED)  # Disable the "Replay" button until the new GIF finishes playing
        next_button.config(state=tk.DISABLED)  # Disable the "Next" button until the new GIF finishes playing
        display_frame(0)  # Start displaying frames of the new GIF

# Create the main window
root = tk.Tk()

# Creates a label widget to display the animated GIF
gif_label = tk.Label(root, image="")
gif_label.place(relx=0.25, rely=0.38, anchor=tk.CENTER)

# Create the "Replay" button
replay_button = tk.Button(root, text="Replay", command=replay_gif, state=tk.DISABLED)
replay_button.place(relx=0.4, rely=0.9, anchor=tk.CENTER)

# Create the "Next" button
next_button = tk.Button(root, text="Next", command=next_gif, state=tk.DISABLED)
next_button.place(relx=0.6, rely=0.9, anchor=tk.CENTER)

# Start displaying frames of the first GIF
display_frame(0)

# Start the main event loop
root.mainloop()
