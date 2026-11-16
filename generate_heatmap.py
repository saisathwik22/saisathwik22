"""Generate GitHub-style contribution heatmaps (dark + light SVG) for a profile README."""
import json, os, sys, random, urllib.request
from datetime import date

USER = os.environ.get("GH_USER", "saisathwik22")
TOKEN = os.environ.get("GH_TOKEN", "")
OUT = os.path.join(os.path.dirname(__file__), "..", "assets")

QUERY = """query($login:String!){user(login:$login){contributionsCollection{contributionCalendar{
totalContributions weeks{contributionDays{date contributionLevel}}}}}}"""
LEVELS = {"NONE": 0, "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2, "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4}

THEMES = {
    "dark":  {"colors": ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"], "text": "#8b949e"},
    "light": {"colors": ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"], "text": "#57606a"},
}
CELL, GAP, LEFT, TOP = 11, 3, 32, 22
MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]


def fetch():
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": USER}}).encode(),
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"},
    )
    data = json.load(urllib.request.urlopen(req))
    cal = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    weeks = [[(d["date"], LEVELS[d["contributionLevel"]]) for d in w["contributionDays"]] for w in cal["weeks"]]
    return weeks, cal["totalContributions"]


def demo():
    random.seed(1)
    weeks, d0 = [], date(2025, 11, 16).toordinal()
    for w in range(53):
        days = []
        for i in range(7):
            dt = date.fromordinal(d0 + w * 7 + i - 7 * 0)
            days.append((dt.isoformat(), random.choice([0, 0, 0, 1, 1, 2, 3, 4])))
        weeks.append(days)
    return weeks, 412


def render(weeks, total, theme):
    t = THEMES[theme]
    width = LEFT + len(weeks) * (CELL + GAP) + 10
    height = TOP + 7 * (CELL + GAP) + 28
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="10">']
    last_month = -1
    for x, week in enumerate(weeks):
        m = int(week[0][0][5:7]) - 1
        if m != last_month:
            if x == 0 or x * (CELL + GAP) - 0 > 0:
                p.append(f'<text x="{LEFT + x * (CELL + GAP)}" y="12" fill="{t["text"]}">{MONTHS[m]}</text>')
            last_month = m
        for y, (_, lvl) in enumerate(week):
            p.append(f'<rect x="{LEFT + x * (CELL + GAP)}" y="{TOP + y * (CELL + GAP)}" width="{CELL}" height="{CELL}" rx="2" fill="{t["colors"][lvl]}"/>')
    for label, row in (("Mon", 1), ("Wed", 3), ("Fri", 5)):
        p.append(f'<text x="0" y="{TOP + row * (CELL + GAP) + 9}" fill="{t["text"]}">{label}</text>')
    ly = TOP + 7 * (CELL + GAP) + 16
    p.append(f'<text x="{LEFT}" y="{ly + 9}" fill="{t["text"]}">{total} contributions in the last year</text>')
    lx = width - 10 - 5 * (CELL + 3) - 60
    p.append(f'<text x="{lx}" y="{ly + 9}" fill="{t["text"]}">Less</text>')
    for i, c in enumerate(t["colors"]):
        p.append(f'<rect x="{lx + 28 + i * (CELL + 3)}" y="{ly}" width="{CELL}" height="{CELL}" rx="2" fill="{c}"/>')
    p.append(f'<text x="{lx + 28 + 5 * (CELL + 3) + 2}" y="{ly + 9}" fill="{t["text"]}">More</text>')
    p.append("</svg>")
    return "\n".join(p)


if __name__ == "__main__":
    weeks, total = demo() if "--demo" in sys.argv else fetch()
    os.makedirs(OUT, exist_ok=True)
    for theme in THEMES:
        with open(os.path.join(OUT, f"contributions-{theme}.svg"), "w") as f:
            f.write(render(weeks, total, theme))
    print("done", total)
