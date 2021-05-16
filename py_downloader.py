# create youtube download with library pafy
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
from threading import *
import pafy

FolderName = ''
fileSizeInBytes = 0
MaxFileSize = 0

# fucn Lokasi Folder Download
def openDirectory():
    global FolderName
    FolderName = filedialog.askdirectory()
    if (len(FolderName) > 1):
        fileLocationLabelError.config(text=FolderName,fg="green")

    else:
        fileLocationLabelError.config(text="Please choose folder!",fg="red")

# fucn perincian kontent video
def detail_vid():
    yt = youtubeEntry.get()
    videos = pafy.new(yt)
    youtubeEntryError.config(text=videos,fg="green")

# fucn download video
def downloadVid():
    yt = youtubeEntry.get()
    videos = pafy.new(yt)

    print(videos.title)
    stream = videos.streams
    for i in stream:
        data = "{} {}".format(i.resolution, i.extension)
        print(data)

    fix_dwn = videos.getbest(preftype="mp4",ftypestrict=True)
    print("Resolusinya = ", fix_dwn.resolution, fix_dwn.extension)
    iwan = fix_dwn.download(FolderName,quiet=True)

# Tkinter Windows
root = Tk()
root.title("Create By Iwn.exe")
# ===============contents strech ac to windows strech====
root.grid_columnconfigure(0, weight=1)  # strech things Horiontally
# =============youtube link label=================
youtubeLinkLabel = Label(root,text="Masukan Link Youtubee ", fg="blue", font=("Agency FB", 20))
youtubeLinkLabel.grid()

# Membuat entry link youtube + tombol
youtubeEntryVar = StringVar()
youtubeEntry = Entry(root, width=50, textvariable=youtubeEntryVar)
youtubeEntry.grid()
entry_but = Button(root, width=20, bg="green", fg="white",text="Ok", font=("Arial", 10),command=detail_vid)
entry_but.grid()

# ketika link error
youtubeEntryError = Label(root, fg="red", text="", font=("Times New Roman", 10))
youtubeEntryError.grid(pady=(0, 5))

# tombol untuk memilih tempat penyimpanan
SaveLabel = Label(root, text="Pilih tempat penyimpanan : ", fg="blue", font=("Agency FB", 20, "bold"))
SaveLabel.grid()

# memilih tempat penyimpanan
SaveEntry = Button(root, width=20, bg="green", fg="white", text="Pilih Folder", font=("Arial", 10), command=openDirectory)
SaveEntry.grid()

# jika tidak memilih tempat penyimpanan, akan eror
fileLocationLabelError = Label(root,  text="", font=("Agency FB", 20))
fileLocationLabelError.grid(pady=(0, 0))

# tombol download
downloadButton = Button(root, text="Download", fg="white", width=15, bg="green", command=downloadVid)
downloadButton.grid(pady=(20, 20))

root.mainloop()
