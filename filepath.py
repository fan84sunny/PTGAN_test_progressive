import os

MODEL_PATH="/models"

def modelpath_join(suffix_path):
    return os.path.join(MODEL_PATH, suffix_path)
