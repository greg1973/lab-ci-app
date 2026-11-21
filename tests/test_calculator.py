import sys
import os

sys.path.append(os.path.abspath("src"))

from calculator import add

def test_add():
    assert add(2, 3) == 5