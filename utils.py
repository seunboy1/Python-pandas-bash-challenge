import os
import shutil
import subprocess

def unzip():

    # Target directory
    extract_dir = "assets/file"

    # Remove directory
    if os.path.exists(extract_dir):
        shutil.rmtree(extract_dir)
    
    # Format of archive file
    archive_format = "zip"
    
    # Unpack the archive file
    shutil.unpack_archive("assets/file.zip", extract_dir, archive_format)


def run_shell():
    subprocess.call(['sh', './script.sh'])