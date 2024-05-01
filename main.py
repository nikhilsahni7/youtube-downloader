import pytube
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class YouTubeDownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Downloader")
        self.geometry("600x400")
        self.configure(bg="#f2f2f2")

        
        self.url_frame = tk.Frame(self, bg="#f2f2f2")
        self.url_frame.pack(pady=10)
        self.url_label = tk.Label(self.url_frame, text="Enter YouTube URL:", bg="#f2f2f2")
        self.url_label.pack(side=tk.LEFT, padx=5)
        self.url_entry = tk.Entry(self.url_frame, width=50, font=("Arial", 12))
        self.url_entry.pack(side=tk.LEFT, padx=5)

    
        self.info_frame = tk.Frame(self, bg="#f2f2f2")
        self.info_frame.pack(pady=10)
        self.title_label = tk.Label(self.info_frame, text="Title:", bg="#f2f2f2", font=("Arial", 12, "bold"))
        self.title_label.pack(side=tk.LEFT, padx=5)
        self.title_value = tk.Label(self.info_frame, bg="#f2f2f2", font=("Arial", 12))
        self.title_value.pack(side=tk.LEFT, padx=5)
        self.length_label = tk.Label(self.info_frame, text="Length:", bg="#f2f2f2", font=("Arial", 12, "bold"))
        self.length_label.pack(side=tk.LEFT, padx=5)
        self.length_value = tk.Label(self.info_frame, bg="#f2f2f2", font=("Arial", 12))
        self.length_value.pack(side=tk.LEFT, padx=5)

        
        self.save_frame = tk.Frame(self, bg="#f2f2f2")
        self.save_frame.pack(pady=10)
        self.save_label = tk.Label(self.save_frame, text="Save Directory:", bg="#f2f2f2", font=("Arial", 12))
        self.save_label.pack(side=tk.LEFT, padx=5)
        self.save_entry = tk.Entry(self.save_frame, width=50, font=("Arial", 12))
        self.save_entry.pack(side=tk.LEFT, padx=5)
        self.browse_button = tk.Button(self.save_frame, text="Browse", command=self.open_file_dialog, bg="#4CAF50", fg="#ffffff", font=("Arial", 12))
        self.browse_button.pack(side=tk.LEFT, padx=5)

       
        self.progress_frame = tk.Frame(self, bg="#f2f2f2")
        self.progress_frame.pack(pady=10)
        self.progress_bar = ttk.Progressbar(self.progress_frame, mode="determinate", length=400)
        self.progress_bar.pack()

        
        self.download_button = tk.Button(self, text="Download", command=self.download_video, bg="#4CAF50", fg="#ffffff", font=("Arial", 14, "bold"), padx=20, pady=10)
        self.download_button.pack(pady=10)

        
        self.status_label = tk.Label(self, text="", bg="#f2f2f2", font=("Arial", 12))
        self.status_label.pack(pady=10)

    def open_file_dialog(self):
        folder = filedialog.askdirectory(initialdir="/home/nikhil-sahni/Downloads")
        if folder:
            self.save_entry.delete(0, tk.END)
            self.save_entry.insert(0, folder)

    def download_video(self):
        url = self.url_entry.get()
        save_dir = self.save_entry.get()

        if not url or not save_dir:
            messagebox.showerror("Error", "Please enter both URL and save directory")
            return

        try:
            yt = pytube.YouTube(url, on_progress_callback=self.on_progress)
            self.update_video_info(yt)
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=save_dir)
            self.status_label.config(text="Video downloaded successfully!", fg="green")
        except Exception as e:
            self.status_label.config(text=str(e), fg="red")

    def update_video_info(self, yt):
        self.title_value.config(text=yt.title)
        duration = yt.length
        hours = duration // 3600
        minutes = (duration % 3600) // 60
        seconds = duration % 60
        length_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.length_value.config(text=length_str)

    def on_progress(self, stream, chunk, bytes_remaining):
        total_bytes = stream.filesize
        bytes_downloaded = total_bytes - bytes_remaining
        progress = int(100 * bytes_downloaded / total_bytes)
        self.progress_bar["value"] = progress
        self.update_idletasks()

if __name__ == "__main__":
    app = YouTubeDownloader()
    app.mainloop()