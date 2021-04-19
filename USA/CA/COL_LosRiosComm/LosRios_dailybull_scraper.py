import sys
import os
import configs
import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

p = Path(__file__).resolve().parents[3]
sys.path.insert(1, str(p))
from common.base_scrapers import crimegraphics_scraper


save_dir = "./data/daily_bulletin/"
data = []

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

crimegraphics_scraper(configs, save_dir)
