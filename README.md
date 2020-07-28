# pySongStructure

## Overview
pySongStructure is a high-level package for analysing song structures. 

## Usage:

For getting a basic overview of the structure

```python
from structure_detection import process
import json

out = process('spirit.mp3', 44100, boundary_detection_id: str = "olda", label_detection_id: str = "scluster")

outname = 'spirit.json'
print(outname)
with open(outname, 'w') as outfile:
    json.dump(out, outfile, indent=4)

```

Other functions for getting more specific data:
```python
get_boundaries, # gets section boundary data and labels 
get_tempos, # gets estimated tempos for each section
get_clean_labels, # cleans labels from get_boundaries into a more readable format
get_section_beats, # gets section boundaries in terms of estimated beat numbers
get_structure_array, # formats basic overview of the structure in an array
```

## This library uses the MSAF Library for boundary detection and labeling
Nieto, O., Bello, J. P., Systematic Exploration Of Computational Music Structure Research. Proc. of the 17th International Society for Music Information Retrieval Conference (ISMIR). New York City, NY, USA, 2016 (PDF).