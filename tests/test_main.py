import sys
import os

sys.path.append(os.path.abspath("src"))

from main import hello

def test_hello():
    assert hello() == "Hello World"