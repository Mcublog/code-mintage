import sys
from os.path import dirname, realpath
from pathlib import Path

sys.path.append(dirname(realpath(__file__)))
sys.path.append(f"{Path(__file__).resolve().parent}")
sys.path.append(f"{Path(__file__).resolve().parent.parent}")
