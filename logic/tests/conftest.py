import os

import pytest


@pytest.fixture
def remove_tmp_dir_after_test():
    path_to_tmp_dir = os.path.join(os.getcwd(), "tmp")
    try:
        if os.path.exists(path_to_tmp_dir):
            for root, dirs, files in os.walk(path_to_tmp_dir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(path_to_tmp_dir)
    except Exception as e:
        raise Exception(f"{e}")
