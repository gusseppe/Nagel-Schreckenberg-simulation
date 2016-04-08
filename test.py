import numpy as np
import matplotlib.pyplot as plt
import json

with open('road.json') as f:
    data = json.load(f)

a = np.array(data)
# showing image
plt.imshow(a, cmap="Greys", interpolation="nearest")
plt.savefig('ca.png')
plt.show( )
#print(type(data))
#for e in data:
    #print(e)
