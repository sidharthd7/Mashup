import os

def ensure_directory_exists(path):
    """
    Ensures that the specified directory exists. Creates it if it doesn't exist.
    
    Args:
        path (str): Path to the directory.
    """
    if not os.path.exists(path):
        os.makedirs(path)

def validate_url(url):
    """
    Validates if the given URL seems to be a valid YouTube URL.
    
    Args:
        url (str): URL to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    # Simple validation (you may use regex for more complex checks)
    return url.startswith("https://www.youtube.com/") or url.startswith("https://youtu.be/")

def print_progress(current, total):
    """
    Prints a simple progress update.

    Args:
        current (int): Current step.
        total (int): Total number of steps.
    """
    print(f"Processing {current} out of {total}...")

