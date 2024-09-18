import tkinter
import customtkinter
from yt_dlp import YoutubeDL

def startDownload():
    try:
        ytLink = link.get()
        ydl_opts = {
            'format': 'best',
            'progress_hooks': [on_progress_hook],
            'nocolor': True  # Disable colored output to avoid parsing issues
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([ytLink])
        finishLabel.configure(text="Download Complete!", text_color="green")
    except Exception as e:
        finishLabel.configure(text="Download Error: " + str(e), text_color="red")

def on_progress_hook(d):
    if d['status'] == 'downloading':
        percentage = d.get('_percent_str', '0%')
        clean_percentage = ''.join(c for c in percentage if c.isdigit() or c == '.').strip('%')
        progressPercentage.configure(text=clean_percentage + "%")
        progressBar.set(float(clean_percentage) / 100)

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert Youtube Video URL")
title.pack(padx=10, pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Dowloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress percentage
progressPercentage = customtkinter.CTkLabel(app, text="0%")
progressPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run App
app.mainloop()
