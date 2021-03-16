"""
  Splits the a given file into individual files of a given size.

  USAGE:
  python3 ./SplitFiles.py [file name] [lines per file] [output file name]
"""
from sys import argv, exit
from math import ceil

if len(argv) <= 1:
  print("ERR: Missing first argument. Path to file to split.")
  exit(1)
if len(argv) <= 2:
  print("ERR: Missing second argument. Number of lines per file.")
  exit(1)
if len(argv) <= 3:
  print("ERR: Missing output file name prefix.")
  exit(1)

files = dict()
fp = 0

print(" - parsing file", argv[1])
with open(argv[1], 'r') as f:
  lines = list(f)

print(" - file has", len(lines), "lines.")
print(" - splitting by", argv[2], "will result in", ceil(len(lines) / int(argv[2])), "files")
print(" - writing files")
for i, line in enumerate(lines):
  cur_val = files[fp] if fp in files else list()
  cur_val.append(line)
  files[fp] = cur_val
  if len(cur_val) > 19:
    name = f'{fp:03} {argv[3]}.csv'
    print("\t", name)
    with open(name, 'x') as f:
      f.write(''.join(cur_val))
    fp += 1
