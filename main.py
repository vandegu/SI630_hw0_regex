import csv
import pandas as pd
import numpy as np
import re

#  Open the file with Pandas (faster, avoids the pesky 'b's)
din = pd.read_table('webpages.csv',delimiter=',')
din = np.array(din)

# Iterate over the input data and search for email addresses. If found, add to the array.
for i,line in enumerate(din[0:4,:]):
    print(line[0])
