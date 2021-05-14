import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper2

save_url = [
    ["save_folder", "url"],
    ["save_folder", "url"],
    ["save_folder", "url"],
    ["save_folder", "url"],
]
"save_folder" = "./data/"

# Optional argument `save_subfolder` allows saving in a subfolder
opendata_scraper2(save_url, save_folder, sleep_time=1)
