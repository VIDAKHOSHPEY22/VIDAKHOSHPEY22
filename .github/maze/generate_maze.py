# maze/generate_maze.py

import os
import requests
import svgwrite
from datetime import datetime, timedelta

USERNAME = os.getenv("GITHUB_USERNAME", "VIDAKHOSHPEY22")

def fetch_contributions(username):
    url = f"https://github-contributions-api.deno.dev/{username}.json"
    res = requests.get(url)
    data = res.json()["contributions"]
    return data

def generate_svg(contributions, filename):
    dwg = svgwrite.Drawing(filename, size=("800px", "120px"))
    x = 10
    y = 10

    for week in contributions:
        for day in week:
            color = day["color"]
            dwg.add(dwg.rect(insert=(x, y), size=("10px", "10px"), fill=color))
            y += 12
        y = 10
        x += 12

    dwg.add(dwg.text("🐭 Start", insert=(10, 10), font_size="10px"))
    dwg.save()

if __name__ == "__main__":
    data = fetch_contributions(USERNAME)
    generate_svg(data, "dist/github-contribution-maze.svg")
