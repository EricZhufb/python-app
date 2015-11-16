#
import sys
import csv
import json
lines = []
if len(sys.argv) != 3:
    sys.exit('Usage: args must contains input file and output file...')
jsonf = sys.argv[1]
csvf = sys.argv[2]
with open(jsonf) as f:
    lines = f.readlines()
with open(csvf,'wb') as csvfile:
    writer = None
    for line in lines:
        d = json.loads(line.decode('utf-8'))
        if writer == None:
            fields = []
            for k,v in d.items():
               fields.append(k)
            writer = csv.DictWriter(csvfile,fieldnames=fields)
            writer.writeheader()
        nd = {}
        for k,v in d.items():
            if type(v) == unicode:
                v = v.encode('utf8')
            nd[k] = v
        writer.writerow(nd)
