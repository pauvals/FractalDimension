# Box-counting in three dimensional numpy arrays.

Description from [wikipedia](https://en.wikipedia.org/w/index.php?title=Fractal_dimension&oldid=1253046936) (2/2025):
>In mathematics, a fractal dimension is a term invoked in the science of geometry to provide a rational statistical index of complexity detail in a pattern. A fractal pattern changes with the scale at which it is measured. It is also a measure of the space-filling capacity of a pattern, and it tells how a fractal scales differently, in a fractal (non-integer) dimension.


Here [we](https://github.com/ChatzigeorgiouGroup) offer a function that calculates the fractal dimension of an object embedded in three dimensional space using the boxcounting method, also known as the [Minkowski-Bouligand](https://en.wikipedia.org/wiki/Minkowski%E2%80%93Bouligand_dimension) dimension.

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

## A use case: measurement of the Fractal Dimension of a coordinates system from Molecular Dynamics simulations

Using [dana](https://github.com/pauvals/din-mol-Li), our molecular dynamics program, we obtained different lithium metal anode configurations. One may use this script to analyze 
their fractal dimension. We used directly the `fractal.py` script to analyze our processed outputs.


Made with :mate: :metal: :)


