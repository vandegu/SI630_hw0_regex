import csv
import pandas as pd
import numpy as np
import re

#  Open the file with Pandas (faster, avoids the pesky 'b's)
din = pd.read_table('webpages.csv',delimiter=',')
din = np.array(din)

# Iterate over the input data and search for email addresses. If found, add to the array.
for i,line in enumerate(din[:]):
    sstr = line[0]
    m = re.search('([a-zA-Z0-9]+)\s*(/at/|@|\[at\])\s*([a-zA-Z0-9]+)\s*(/dot/|\[dot\]|\.)\s*([a-zA-Z0-9]+)',sstr)
    if m:
        #print('{}@{}.{}'.format(m.group(1),m.group(3),m.group(5)))
        din[i,1] = '{}@{}.{}'.format(m.group(1),m.group(3),m.group(5))
    else:
        din[i,1] = 'None'

print(din[:100,:])
np.savetxt('email-outputs.csv',din,delimiter=',',header='html,email',fmt='%s',comments='')
