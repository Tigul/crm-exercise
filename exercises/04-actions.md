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

# Actions
In this exercise, we will implement an action designator. Actions are a more complex and abstract concept than motions. 
They can be used to perform a sequence of motions and other actions, and they can also include conditions and effects.

In general, you can think of motions as the atomic movements that a robot can perform, while actions are higher-level 
tasks that can be composed of multiple motions and other actions. For example, a motion is "move the left arm to a specific position", while an action is "pick up an object with the left arm".


## Exercise 1: Implementing the Action Designator

The actions we will implement in this exercise are:
* **Pick**: This action will pick up an object with the robot's end effector.
* **Place**: This action will place an object at a specific location with the robot's end effector.
* **Navigate**: This action will move the robot's end effector to a specific position in Cartesian space.

You need to implement the `ActionDesignator` class in the `exercises/architectures/actions.py` file.

### Setup
We use the same world as in the previous exercises. 
```python
from architecture.world import setup_world
world = setup_world()
```

### Pick Action
You need to implement the `PickAction` class in the `exercises/architectures/actions.py` file.
The `PickAction` should take an object designator and an arm as input and should perform the pick action by moving the robot's end effector to the object's position and closing the gripper.

The arm is given as the name of the link that should be used for the pick action.

```python
from architecture.actions import PickAction
from architecture.objects import ObjectDesignator
from architecture.relation import Relationship, SpatialRelationship
on = Relationship(table, SpatialRelationship.ONTOP)
milk = ObjectDesignator("milk", [on])

pick_action = PickAction(object_designator=milk, arm="l_gripper_tool_frame")
pick_action.perform(world=world)
```

### Place Action
You need to implement the `PlaceAction` class in the `exercises/architectures/actions.py` file.
The `PlaceAction` should take an object designator, a target position in Cartesian space, and an arm as input.

The `PlaceAction` should perform the place action by moving the robot's end effector to the target position and opening the gripper.
This action assumes that the object is already in the robot's gripper, meaning that the pick action has been performed before.
Therefore, we are re-using the `ObjectDesignator` from the pick action.

```python
from architecture.actions import PlaceAction
from architecture.objects import ObjectDesignator
from architecture.relation import Relationship, SpatialRelationship

target_pose = np.eye(4)
target_pose[:3, 3] = [0.5, 0.0, 0.8]  # Set the target position
place_action = PlaceAction(object_designator=milk, target_pose=target_pose, arm="l_gripper_tool_frame")
place_action.perform(world=world)
```

### Navigate Action
You need to implement the `NavigateAction` class in the `exercises/architectures/actions.py` file.
The `NavigateAction` should take a target pose in Cartesian space as input and should perform the navigate action by moving the robot's base to the target position.

```python
from architecture.actions import NavigateAction
import numpy as np
target_pose = np.eye(4)
target_pose[:3, 3] = [1.0, 0.0, 0.0]  # Set the target position
navigate_action = NavigateAction(target_pose=target_pose)
navigate_action.perform(world=world)
```
