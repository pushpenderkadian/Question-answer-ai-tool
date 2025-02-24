import requests
from fastapi import HTTPException
from bs4 import BeautifulSoup


def extract_text(urls):
    combined_text = ""
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            page_text = ' '.join([p.get_text() for p in soup.find_all(['p', 'h1', 'h2', 'h3','h4','h5','h6', 'li'])])
            combined_text += page_text + " "
        except requests.RequestException as e:
            print(f"Failed to fetch {url}: {str(e)}")
            raise HTTPException(status_code=400, detail=f"Failed to fetch {url}: {str(e)}")
    combined_text = combined_text.strip().replace("\n", " ")
    return combined_text
