# Importing the necessary modules for the GUI and image handling
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

# Create the main window
root = tk.Tk()
root.title("GymGenius")  # Sets the window title to "GymGenius"
root.geometry("500x500")  # Sets the window size to 500x500 pixels
root.configure(bg="#F1EFE7")  # Sets the window background color to "#F1EFE7"

# Load and process the animated GIF
file = "images/gifs/gymgenius.gif"
frames = Image.open(file)  # Opens the "gymgenius.gif" file using the PIL library
image_frame_list = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(frames)]
# Converts each frame of the GIF into a PhotoImage object and stores them in "image_frame_list"

# Function to animate the frames of the GIF
def animation(count):
    im = image_frame_list[count]

    gif_label.configure(image=im)  # Updates the image displayed in the label "gif_label"
    count += 1
    if count < len(image_frame_list):  # Check if there are more frames to display
        root.after(50, lambda: animation(count))  # Schedule the next frame update after 50 milliseconds

# Creates a label widget to display the animated GIF
gif_label = tk.Label(root, image="")
gif_label.pack()

# Function to hide the start button
def hide_start():
    image_button1.pack_forget()  # Hides the start button ("image_button1")

# Load and resize the first image for the start button
image1 = Image.open("images/buttons/button.png")
image1 = image1.resize((300, 100))  # Resizes the image to 300x100 pixels
photo1 = ImageTk.PhotoImage(image1)  # Creates a PhotoImage object from the resized image

# Creates a button widget for the start button
image_button1 = tk.Button(root, image=photo1, bg="#F1EFE7", borderwidth=0, highlightthickness=0, command=lambda: (root.after(1300, start), hide_start(), animation(0)))
image_button1.pack(pady=(100, 50))

#Global Variables that are called to by the functions
image_frame_list_resized = None
count = 0
replay = False
gif_index = 0

