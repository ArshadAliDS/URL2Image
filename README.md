# Project Name: ImageDownloader
Description
ImageDownloader is a Python-based tool designed to download images from web links and save them to your local device. This script reads image URLs from a CSV file, downloads each image, and saves them with a structured filename in a specified directory. Additionally, it updates the CSV file with the download status of each image, allowing you to track which images have been successfully downloaded, skipped, or encountered an error during the process.

Features
Reads image URLs from a CSV file.
Downloads images and saves them with a specified filename format.
Skips downloading if the image already exists.
Updates the CSV file with the download status for each image.
Provides real-time feedback on the progress of the download process.
Requirements
Python 3.x
pandas
urllib
IPython