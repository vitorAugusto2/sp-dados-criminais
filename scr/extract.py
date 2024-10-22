import requests
import urllib3
from typing import List


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def download_data(url: List[str], path_output: str) -> None:
    print(f"Starting download of {url}")
    with requests.get(url, verify=False, stream=True) as resp:
        resp.raise_for_status()
        with open(path_output, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    print(f"File downloaded successfully: {path_output}")
