### Min Max Normalization
---

A method where the maximum and minimum values in the dataset are used to standardize
the rest of the dataset entries by mapping them to a value between 0 and 1. 

This function is applied to each value in the dataset. <br/> 

```shell
normalized value = (value - minimum value) / (maximum value - minus value)
```

There are many ways to do this in Python. Here is one I created. <br/>

```python
import numpy

# dummy data
dataset = numpy.array([1.1, 4.3, -9.9, 2.5, 2.3, -7.6, 9.5,
                      4.5, 2.2, 6.7, 1.9, 8.7, 6.7, 6.6, 
                      6.6, 3.2, -5.7, 8.1])
   
# tuple of min max values from dataset
min_max = (dataset.min(),dataset.max())

# function that normalizes dataset
make_normal = lambda dataset: numpy.asarray([((val - min_max[0]) / (min_max[1] - min_max[0])) for val in dataset])

new_dataset = make_normal(dataset)
```

Let's visualize <br/>

```python
import matplot.pyplot as plt



<img src="https://github.com/tmartin2/Neurophysiology/blob/master/SynapticIntegration/Images/backprop.gif" width="600" height="400" align="center" />
