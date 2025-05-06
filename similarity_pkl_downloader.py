import urllib.request

url = "https://www.dropbox.com/scl/fi/1vjv6uh0evtc1ciybtz5o/similarity.pkl?rlkey=jdlzyskp5284l1gfpamx2lvtl&st=tidtg79h&dl=0"
output = "similarity.pkl"

urllib.request.urlretrieve(url, output)
print("Download completed.")
