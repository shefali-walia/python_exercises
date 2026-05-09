""" To read ZIP files and download them directly from the web, use the following three libraries: requests, zipfile, and io.

requests … send and receive data from Web
zipfile … reads abd writes ZIP files
io … reads and writes files """

import requests, zipfile, io
from io import StringIO

url = 'https://github.com/Hernan4444/MyAnimeList-Database/archive/refs/heads/master.zip'
r = requests.get(url, stream = True)  # stream = true mean don't download immediately, wait till I ask for data (to save memory)
z = zipfile.ZipFile(io.BytesIO(r.content))
"""r.content — the raw bytes of whatever was downloaded (the zip file, as a sequence of bytes)
io.BytesIO(r.content) — wraps those bytes into a fake file object. Normally ZipFile expects a file on disk, but BytesIO tricks it into thinking "here's a file" when it's actually just bytes sitting in RAM. No actual file is written to disk at this point.
zipfile.ZipFile(...) — opens that fake file as a zip archive, so Python can now read its contents, list files inside it, extract them, etc."""

#Imagine you downloaded a zip file but instead of saving it to your desktop, it's just floating in RAM. This line takes those floating bytes and says "treat this as a zip file" so Python can work with it.
#BytesIO is just a wrapper that makes RAM look like a file to Python.

z.extractall() # Or could also do z.extractall("/some/path") to extract to a specific folder
#Takes every file inside the zip and dumps it into the current working directory 