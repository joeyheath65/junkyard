import os
[os.rename(f, 'L3_' + str(f)) for f in os.listdir('.') 
if ((not f.startswith('.')) and f.endswith(".xlsm"))]

