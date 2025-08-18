---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.3
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Locations II
In this exercise, we will implement a `LocationDesignator` that uses the `Costmap` to find a location that satisfies a set of constraints.
The `LocationDesignator` will sample from the costmap to find a location and verify that it satisfies the constraints.

## Exercise 1: Implementing the LocationDesignator for Occupancy
You need to implement the `LocationDesignator` class in the `exercises/architectures/locations.py` file.

### Setup
We use the same world as in the previous exercises. 
```python
from architecture.world import setup_world
world = setup_world()
```
### Implementing the Occupancy Location Designator
The occupancy location designator is a location designator that finds a location where the robot can stand.
You need to implement the `OccupancyLocationDesignator` class in the `exercises/architectures/locations.py` file.

```python
import numpy as np
from architecture.locations import LocationDesignator
location = LocationDesignator(target=np.array([1,1,0]), world=world)

```

### Implementing the Reachability Location Designator
The reachability location designator is a location designator that finds a location from where a robot can reach a point in the world.
For this location you need to combine both the occupancy and reachability costmaps.

You need to implement the `ReachabilityLocationDesignator` class in the `exercises/architectures/locations.py` file.

```python
from architecture.locations import ReachabilityLocationDesignator
location = ReachabilityLocationDesignator(target=np.array([1,1,0]), world=world)
```
