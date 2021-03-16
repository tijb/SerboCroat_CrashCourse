"""
  Formats the files in a given directory into teh Ankikun iPhone format.
  Copies the existing files, does not overwrite.

  USAGE
  python3 ./AnkikunFormat.py [source directory]
"""
from sys import argv, exit
from os import scandir

if len(argv) <= 1:
  print("ERR: Missing the file source directory.")
  exit(1)

print(" - Checking", argv[1])
print(" - Converting Files")
with scandir(argv[1]) as file_names:
  for file_name in file_names:
    with open(f"{argv[1]}/{file_name.name}", 'r') as f:
      content = f.read()

    # our CSV files are 2 fields.
    # Ankikun uses the second field as a "pronunciation" field.
    # we dont have a Cyrillic/Latin translation, so this will just
    # leave that field blank in the new files, so that Ankikun doesn't
    # crash.
    content.replace(',',',,')

    new_filename = file_name.name.replace('.csv',' iPhone.csv')
    print("\t", new_filename)
    with open(new_filename, 'x') as f:
      f.write(content)


