import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from pytube import YouTube
import os

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.geometry("520x320")
        self.root.resizable(False, False)
        self.root.title("YouTube Video Downloader")
        self.root.config(background="PaleGreen1")

        self.video_Link = StringVar()
        self.download_Path = StringVar()

        self.create_widgets()

    def create_widgets(self):
        head_label = Label(self.root, text="YouTube Video Downloader Using Tkinter",
                           padx=15, pady=15, font="SegoeUI 14", bg="palegreen1", fg="red")
        head_label.grid(row=1, column=1, pady=10, padx=5, columnspan=3)

        link_label = Label(self.root, text="YouTube link :", bg="salmon", pady=5, padx=5)
        link_label.grid(row=2, column=0, pady=5, padx=5)

        self.link_text = Entry(self.root, width=35, textvariable=self.video_Link, font="Arial 14")
        self.link_text.grid(row=2, column=1, pady=5, padx=5, columnspan=2)

        destination_label = Label(self.root, text="Destination :", bg="salmon", pady=5, padx=9)
        destination_label.grid(row=3, column=0, pady=5, padx=5)

        self.destination_text = Entry(self.root, width=27, textvariable=self.download_Path, font="Arial 14")
        self.destination_text.grid(row=3, column=1, pady=5, padx=5)

        browse_button = Button(self.root, text="Browse", command=self.browse, width=10, bg="bisque", relief=GROOVE)
        browse_button.grid(row=3, column=2, pady=1, padx=1)

        download_button = Button(self.root, text="Download Video", command=self.show_video_info, width=20, bg="thistle1",
                                 pady=10, padx=15, relief=GROOVE, font="Georgia, 13")
        download_button.grid(row=4, column=1, pady=20, padx=20)

        self.progress = ttk.Progressbar(self.root, orient=HORIZONTAL, length=500, mode='determinate')
        self.progress.grid(row=5, column=0, columnspan=3, pady=10, padx=10)

    def browse(self):
        download_directory = filedialog.askdirectory(initialdir=os.path.expanduser("~"), title="Save Video")
        self.download_Path.set(download_directory)

    def show_video_info(self):
        try:
            youtube_link = self.video_Link.get()
            if not youtube_link:
                messagebox.showerror("Error", "Please enter a YouTube link")
                return

            video = YouTube(youtube_link)
            video_info = f"Title: {video.title}\nDuration: {video.length // 60} minutes {video.length % 60} seconds\nAuthor: {video.author}"
            proceed = messagebox.askyesno("Video Information", f"{video_info}\n\nDo you want to download this video?")
            if proceed:
                self.download(video)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def download(self, video):
        try:
            download_folder = self.download_Path.get()
            if not download_folder:
                messagebox.showerror("Error", "Please select a download directory")
                return

            video_stream = video.streams.get_highest_resolution()

            if not os.access(download_folder, os.W_OK):
                messagebox.showerror("Error", "Cannot write to the selected directory. Please choose another directory.")
                return

            video_stream.download(download_folder)
            messagebox.showinfo("SUCCESSFULLY", "DOWNLOADED AND SAVED IN\n" + download_folder)
            self.progress['value'] = 0  # Reset progress bar after download
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def progress_callback(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        self.progress['value'] = percentage_of_completion
        self.root.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()
