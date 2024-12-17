import os
import shutil
import tempfile
from foldersync.core import sync_directories


def test_sync_directories():
    with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as dst:
        # Create a file in src
        src_file = os.path.join(src, "hello.txt")
        with open(src_file, "w", encoding="utf-8") as f:
            f.write("Hello")

        # Run sync
        sync_directories(src, dst)

        # Check that file exists in dst
        dst_file = os.path.join(dst, "hello.txt")
        assert os.path.exists(dst_file), "File was not copied to destination."
