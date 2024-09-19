# Pytube - YouTube Video Downloader

Pytube is a simple YouTube video downloader built using Python. It provides a straightforward graphical interface for users to input a YouTube video URL and download the video in the best available format. The project was recently updated to use yt-dlp (a modern fork of youtube-dl), enhancing its performance and compatibility with YouTube.

## Features

-   Downloads videos in the best available format from YouTube
    
-   Displays a progress bar with percentage completion during the download
    
-   Simple and clean GUI built using tkinter and customtkinter
    
-   Error handling with user feedback if the download fails
    

## Dependencies

-   **yt-dlp:** A popular command-line utility that allows downloading videos from YouTube and other video sites.
    
-   **customtkinter:** A modern alternative to tkinter, providing customizable GUI elements.
    
-   **tkinter:** A standard Python library for GUI development.
    

## Installation

1.  Clone this repository:
    
	    git clone https://github.com/yourusername/pytube-downloader.git

2.  Install the required dependencies:
    
	    pip install yt-dlp customtkinter

3.  Run the application:
    
	    python pytube.py


## Usage

1.  Open the app.
    
2.  Paste the YouTube video URL in the input field.
    
3.  Click the "Download" button.
    
4.  The progress bar will show the percentage of download completion.
    
5.  Once the download is complete, a "Download Complete!" message will be displayed.
    

## Code Overview

The application uses yt-dlp to handle video downloads. A progress bar and percentage label keep users updated during the download process.

**Key functionality:**

-   **startDownload():** Initiates the video download using yt-dlp.
    
-   **on_progress_hook():** Updates the progress bar and percentage as the video is being downloaded.
    
-   **Error handling:** If any error occurs during the download, the user is notified via the GUI.
    

## Video Tutorial

This project was inspired by and built with the help of this tutorial: [YouTube Video Downloader](https://www.youtube.com/watch?v=NI9LXzo0UY0&list=LL&index=21v=NI9LXzo0UY0&list=LL&index=20).
