import json
import os

s = ', '.join(['"'+ t+'":"1"' for t in list(['A', 'B', 'C'])])
print("{" + s + "}")