Image Fetcher
A Python script that downloads images from URLs and saves them to organized directories.

Features
Downloads images from any provided URL

Creates organized directories for image storage

Handles various error conditions gracefully

Extracts appropriate filenames from URLs or generates them

Provides clear feedback throughout the process

Installation
Ensure you have Python 3.6+ installed

Install the required dependency:

bash
pip install requests
Usage
Basic Usage
Run the script and provide a URL when prompted:

bash
python image_fetcher.py
Specific Image Download
The script can be modified to download a specific image to a custom directory by changing the url and directory variables in the main() function.

How It Works
The script prompts for a URL containing an image

Creates a directory (default: "Fetched_Images") if it doesn't exist

Downloads the image from the provided URL

Saves it to the directory with an appropriate filename

Handles errors gracefully with informative messages

Error Handling
The script handles various error conditions including:

Connection timeouts

HTTP errors (404, 500, etc.)

Permission issues

Invalid URLs

Network problems

Ubuntu Principles
This tool embodies several Ubuntu principles:

Community: Connects to the wider web to fetch resources

Respect: Handles errors gracefully without crashing

Sharing: Organizes images in directories for easy sharing

Practicality: Serves a real need for downloading and organizing images

Example
To download the walking man image to a "walking-man" directory:

python
# In the main() function:
url = "https://images.pexels.com/photos/32690481/pexels-photo-32690481.jpeg"
directory = "walking-man"
License
This project is open source and available under the MIT License.