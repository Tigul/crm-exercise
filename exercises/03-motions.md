from exercises.architecture.motions import JointMotionDesignator---
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

# Motions

In this exercise, we will implement a motion designator that can be used to control the robot's movements.
In total there are three different types of motions that we will implement:
* **Joint Motion**: This motion will move the robot's joints to a specific position.
* **Cartesian Motion**: This motion will move the robot's end effector to a specific position in Cartesian space.

The code for this exercise is located in the `exercises/architectures/motions.py` file.

## Setup
We use the same world as in the previous exercises. 
```python
from architecture.world import setup_world
world = setup_world()
```

## Exercise 1: Implementing the Joint Motion
You need to implement the `JointMotion` class in the `exercises/architectures/motions.py` file.
The `JointMotion` gets a dict of joint names and their target positions as input and should move the robot's joints to the specified positions.

```python
from architecture.motions import JointMotion

joint_goals = JointMotion({
    "head_pan_joint": 0.0,
    "head_tilt_joint": 0.0,
    "torso_lift_joint": 0.0,
    "arm_left_1_joint": 0.0,
    "arm_left_2_joint": 0.0,
    "arm_left_3_joint": 0.0,
    "arm_left_4_joint": 0.0,
    "arm_left_5_joint": 0.0,
    "arm_left_6_joint": 0.0,
    "arm_left_7_joint": 0.0,
})


joint_motion = JointMotionDesignator(joint_goals=joint_goals, 
                                     end_effector="left_gripper")

joint_motion.perform(world=world)
```

## Exercise 2: Implementing the Cartesian Motion
You need to implement the `CartesianMotion` class in the `exercises/architectures/motions.py` file.
The `CartesianMotion` gets a target position in Cartesian space and should move the robot's end effector to the specified position.

```python
from architecture.motions import CartesianMotion
import numpy as np

targte_pose = np.eye(4)

cartesian_motion = CartesianMotion(goal_pose=target_pose, 
                                   end_effector="left_gripper")

cartesian_motion.perform(world=world)
```

