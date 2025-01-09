import sys
import os

module_path = os.path.abspath("path/to/your/module") # Replace with actual path
sys.path.append(module_path)

import my_module

my_module.my_function()