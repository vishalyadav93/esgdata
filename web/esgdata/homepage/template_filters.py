import os
from app import app

@app.template_filter('basename')
def get_basename(filepath):
    return os.path.basename(filepath)
