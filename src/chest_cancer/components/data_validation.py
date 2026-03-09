import os

class DataValidation:
    def __init__(self, config):
        self.config = config
    
    def validate_dataset(self):
        train_path = os.path.join(self.config.data_dir, "train")
        test_path = os.path.join(self.config.data_dir, "test")
        valid_path = os.path.join(self.config.data_dir, "valid")
        
        status = True

        if not os.path.exists(train_path):
            status = False
        if not os.path.exists(test_path):
            status = False
        if not os.path.exists(valid_path):
            status = False
        
        os.makedirs(self.config.root_dir, exist_ok=True)

        with open(self.config.status_file, "w") as f:
            f.write(f"Validation status: {status}")