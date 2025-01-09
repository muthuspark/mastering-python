API_KEY = "your_secret_api_key"

import os
API_KEY = os.environ.get("API_KEY")
if API_KEY is None:
    raise ValueError("API_KEY environment variable not set")