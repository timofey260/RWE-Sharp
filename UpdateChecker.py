import urllib.request
import sys

"""
this is demo to update checker that tries to update all rwe# files(including drizzle at some point)
"""

url = "https://github.com/timofey260/RWE-Plus/releases/download/2.6.3/RWE+_linux_nodrizzle.zip"
print("Download start!")


def getit(v1: int, v2: int, v3: int):
	print(f"\rDownloaded {v1}/{round(v3/v2)} blocks, {round(v1*v2/1_048_576)}mb/{round(v3/1_048_576)}mb", end="")


# filename, headers = urllib.request.urlretrieve(url, filename="f:\\Desktop\\file.zip", reporthook=getit)
# print("Download complete!")
# print("Download file location: ", filename)
# print("Download headers: ", headers)