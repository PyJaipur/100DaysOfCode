import json
from collections import defaultdict

userlinks = {
    "arjoonn": "https://www.arjoonn.com",
    "shivank98": "https://github.com/Shivank98",
}

SEP = "--------------"
with open("README.md", "r") as fl:
    pre = fl.read().split(SEP)[0]

commits = defaultdict(set)
buf = {}
while True:
    try:
        line = input()
    except EOFError:
        break
    else:
        if line.startswith("commit"):
            buf["commit"] = line.split()[1]
        elif line.startswith("Author"):
            buf["author"] = line.split("Author:")[1]
        elif line.startswith("Date"):
            buf["year"] = line.split("Date:")[1].split()[-2]
            commits[buf["year"]].add(buf["author"])
            buf = {}
print(pre, "\n")
print(SEP, "\n")

for year, authors in sorted(commits.items(), key=lambda x: int(x[0]), reverse=True):
    print(f"\n## {year}\n")
    authors = [author.split("<")[0].strip().lower() for author in authors]
    last = ""
    for author in sorted(authors):
        if last and last in author:
            continue
        last = author
        if author in userlinks:
            author = f"[{author}]({userlinks[author]})"
        print(f"- {author}")
