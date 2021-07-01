import argparse
import json
import tabulate

# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-r', '--report')
args = parser.parse_args()


headers = [
            r'time', 
            r'temp. max',
            r'temp. min',
          ]

with open(args.report) as report_file:
    report = json.load(report_file)


lines = [[time, temps[0], temps[1]] for time, temps in report.items()]

table = tabulate.tabulate(
        lines,
        headers=headers,
        tablefmt='latex_booktabs',
        floatfmt=('.1f', '.1f', '.1f'),
        colalign=('center', 'center', 'center'),
    )

print(table)
