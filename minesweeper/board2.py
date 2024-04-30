import tkinter as tk
from PIL import Image, ImageTk



def update_image(event):
    # Get the index of the clicked image
    index = event.widget.index
    # Update the image based on the index
    img = Image.open(image_paths[1])  # Load the new image
    img.thumbnail((100, 100))  # Resize the image if needed
    photo = ImageTk.PhotoImage(img)  # Convert image to Tkinter format
    labels[index].configure(image=photo)  # Update the image on the label
    labels[index].image = photo  # Keep a reference to avoid garbage collection

# Paths to the images
image_paths = ["images/flag.png", "images/empty-block.png", "images/wrong-flag.png", "images/unclicked-bomb.png"]

# Create tkinter window
root = tk.Tk()
root.title("Image Grid")

# Create labels to display images
labels = []
for i, path in enumerate(image_paths):
    img = Image.open(path)
    img.thumbnail((100, 100))  # Resize the image if needed
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.index = i  # Store the index of the image
    label.bind("<Button-1>", update_image)  # Bind click event
    label.photo = photo  # Keep a reference to avoid garbage collection
    label.grid(row=i // 2 , column=i % 2)
    labels.append(label)

root.mainloop()