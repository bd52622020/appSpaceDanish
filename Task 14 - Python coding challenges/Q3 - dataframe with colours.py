#!/usr/bin/env python

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.uniform(-100,100,size=(10, 4) ) )
def colors(val):
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color
df.style.applymap(colors)