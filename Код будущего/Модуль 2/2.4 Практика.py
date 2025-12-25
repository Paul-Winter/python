import os
import json
os.chdir("C:\\test")    #???
with open("report.json") as f:
    data = json.load(f)
    vulns = data["host"]["services"][0]["vulnerabilities"]
    print(vulns)