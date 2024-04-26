import os
import sys
import json

# Append the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

# Additional imports
from unittest.mock import patch, MagicMock
import pytest

import pandas as pd

from io import StringIO