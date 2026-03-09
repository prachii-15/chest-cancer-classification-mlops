import os
import shutil

class DataIngestion:
    def __init__(self, config):
        self.config = config

    def copy_dataset(self):
        source = self.config.source_dir
        destination = self.config.root_dir

        os.makedirs(destination, exist_ok=True)

        shutil.copytree(
            source,
            destination,
            dirs_exist_ok=True
        )
