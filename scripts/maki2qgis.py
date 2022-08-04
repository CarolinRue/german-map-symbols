#!/usr/bin/env python3

# Converter script for maki symols to QGIS SVG symbols

import os
import re
import shutil

source_path = "maki-symbols"
output_path = "qgis-symbols"
qgis_param = 'fill="param(fill)" fill-opacity="param(fill-opacity)" stroke="param(outline)" stroke-opacity="param(outline-opacity)" stroke-width="param(outline-width)"'

# clean output dir

for f in os.listdir(output_path):
    if not f.endswith(".svg"):
        continue
    os.remove(os.path.join(output_path, f))

# copy new files
for f in os.listdir(source_path):
    print(f)
    shutil.copy2(os.path.join(source_path, f), os.path.join(output_path, f))

    # open file
    with open (os.path.join(output_path, f), "r+") as file:
        fcontent = file.read()
        file.seek(0)

        #replace style in SVG
        output = re.sub('style="[^"]*"', qgis_param, fcontent)
        file.write(output)
        file.truncate()

    

    



    