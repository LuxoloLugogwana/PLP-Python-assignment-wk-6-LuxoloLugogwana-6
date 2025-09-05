#!/usr/bin/env python3
"""
Image Fetcher - Downloads an image from a given URL and saves it to a specified directory
"""

import requests
import os
from urllib.parse import urlparse, unquote
from pathlib import Path
import mimetypes

def create_directory(directory_name):
    """Create directory for storing images with exist_ok=True"""
    try:
        os.makedirs(directory_name, exist_ok=True)
        print(f"✓ Directory '{directory_name}' is ready")
        return True
    except PermissionError:
        print("✗ Permission denied: Cannot create directory")
        return False
    except Exception as e:
        print(f"✗ Unexpected error creating directory: {e}")
        return False

def extract_filename(url, response):
    """Extract appropriate filename from URL or generate one"""
    # Try to get filename from Content-Disposition header
    content_disposition = response.headers.get('Content-Disposition', '')
    if 'filename=' in content_disposition:
        filename = content_disposition.split('filename=')[1].strip('"\'')
        return unquote(filename)

    # Try to get filename from URL path
    parsed_url = urlparse(url)
    path = parsed_url.path
    if path and '/' in path:
        filename = path.split('/')[-1]
        if filename and '.' in filename:
            return unquote(filename)

    # Generate filename based on content type
    content_type = response.headers.get('Content-Type', '').split(';')[0]
    extension = mimetypes.guess_extension(content_type) or '.bin'
    return f"image{extension}"

def download_image(url, directory):
    """Download image from URL and save to directory"""
    try:
        print(f"🔗 Connecting to: {url}")

        # Send request with timeout and headers to respect server
        headers = {
            'User-Agent': 'ImageFetcher/1.0 (Community Image Download Tool)'
        }
        response = requests.get(url, headers=headers, timeout=30)

        # Check for HTTP errors
        response.raise_for_status()

        # Extract or generate filename
        filename = extract_filename(url, response)
        filepath = os.path.join(directory, filename)

        # Save the image
        print(f"📥 Downloading image...")
        with open(filepath, 'wb') as file:
            file.write(response.content)

        # Get file size for user feedback
        file_size = os.path.getsize(filepath)
        print(f"✅ Successfully saved: {filename} ({file_size:,} bytes)")
        print(f"📁 Location: {os.path.abspath(filepath)}")
        return True

    except requests.exceptions.Timeout:
        print("✗ Connection timeout: The server took too long to respond")
    except requests.exceptions.ConnectionError:
        print("✗ Connection error: Could not connect to the server")
    except requests.exceptions.HTTPError as e:
        print(f"✗ HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"✗ Network error: {e}")
    except PermissionError:
        print("✗ Permission denied: Cannot write to file")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

    return False

def main():
    """Main function to download the specific image"""
    print("=" * 50)
    print("🌐 Image Fetcher - Download Specific Image")
    print("=" * 50)

    # The specific URL and directory requested
    url = "https://images.pexels.com/photos/32690481/pexels-photo-32690481.jpeg"
    directory = "walking-man"

    # Create directory for the image
    if not create_directory(directory):
        return

    # Download the image
    success = download_image(url, directory)

    if success:
        print("\n💫 Success! Image downloaded successfully")
    else:
        print("\n⚠️  Download failed. Please check the URL and try again")

if __name__ == "__main__":
    main()