from pySongStructure import process
import json

out = process('spirit.mp3', 44100)

outname = 'spirit.json'
print(outname)
with open(outname, 'w') as outfile:
    json.dump(out, outfile, indent=4)

