# Box-counting in three dimensional numpy arrays.

Description from [wikipedia](https://en.wikipedia.org/wiki/Fractal_dimension)
>In mathematics, more specifically in fractal geometry, a fractal dimension is a ratio providing a statistical index of complexity comparing how detail in a pattern (strictly speaking, a fractal pattern) changes with the scale at which it is measured. It has also been characterized as a measure of the space-filling capacity of a pattern that tells how a fractal scales differently from the space it is embedded in; a fractal dimension does not have to be an integer.

Here we offer a function that calculates the fractal dimension of an object embedded in three dimensional space using the boxcounting method, also known as the [Minkowski-Bouligand](https://en.wikipedia.org/wiki/Minkowski%E2%80%93Bouligand_dimension) dimension.

### Usage
Simple example, measuring a box in 3D space.


```python
import numpy as np
from FractalDimension import fractal_dimension
import matplotlib.pyplot as plt

#test data
box = np.zeros(shape = (100,100,100))
box[20:80,20:80,20:80] = 1

fd = fractal_dimension(box, n_offsets=10, plot = True)
print(f"Fractal Dimension of the box: {fd}")
plt.show()
```

    Fractal Dimension of the box: 3.036397272261638



![png](README_notebook_files/README_notebook_1_1.png)


For a more complete overview of the function and its parameters, have a look at the notebook detailing the development of the function in binder.

## Our use case: measurement of the Fractal Dimension of a coordinates system from Molecular Dynamics simulations

Using [dana](https://github.com/pauvals/din-mol-Li), our molecular dynamics program, we obtained different lithium metal anode configurations. One may use this script to analyze 
their fractal dimension. We used directly the `fractal.py` script to analyze our processed outputs.


Made with :mate: :metal: :)