def start():
    root.withdraw()  # Hides the main window ("root")

    # Create a new top-level window for the intro page
    intro_page = tk.Toplevel(root)
    intro_page.geometry("500x500")  # Sets the size of the start page window to 500x500 pixels
    intro_page.configure(bg="#F1EFE7")  # Sets the background color of the start page window
    
    def main():
        intro_page.withdraw()  # Hides the main window ("root")
        
            
        # Create a new top-level window for the main page
        main_page = tk.Toplevel(root)
        main_page.geometry("500x500")  # Sets the size of the start page window to 500x500 pixels
        main_page.configure(bg="#F1EFE7")
        
        def push():
            global gif_index
            global image_frame_list_resized
            main_page.withdraw()
                
            push_page = tk.Toplevel(root)
            push_page.geometry("500x500")
            push_page.configure(bg="#F1EFE7")
            
            def back():
                push_page.destroy()
                main()
            
            #Load and resize the back image
            back_image = Image.open("images/buttons/back.png")
            back_image = back_image.resize((30,30))
            back_photo = ImageTk.PhotoImage(back_image)
    
            back_button = tk.Button(push_page, image=back_photo, bg="#F1EFE7", borderwidth=0, highlightthickness=0, command=back)
            back_button.image = back_photo
            back_button.place(relx=0.05, rely=0.1, anchor=tk.SW)
    
           
            # Function to load and prepare the GIF frames for animation
            def load_gif_frames(gif_path):
                frames = Image.open(gif_path)
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
                return [ImageTk.PhotoImage(frame.resize((new_width, new_height))) for frame in ImageSequence.Iterator(frames)]

    

            def next_button_click():
                global gif_index, image_frame_list_resized, count, replay

                if gif_index == len(gif_paths) - 1:
                    #If gif_index is already at the last GIF, do nothing and return
                    return

                gif_index += 1# Increment gif_index to display the next GIF
                gif_path = gif_paths[gif_index]

                #Load and prepare the GIF frames for animation
                image_frame_list_resized = load_gif_frames(gif_path)

                #Reset the count and replay flag
                count = 0
                replay = False
                
            def previous_button_click():
                global gif_index, image_frame_list_resized, count, replay

                if gif_index == 0:
                    #If gif_index is already at the first GIF, do nothing and return
                    return

                gif_index -= 1  #Decrement gif_index to display the next GIF
                gif_path = gif_paths[gif_index]

                #Load and prepare the GIF frames for animation
                image_frame_list_resized = load_gif_frames(gif_path)

                #Reset the count and replay flag
                count = 0
                replay = False

                
            # Function to animate the resized frames of the GIF
            def main_animation(count):
                global image_frame_list_resized
                im = image_frame_list_resized[count]

                gif_label.configure(image=im)  # Updates the image displayed in the label "gif_label"
                count += 1

                if count < len(image_frame_list_resized):  # Check if there are more frames to display
                    root.after(50, lambda: main_animation(count))  # Schedule the next frame update after 50 milliseconds

            
            benchlogo_image = Image.open("images/statements/benchlogo.png")
            benchlogo_image = benchlogo_image.resize((200, 50))
            benchlogo_photo = ImageTk.PhotoImage(benchlogo_image)

            benchlogo_label = tk.Label(push_page, image=benchlogo_photo, bg="#F1EFE7")
            benchlogo_label.image = benchlogo_photo
            benchlogo_label.place(relx=0.5, rely=0.08, anchor=tk.CENTER)
            
            benchinfo_image = Image.open("images/statements/benchinfo.png")
            benchinfo_image = benchinfo_image.resize((250, 260))
            benchinfo_photo = ImageTk.PhotoImage(benchinfo_image)
            
            benchinfo_label = tk.Label(push_page, image=benchinfo_photo, bg="#F1EFE7")
            benchinfo_label.image = benchinfo_photo
            benchinfo_label.place(relx=1, rely=0.5, anchor=tk.E)
        
            inclinelogo_image = Image.open("images/statements/inclinelogo.png")
            inclinelogo_image = inclinelogo_image.resize((250, 60))
            inclinelogo_photo = ImageTk.PhotoImage(inclinelogo_image)

            inclinelogo_label = tk.Label(push_page, image=inclinelogo_photo, bg="#F1EFE7")
            inclinelogo_label.image = inclinelogo_photo
            
            inclineinfo_image = Image.open("images/statements/inclineinfo.png")
            inclineinfo_image = inclineinfo_image.resize((250, 260))
            inclineinfo_photo = ImageTk.PhotoImage(inclineinfo_image)
            
            inclineinfo_label = tk.Label(push_page, image=inclineinfo_photo, bg="#F1EFE7")
            inclineinfo_label.image = inclineinfo_photo
            
            shoulderpresslogo_image = Image.open("images/statements/shoulderlogo.png")
            shoulderpresslogo_image = shoulderpresslogo_image.resize((250, 60))
            shoulderpresslogo_photo = ImageTk.PhotoImage(shoulderpresslogo_image)
            
            shoulderpresslogo_label = tk.Label(push_page, image=shoulderpresslogo_photo, bg="#F1EFE7")
            shoulderpresslogo_label.image = shoulderpresslogo_photo
            
            shoulderpressinfo_image = Image.open("images/statements/shoulderinfo.png")
            shoulderpressinfo_image = shoulderpressinfo_image.resize((250, 260))
            shoulderpressinfo_photo = ImageTk.PhotoImage(shoulderpressinfo_image)
            
            shoulderpressinfo_label = tk.Label(push_page, image=shoulderpressinfo_photo, bg="#F1EFE7")
            shoulderpressinfo_label.image = shoulderpressinfo_photo
            
            laterallogo_image = Image.open("images/statements/laterallogo.png")
            laterallogo_image = laterallogo_image.resize((250, 60))
            laterallogo_photo = ImageTk.PhotoImage(laterallogo_image)
            
            laterallogo_label = tk.Label(push_page, image=laterallogo_photo, bg="#F1EFE7")
            laterallogo_label.image = laterallogo_photo
            
            lateralinfo_image = Image.open("images/statements/lateralinfo.png")
            lateralinfo_image = lateralinfo_image.resize((250, 260))
            lateralinfo_photo = ImageTk.PhotoImage(lateralinfo_image)
            
            lateralinfo_label = tk.Label(push_page, image=lateralinfo_photo, bg="#F1EFE7")
            lateralinfo_label.image = lateralinfo_photo
            
            ropetriceplogo_image = Image.open("images/statements/ropetriceplogo.png")
            ropetriceplogo_image = ropetriceplogo_image.resize((250, 60))
            ropetriceplogo_photo = ImageTk.PhotoImage(ropetriceplogo_image)
            
            ropetriceplogo_label = tk.Label(push_page, image=ropetriceplogo_photo, bg="#F1EFE7")
            ropetriceplogo_label.image = ropetriceplogo_photo
            
            ropetricepinfo_image = Image.open("images/statements/ropetricepinfo.png")
            ropetricepinfo_image = ropetricepinfo_image.resize((250, 260))
            ropetricepinfo_photo = ImageTk.PhotoImage(ropetricepinfo_image)
            
            ropetricepinfo_label = tk.Label(push_page, image=ropetricepinfo_photo, bg="#F1EFE7")
            ropetricepinfo_label.image = ropetricepinfo_photo
            
            tricepoverheadlogo_image = Image.open("images/statements/tricepoverheadlogo.png")
            tricepoverheadlogo_image = tricepoverheadlogo_image.resize((250, 60))
            tricepoverheadlogo_photo = ImageTk.PhotoImage(tricepoverheadlogo_image)
            
            tricepoverheadlogo_label = tk.Label(push_page, image=tricepoverheadlogo_photo, bg="#F1EFE7")
            tricepoverheadlogo_label.image = tricepoverheadlogo_photo
            
            tricepoverheadinfo_image = Image.open("images/statements/tricepoverheadinfo.png")
            tricepoverheadinfo_image = tricepoverheadinfo_image.resize((250, 260))
            tricepoverheadinfo_photo = ImageTk.PhotoImage(tricepoverheadinfo_image)
            
            tricepoverheadinfo_label = tk.Label(push_page, image=tricepoverheadinfo_photo, bg="#F1EFE7")
            tricepoverheadinfo_label.image = tricepoverheadinfo_photo
            
            
            
            # Creates a label widget to display the animated GIF
            gif_label = tk.Label(push_page, image="")
            gif_label.place(relx=0.25, rely=0.38, anchor=tk.CENTER)

            # Initialize the gif_index and load the first GIF
            gif_paths = ["images/gifs/push/bench.gif", "images/gifs/push/incline.gif", 
                         "images/gifs/push/shoulderpress.gif", "images/gifs/push/lateralraise.gif",
                         "images/gifs/push/ropetricep.gif", "images/gifs/push/overheadtricep.gif"]  # Add more paths as needed
            gif_index = 0
            image_frame_list_resized = load_gif_frames(gif_paths[gif_index])
            
            
            # List of labels to be shown in sequence
            labels_to_show = [benchlogo_label, inclinelogo_label, shoulderpresslogo_label, laterallogo_label, ropetriceplogo_label, tricepoverheadlogo_label]  # Add more labels if needed
            info_to_show= [benchinfo_label, inclineinfo_label, shoulderpressinfo_label, lateralinfo_label, ropetricepinfo_label, tricepoverheadinfo_label]
            current_label_index = 0  # Index to keep track of the currently displayed label
            current_info_index = 0


            # Function to handle the next button click
            def show_next_label():
                nonlocal current_label_index
                nonlocal current_info_index
    
                if current_label_index == len(labels_to_show) - 1:
                    # If we reached the last label, do nothing and return
                    return

                current_label = labels_to_show[current_label_index]
                current_info = info_to_show[current_info_index]
                current_label.place_forget()  # Hide the previous label
                current_info.place_forget()
    
                current_label_index += 1
                current_info_index += 1
    
                next_label = labels_to_show[current_label_index]  # Get the next label to show
                next_info = info_to_show[current_info_index]
                next_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)  # Show the next label
                next_info.place(relx=1, rely=0.5, anchor=tk.E)
                
           # Function to handle the previous button click
            def show_previous_label():
                nonlocal current_label_index
                nonlocal current_info_index
    
                if current_label_index == 0:
                    # If we reached the first label, do nothing and return
                    return
    
                current_label = labels_to_show[current_label_index]
                current_info = info_to_show[current_info_index]
                current_label.place_forget()  # Hide the current label
                current_info.place_forget()
    
                current_label_index -= 1
                current_info_index -= 1

                previous_label = labels_to_show[current_label_index]  # Get the previous label to show
                previous_info = info_to_show[current_info_index]
                previous_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)  # Show the previous label
                previous_info.place(relx=1, rely=0.5, anchor=tk.E)
                    
            #Load and resize the next image
            next_image = Image.open("images/buttons/next.png")
            next_image = next_image.resize((30, 30))
            next_photo = ImageTk.PhotoImage(next_image)

            #Creates a button widget
            next_button = tk.Button(push_page, image=next_photo, bg="#F1EFE7", borderwidth=0, highlightthickness=0, command=lambda: (show_next_label(), next_button_click()))
            next_button.image = next_photo
            next_button.place(relx=0.95, rely=0.95, anchor=tk.SE)  
            
            start_image = Image.open("images/buttons/button.png")
            start_image = start_image.resize((200, 50))
            start_photo = ImageTk.PhotoImage(start_image)

            start_button = tk.Button(push_page, image=start_photo, bg="#F1EFE7", borderwidth=0, highlightthickness=0, command=lambda: main_animation(0))
            start_button.image = start_photo
            start_button.place(relx=0.25, rely=0.7, anchor=tk.S)
            
            #Load and resize the back image
            back_image = Image.open("images/buttons/back.png")
            back_image = back_image.resize((30,30))
            back_photo = ImageTk.PhotoImage(back_image)
    
            back_button = tk.Button(push_page, image=back_photo, bg="#F1EFE7", borderwidth=0, highlightthickness=0, command=lambda: (previous_button_click(), show_previous_label()))
            back_button.image = back_photo
            back_button.place(relx=0.05, rely=0.91, anchor=tk.W)
            
                

            

            
            

        def pull():
            global gif_index
            global image_frame_list_resized
            main_page.withdraw()
                
            pull_page = tk.Toplevel(root)
            pull_page.geometry("500x500")
            pull_page.configure(bg="#F1EFE7")
            
            def back():
                pull_page.destroy()
                main()
                
            #Load and resize the back image
            back_image = Image.open("images/buttons/back.png")
            back_image = back_image.resize((30,30))
            back_photo = ImageTk.PhotoImage(back_image)
    
            back_button = tk.Button(pull_page, image=back_photo, bg="#F1EFE7", borderwidth=0, highlightthickness=0, command=back)
            back_button.image = back_photo
            back_button.place(relx=0.05, rely=0.1, anchor=tk.SW)
    
           
            # Function to load and prepare the GIF frames for animation
            def load_gif_frames(gif_path):
                frames = Image.open(gif_path)
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
                return [ImageTk.PhotoImage(frame.resize((new_width, new_height))) for frame in ImageSequence.Iterator(frames)]

    

            def next_button_click():
                global gif_index, image_frame_list_resized, count, replay

                if gif_index == len(gif_paths) - 1:
                    #If gif_index is already at the last GIF, do nothing and return
                    return

                gif_index += 1# Increment gif_index to display the next GIF
                gif_path = gif_paths[gif_index]

                #Load and prepare the GIF frames for animation
                image_frame_list_resized = load_gif_frames(gif_path)

                #Reset the count and replay flag
                count = 0
                replay = False
                
            def previous_button_click():
                global gif_index, image_frame_list_resized, count, replay

                if gif_index == 0:
                    #If gif_index is already at the first GIF, do nothing and return
                    return

                gif_index -= 1  #Decrement gif_index to display the next GIF
                gif_path = gif_paths[gif_index]

                #Load and prepare the GIF frames for animation
                image_frame_list_resized = load_gif_frames(gif_path)

                #Reset the count and replay flag
                count = 0
                replay = False

                
            # Function to animate the resized frames of the GIF
            def main_animation(count):
                global image_frame_list_resized
                im = image_frame_list_resized[count]

                gif_label.configure(image=im)  # Updates the image displayed in the label "gif_label"
                count += 1

                if count < len(image_frame_list_resized):  # Check if there are more frames to display
                    root.after(50, lambda: main_animation(count))  # Schedule the next frame update after 50 milliseconds

            
            latpulldownlogo_image = Image.open("images/statements/latpulldownlogo.png")
            latpulldownlogo_image = latpulldownlogo_image.resize((250, 60))
            latpulldownlogo_photo = ImageTk.PhotoImage(latpulldownlogo_image)
            
            latpulldownlogo_label = tk.Label(pull_page, image=latpulldownlogo_photo, bg="#F1EFE7")
            latpulldownlogo_label.image = latpulldownlogo_photo
            latpulldownlogo_label.place(relx=0.5, rely=0.08, anchor=tk.CENTER)
            
            latpulldowninfo_image = Image.open("images/statements/latpulldowninfo.png")
            latpulldowninfo_image = latpulldowninfo_image.resize((250, 260))
            latpulldowninfo_photo = ImageTk.PhotoImage(latpulldowninfo_image)
            
            latpulldowninfo_label = tk.Label(pull_page, image=latpulldowninfo_photo, bg="#F1EFE7")
            latpulldowninfo_label.image = latpulldowninfo_photo
            latpulldowninfo_label.place(relx=1, rely=0.5, anchor=tk.E)
            
            
            rowlogo_image = Image.open("images/statements/rowlogo.png")
            rowlogo_image = rowlogo_image.resize((250, 60))
            rowlogo_photo = ImageTk.PhotoImage(rowlogo_image)
            
            rowlogo_label = tk.Label(pull_page, image=rowlogo_photo, bg="#F1EFE7")
            rowlogo_label.image = rowlogo_photo
        
            rowinfo_image = Image.open("images/statements/rowinfo.png")
            rowinfo_image = rowinfo_image.resize((250, 260))
            rowinfo_photo = ImageTk.PhotoImage(rowinfo_image)
            
            rowinfo_label = tk.Label(pull_page, image=rowinfo_photo, bg="#F1EFE7")
            rowinfo_label.image = rowinfo_photo
            
            
            barbelllogo_image = Image.open("images/statements/barbelllogo.png")
            barbelllogo_image = barbelllogo_image.resize((250, 60))
            barbelllogo_photo = ImageTk.PhotoImage(barbelllogo_image)
            
            barbelllogo_label = tk.Label(pull_page, image=barbelllogo_photo, bg="#F1EFE7")
            barbelllogo_label.image = barbelllogo_photo
        
            barbellinfo_image = Image.open("images/statements/barbellinfo.png")
            barbellinfo_image = barbellinfo_image.resize((250, 260))
            barbellinfo_photo = ImageTk.PhotoImage(barbellinfo_image)
            
            barbellinfo_label = tk.Label(pull_page, image=barbellinfo_photo, bg="#F1EFE7")
            barbellinfo_label.image = barbellinfo_photo
            
            
            hammercurllogo_image = Image.open("images/statements/hammercurllogo.png")
            hammercurllogo_image = hammercurllogo_image.resize((250, 60))
            hammercurllogo_photo = ImageTk.PhotoImage(hammercurllogo_image)
            
            hammercurllogo_label = tk.Label(pull_page, image=hammercurllogo_photo, bg="#F1EFE7")
            hammercurllogo_label.image = hammercurllogo_photo
        
            hammercurlinfo_image = Image.open("images/statements/hammercurlinfo.png")
            hammercurlinfo_image = hammercurlinfo_image.resize((250, 260))
            hammercurlinfo_photo = ImageTk.PhotoImage(hammercurlinfo_image)
            
            hammercurlinfo_label = tk.Label(pull_page, image=hammercurlinfo_photo, bg="#F1EFE7")
            hammercurlinfo_label.image = hammercurlinfo_photo
           
           
           
           
           
           
           
            # Creates a label widget to display the animated GIF
            gif_label = tk.Label(pull_page, image="")
            gif_label.place(relx=0.25, rely=0.38, anchor=tk.CENTER)

            # Initialize the gif_index and load the first GIF
            gif_paths = ["images/gifs/pull/latpulldown.gif", "images/gifs/pull/row.gif", "images/gifs/pull/barbellcurl.gif", "images/gifs/pull/hammercurl.gif"]  # Add more paths as needed
            gif_index = 0
            image_frame_list_resized = load_gif_frames(gif_paths[gif_index])
            
            
            # List of labels to be shown in sequence
            labels_to_show = [latpulldownlogo_label, rowlogo_label, barbelllogo_label, hammercurllogo_label]  # Add more labels if needed
            info_to_show= [latpulldowninfo_label, rowinfo_label, barbellinfo_label, hammercurlinfo_label]
            current_label_index = 0  # Index to keep track of the currently displayed label
            current_info_index = 0


            # Function to handle the next button click
            def show_next_label():
                nonlocal current_label_index
                nonlocal current_info_index
    
                if current_label_index == len(labels_to_show) - 1:
                    # If we reached the last label, do nothing and return
                    return

                current_label = labels_to_show[current_label_index]
                current_info = info_to_show[current_info_index]
                current_label.place_forget()  # Hide the previous label
                current_info.place_forget()
    
                current_label_index += 1
                current_info_index += 1
    
                next_label = labels_to_show[current_label_index]  # Get the next label to show
                next_info = info_to_show[current_info_index]
                next_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)  # Show the next label
                next_info.place(relx=1, rely=0.5, anchor=tk.E)
                
           # Function to handle the previous button click
            def show_previous_label():
                nonlocal current_label_index
                nonlocal current_info_index
    
                if current_label_index == 0:
                    # If we reached the first label, do nothing and return
                    return
    
                current_label = labels_to_show[current_label_index]
                current_info = info_to_show[current_info_index]
                current_label.place_forget()  # Hide the current label
                current_info.place_forget()
    
                current_label_index -= 1
                current_info_index -= 1

                previous_label = labels_to_show[current_label_index]  # Get the previous label to show
                previous_info = info_to_show[current_info_index]
                previous_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)  # Show the previous label
                previous_info.place(relx=1, rely=0.5, anchor=tk.E)
                    
            #Load and resize the next image
            next_image = Image.open("images/buttons/next.png")
            next_image = next_image.resize((30, 30))
            next_photo = ImageTk.PhotoImage(next_image)

            #Creates a button widget
            next_button = tk.Button(pull_page, image=next_photo, bg="#F1EFE7", borderwidth=0, highlightthickness=0, command=lambda: (show_next_label(), next_button_click()))
            next_button.image = next_photo
            next_button.place(relx=0.95, rely=0.95, anchor=tk.SE)  
            
            start_image = Image.open("images/buttons/button.png")
            start_image = start_image.resize((200, 50))
            start_photo = ImageTk.PhotoImage(start_image)

            start_button = tk.Button(pull_page, image=start_photo, bg="#F1EFE7", borderwidth=0, highlightthickness=0, command=lambda: main_animation(0))
            start_button.image = start_photo
            start_button.place(relx=0.25, rely=0.7, anchor=tk.S)
            
            #Load and resize the back image
            back_image = Image.open("images/buttons/back.png")
            back_image = back_image.resize((30,30))
            back_photo = ImageTk.PhotoImage(back_image)
    
            back_button = tk.Button(pull_page, image=back_photo, bg="#F1EFE7", borderwidth=0, highlightthickness=0, command=lambda: (previous_button_click(), show_previous_label()))
            back_button.image = back_photo
            back_button.place(relx=0.05, rely=0.91, anchor=tk.W)
            
            
                
        def legs():
            push_button.place_forget()
            push2_label.place_forget()
            pull_button.place_forget()
            pull2_label.place_forget()
            legs_button.place_forget()
            legs2_label.place_forget()
            choice_label.place_forget()
            
            def restore():
                back_button.place_forget()
                push_button.place(relx=0.05, rely=0.05, anchor=tk.NW)
                push2_label.place(relx=0.05, rely=0.2, anchor=tk.W)
                pull_button.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
                pull2_label.place(relx=0.5, rely=0.195, anchor=tk.CENTER)
                legs_button.place(relx=0.95, rely=0.04, anchor=tk.NE)
                legs2_label.place(relx=0.95, rely=0.215, anchor=tk.E)
                choice_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
                
            #Load and resize the back image
            back_image = Image.open("images/buttons/back.png")
            back_image = back_image.resize((30,30))
            back_photo = ImageTk.PhotoImage(back_image)
    
            back_button = tk.Button(main_page, image=back_photo, bg="#F1EFE7", borderwidth=0, highlightthickness=0, command=restore)
            back_button.image = back_photo
            back_button.place(relx=0.05, rely=0.1, anchor=tk.SW)
        
        
        
        #Load and resize the push image
        push_image = Image.open("images/buttons/push.png")
        push_image = push_image.resize((100, 50))
        push_photo = ImageTk.PhotoImage(push_image)

        #Creates a button widget
        push_button = tk.Button(main_page, image=push_photo, bg="#F1EFE7", borderwidth=0, highlightthickness=0, command=push)
        push_button.image = push_photo
        push_button.place(relx=0.05, rely=0.05, anchor=tk.NW)
        
        #Load and resize the push image
        push2_image = Image.open("images/statements/push2.png")
        push2_image = push2_image.resize((110, 60))
        push2_photo = ImageTk.PhotoImage(push2_image)

        #Creates a label widget
        push2_label = tk.Label(main_page, image=push2_photo, bg="#F1EFE7")
        push2_label.image = push2_photo
        push2_label.place(relx=0.05, rely=0.2, anchor=tk.W)
        
        #Load and resize the pull image
        pull_image = Image.open("images/buttons/pull.png")
        pull_image = pull_image.resize((100, 50))
        pull_photo = ImageTk.PhotoImage(pull_image)

        #Creates a button widget
        pull_button = tk.Button(main_page, image=pull_photo, bg="#F1EFE7", borderwidth=0, highlightthickness=0, command=pull)
        pull_button.image = pull_photo
        pull_button.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        
        # Load and resize the legs2 image
        pull2_image = Image.open("images/statements/pull2.png")
        pull2_image = pull2_image.resize((100, 50))
        pull2_photo = ImageTk.PhotoImage(pull2_image)

        # Creates an label image
        pull2_label = tk.Label(main_page, image=pull2_photo, bg="#F1EFE7")
        pull2_label.image = pull2_photo
        pull2_label.place(relx=0.5, rely=0.195, anchor=tk.CENTER)
        
        #Load and resize the leg image
        legs_image = Image.open("images/buttons/legs.png")
        legs_image = legs_image.resize((110, 60))
        legs_photo = ImageTk.PhotoImage(legs_image)

        #Creates a button widget
        legs_button = tk.Button(main_page, image=legs_photo, bg="#F1EFE7", borderwidth=0, highlightthickness=0, command=legs)
        legs_button.image = legs_photo
        legs_button.place(relx=0.95, rely=0.04, anchor=tk.NE)
        
        # Load and resize the legs2 image
        legs2_image = Image.open("images/statements/legs2.png")
        legs2_image = legs2_image.resize((120, 70))
        legs2_photo = ImageTk.PhotoImage(legs2_image)

        # Creates an label image
        legs2_label = tk.Label(main_page, image=legs2_photo, bg="#F1EFE7")
        legs2_label.image = legs2_photo
        legs2_label.place(relx=0.95, rely=0.215, anchor=tk.E)
        
        #Load and resize the image
        choice_image = Image.open("images/statements/choice.png")
        choice_image = choice_image.resize((450, 100))
        choice_photo = ImageTk.PhotoImage(choice_image)

        #Creates a label image
        choice_label = tk.Label(main_page, image=choice_photo, bg="#F1EFE7")
        choice_label.image = choice_photo
        choice_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        
        
        
        
        
        

    # Load and resize the intro image
    intro_image = Image.open("images/statements/intro.png")
    intro_image = intro_image.resize((300, 30))  # Resizes the image
    intro_photo = ImageTk.PhotoImage(intro_image)  # Creates a PhotoImage object from the resized image

    # Creates a label widget for the intro image and centers it at the top of the window
    intro_label = tk.Label(intro_page, image=intro_photo, bg="#F1EFE7")
    intro_label.image = intro_photo  # Store the PhotoImage object as an attribute of the label
    intro_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

    # Load and resize the welcoming image
    welcome_image = Image.open("images/statements/welcoming.png")
    welcome_image = welcome_image.resize((400, 400))
    welcome_photo = ImageTk.PhotoImage(welcome_image)

    # Creates an image that is the welcoming body text
    welcome_label = tk.Label(intro_page, image=welcome_photo, bg="#F1EFE7")
    welcome_label.image = welcome_photo

    # Load and resize the hypertrophy image
    hypertrophy_image = Image.open("images/statements/hypertrophy.png")
    hypertrophy_image = hypertrophy_image.resize((400, 400))
    hypertrophy_photo = ImageTk.PhotoImage(hypertrophy_image)

    # Creates an image that is the definition of hypertrophy
    hypertrophy_label = tk.Label(intro_page, image=hypertrophy_photo, bg="#F1EFE7")
    hypertrophy_label.image = hypertrophy_photo
    
    #Load and resize the definition image
    definition_image = Image.open("images/statements/definition.png")
    definition_image = definition_image.resize((400, 400))
    definition_photo = ImageTk.PhotoImage(definition_image)

    # Creates an image that is the definition
    definition_label = tk.Label(intro_page, image=definition_photo, bg="#F1EFE7")
    definition_label.image = definition_photo
    
    #Load and resize the muscle building image
    muscle_image = Image.open("images/statements/muscle.png")
    muscle_image = muscle_image.resize((400, 430))
    muscle_photo = ImageTk.PhotoImage(muscle_image)

    # Creates an image that is the muscle building image
    muscle_label = tk.Label(intro_page, image=muscle_photo, bg="#F1EFE7")
    muscle_label.image = muscle_photo

    #Load and resize the muscle1 building image
    muscle1_image = Image.open("images/statements/muscle1.png")
    muscle1_image = muscle1_image.resize((400, 430))
    muscle1_photo = ImageTk.PhotoImage(muscle1_image)
    
    # Creates an image that is the muscle building image
    muscle1_label = tk.Label(intro_page, image=muscle1_photo, bg="#F1EFE7")
    muscle1_label.image = muscle1_photo
    
    #Load and resize the image
    training_image = Image.open("images/statements/training.png")
    training_image = training_image.resize((400, 430))
    training_photo = ImageTk.PhotoImage(training_image)
    
    # Creates an image that is the explanation of training optimally
    training_label = tk.Label(intro_page, image=training_photo, bg="#F1EFE7")
    training_label.image = training_photo
    
    #Load and resize the image
    training1_image = Image.open("images/statements/training1.png")
    training1_image = training1_image.resize((400, 430))
    training1_photo = ImageTk.PhotoImage(training1_image)
    
    # Creates an image that is the explanation of training optimally
    training1_label = tk.Label(intro_page, image=training1_photo, bg="#F1EFE7")
    training1_label.image = training1_photo
    
    #Load and resize the image
    closing_image = Image.open("images/statements/closing.png")
    closing_image = closing_image.resize((400, 400))
    closing_photo = ImageTk.PhotoImage(closing_image)
    
    # Creates an image that is the closing statement
    closing_label = tk.Label(intro_page, image=closing_photo, bg="#F1EFE7")
    closing_label.image = closing_photo


    # List of labels to be shown in sequence
    labels_to_show = [intro_label, welcome_label, hypertrophy_label, definition_label, muscle_label, muscle1_label, training_label, training1_label, closing_label]  # Add more labels if needed
    current_label_index = 0  # Index to keep track of the currently displayed label

    # Function to handle the next button click
    def show_next_label():
        nonlocal current_label_index
        current_label = labels_to_show[current_label_index]
        current_label.pack_forget()  # Hide the previous label
        current_label_index += 1
        if current_label_index >= len(labels_to_show):
            current_label_index = 0
        next_label = labels_to_show[current_label_index]  # Get the next label to show
        next_label.pack()  # Show the next label
            
    # Function to handle the previous button click
    def show_previous_label():
        nonlocal current_label_index
        current_label = labels_to_show[current_label_index]
        current_label.pack_forget()  # Hide the current label
        current_label_index -= 1
        if current_label_index < 0:
            current_label_index = len(labels_to_show) - 1
        previous_label = labels_to_show[current_label_index]  # Get the previous label to show
        previous_label.pack()  # Show the previous label

    #Load and resize the back image
    back_image = Image.open("images/buttons/back.png")
    back_image = back_image.resize((30,30))
    back_photo = ImageTk.PhotoImage(back_image)
    
    back_button = tk.Button(intro_page, image=back_photo, bg="#F1EFE7", borderwidth=0, highlightthickness=0, command=show_previous_label)
    back_button.image = back_photo
    back_button.place(relx=0.05, rely=0.95, anchor=tk.SW)

    #Load and resize the next image
    next_image = Image.open("images/buttons/next.png")
    next_image = next_image.resize((30, 30))
    next_photo = ImageTk.PhotoImage(next_image)

    #Creates a button widget
    next_button = tk.Button(intro_page, image=next_photo, bg="#F1EFE7", borderwidth=0, highlightthickness=0, command=show_next_label)
    next_button.image = next_photo
    next_button.place(relx=0.95, rely=0.95, anchor=tk.SE)
    
    #Load and resize the skip image
    skip_image = Image.open("images/buttons/skip.png")
    skip_image = skip_image.resize((100, 30))
    skip_photo = ImageTk.PhotoImage(skip_image)
    
    skip_button = tk.Button(intro_page, image=skip_photo, bg="#F1EFE7", borderwidth=0, highlightthickness=0, command=main)
    skip_button.image = skip_photo
    skip_button.place(relx=0.5, rely=0.95, anchor=tk.S)

    #Pack the intro_label initially
    intro_label.pack()
    
    
    
#Start the main event loop to keep the GUI responsive
root.mainloop()
