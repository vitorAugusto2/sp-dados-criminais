import requests
import urllib3
from typing import List

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def download_data(url: List[str], path_output: str, timeout: int = 120) -> None:
    print(f"Starting download of {url}")
    with requests.get(url, verify=False, stream=True, timeout=timeout) as resp:
        resp.raise_for_status()
        with open(path_output, "wb") as f:
            for chunk in resp.iter_content(chunk_size=65536):
                if chunk:
                    f.write(chunk)
    print(f"File downloaded successfully: {path_output}")
