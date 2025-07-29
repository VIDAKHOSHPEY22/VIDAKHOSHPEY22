import requests
from bs4 import BeautifulSoup
import re

USERNAME = "VIDAKHOSHPEY22"
README_PATH = "README.md"

def get_rank(username):
    url = "https://committers.top/iran"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.select("table tbody tr")
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 2:
            rank = cols[0].text.strip().replace("#", "")
            user = cols[1].text.strip().lower()
            if user == username.lower():
                return rank
    return None

def update_readme(rank):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    new_badge = f"![GitHub Rank](https://img.shields.io/badge/GitHub%20Rank-{rank}th%20in%20Iran-%237f3fbf?style=flat&logo=github&logoColor=white)"

    updated = re.sub(r"!\[GitHub Rank\]\(https:\/\/img\.shields\.io\/badge\/GitHub%20Rank-[^\)]*\)",
                     new_badge, content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated)

if __name__ == "__main__":
    rank = get_rank(USERNAME)
    if rank:
        print(f"Found rank: {rank}")
        update_readme(rank)
    else:
        print(f"User {USERNAME} not found on committers.top Iran list.")
