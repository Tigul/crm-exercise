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

# Locations I
This is the first part of the locations exercise. To determine a location that satisfies a set of constraints, we will implement a `LocationDesignator` class.
The `LocationDesignator` will rely on a `Costmap`, the costmap assigns each point in the world a cost based on the constraints 
provided the `LocationDesignator` then samples from the costmap to find a location and verify that it satisfies the constraints.

In this exercise, we will implement the `Costmap` for two constraints the first being where a robot can stand and the 
second being where a robot is most likely to reach a point in the world.

## Exercise 1: Implementing the Costmap

You need to implement the `Costmap` class in the `exercises/architectures/locations.py` file.

## Setup
We use the same world as in the previous exercises. 
```python
from architecture.world import setup_world
world = setup_world()
```
## Implementing the Occupancy Costmap
The occupancy costmap is a costmap that assigns a cost to each point in the world based on whether the robot can stand there or not.

You need to implement the `OccupancyCostmap` class in the `exercises/architectures/locations.py` file.

```python
import numpy as np
from architecture.locations import OccupancyCostmap
occupancy_costmap = OccupancyCostmap(resolution=0.02, width=200, height=200, origin=np.array([1,1,0]),world = world)
```
The `OccupancyCostmap` should return a cost of 0 for points where the robot cannot stand and a cost of 1 for points where the robot can stand.


## Implementing the Reachability Costmap
The reachability costmap is a costmap that assigns a cost to each point in the world based on how likely it is that the robot can reach that point.
You need to implement the `ReachabilityCostmap` class in the `exercises/architectures/locations.py` file.
```python
import numpy as np
from architecture.locations import ReachabilityCostmap
reachability_costmap = ReachabilityCostmap(resolution=0.02, width=200, height=200, origin=np.array([1,1,0]),world = world)
```
The `ReachabilityCostmap` should return a cost of 0 for points that are reachable by the robot and a cost of 1 for points that are not reachable by the robot.