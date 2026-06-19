import json
import argparse
import sys
from config import INPUT


parser = argparse.ArgumentParser(description="Analysiert health_report.json")

parser.add_argument(
    "--output",
    help="Überschreibt Default-Ausgabepfad"
)

parser.add_argument(
    "--status",
    type=int,
    choices=[404, 500, 200],
    help="zeigt Anzahl der Services mit Status-Code"
)

parser.add_argument(
    "--strict",
    action="store_true"
)

args = parser.parse_args()

# OUTPUT definieren (Fallback auf INPUT wenn nicht gesetzt)
OUTPUT = args.output if args.output is not None else "report.json"


# -------------------------
# INPUT laden
# -------------------------
with open(INPUT, "r") as f:
    services = json.load(f)


# -------------------------
# Report Basis
# -------------------------
pythonreport = {
    "gesamt": 0,
    "gesund": 0,
    "ungesund": 0,
    "nach_status": {"200": 0, "404": 0, "500": 0},
    "langsamste": None,
    "ungesunde_services": []
}


# -------------------------
# Report Berechnung
# -------------------------
def reportmerger(data):
    report = pythonreport.copy()

    report["gesamt"] = len(data)

    langsamstes = max(data, key=lambda x: x["responetime"])
    report["langsamste"] = langsamstes

    for service in data:
        # Health
        if service["gesund"]:
            report["gesund"] += 1
        else:
            report["ungesund"] += 1
            report["ungesunde_services"].append(service["name"])

        # Status
        status = str(service["status"])
        if status in report["nach_status"]:
            report["nach_status"][status] += 1

    return report


# -------------------------
# Report erstellen
# -------------------------
final_report = reportmerger(services)


# -------------------------
# OUTPUT schreiben
# -------------------------
with open(OUTPUT, "w") as f:
    json.dump(final_report, f, indent=4)


# -------------------------
# Status Ausgabe
# -------------------------
def args_status(status, file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data["nach_status"].get(str(status), 0)


if args.status is not None:
    print(args_status(args.status, OUTPUT))


# -------------------------
# Strict Mode Exit
# -------------------------
def opener(file_path):
    with open(file_path) as f:
        data = json.load(f)

    if args.strict and data["ungesund"] > 2:
        print("sys.exit(1)")
        sys.exit(1)

    print("sys.exit(0)")
    sys.exit(0)


opener(OUTPUT)