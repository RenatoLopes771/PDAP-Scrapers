import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper2

save_url = [
    ["pdrs/2016-2020/", "https://data.seattle.gov/resource/8fwq-jcnn.csv"],
]

save_folder = "./data/"

# Optional argument `sleep_time` should be set to the site's crawl-delay,
# which can be found in their robots.txt file_name, default time is 1
opendata_scraper2(save_url, save_folder, sleep_time=1, socrata=True)
