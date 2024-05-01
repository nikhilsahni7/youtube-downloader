# YouTube Downloader

A simple and modern GUI application built with Python and tkinter for downloading YouTube videos. This application allows you to download videos from YouTube by entering the video URL and specifying the save directory. It also displays video information such as title and length, and shows a progress bar during the download process.

## Features

- Modern and sleek user interface
- Video title and length display
- Download progress bar
- Save directory selection via file dialog
- Error handling and status messages

## Requirements

- Python 3.x
- pytube library (`pip install pytube`)
- tkinter library (`pip install tkinter`)

## Usage

1. Clone or download the repository.
2. Install the required dependencies by running `pip install pytube`.
3. Run the `main.py` file.
4. Enter the YouTube video URL in the provided text field.
5. Click the "Browse" button to select the save directory for the downloaded video.
6. Click the "Download" button to start the download process.
7. The video title, length, and download progress will be displayed.
8. Upon successful download, a success message will be shown.

## Code Overview

The application is built using the tkinter library for creating the GUI and the pytube library for interacting with the YouTube API. The main class `YouTubeDownloader` is a subclass of `tk.Tk` and contains the following methods:

- `__init__`: Initializes the GUI components, including the URL entry, video information display, save directory entry, progress bar, and download button.
- `open_file_dialog`: Opens a file dialog for selecting the save directory.
- `download_video`: Downloads the video from the provided URL and saves it to the specified directory. It also updates the video information and progress bar.
- `update_video_info`: Displays the video title and length in the GUI.
- `on_progress`: Callback function for updating the progress bar during the download process.

The application is modular and easy to understand, with each component separated into individual methods for better code organization and maintainability.

## License

This project is licensed under the [MIT License](LICENSE).
