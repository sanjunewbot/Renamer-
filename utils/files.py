import os
import uuid


def temp_name(filename):
    ext = os.path.splitext(filename)[1]
    return f"{uuid.uuid4().hex}{ext}"


def safe_remove(path):
    try:
        if os.path.exists(path):
            os.remove(path)
    except:
        pass
