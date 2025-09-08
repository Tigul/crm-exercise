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

# Introduction 
In this exercise, we will introduce you to the basic concepts that we will use in the course. This includes the following:
* How to interact with the Belief state
* How to transform between body frames
* How to use the inverse kinematics solver 

## Using the Belief state
Each cognitive architecture needs a representation of the world in which it operates and which can be used to infer 
information about the world. As a belief state, we use the [Semantic World](https://github.com/cram2/semantic_world) 
which creates a symbolic representation of the world and supports forward and inverse kinematics on it. 

### Loading URDFs
URDFs are used to represent the robot and its environment. The Semantic World supports loading URDFs and adding it to a 
world. The following code snippet shows how to load a URDF and add it to the world:

```python
import os.path
from semantic_world.adapters.urdf import URDFParser
from pathlib import Path


pr2_path = Path().resolve().joinpath("..", "resources", "pr2.urdf")
pr2 = URDFParser.from_file(str(pr2_path)).parse()
```

This will return a `World` with the parsed URDF. To visualize the world and its contents the Semantic World provides a
publisher to RViz2. You can use the following code snippet to visualize the world:

```python
from semantic_world.adapters.viz_marker import VizMarkerPublisher
import rclpy

rclpy.init()
node = rclpy.create_node("semantic_world_viz")

viz_publisher = VizMarkerPublisher(pr2, node)
```
Now you can view the world in RViz2 by opening Rviz2 -> Add -> By Topic -> `/semantic_world/viz_marker`.motion

If you load a second URDF and want to add it to the world, you can use the `merge_world` method of the `World` class:

```python
apartment_path = Path().resolve().joinpath("..", "resources", "apartment.urdf")
apartment = URDFParser.from_file(apartment_path).parse()

apartment.merge_world(pr2)
```

To end the visualization, you can use the following code snippet:

```python
viz_publisher._stop_publishing()
```

### Working with Bodies 
The Semantic World represents the world as a collection of bodies. Bodies are connected to each other via connections. 
These connections can be configured to be fixed or movable.
You can access the bodies in the world using the `bodies` property of the world.
Connections work analogously to bodies.

For our case you can assume that the following mapping holds for the PR2 robot:
Body -> Link
Connection -> Joint

```python 
pr2_path = Path().resolve().joinpath("..", "resources", "pr2.urdf")
pr2 = URDFParser.from_file(str(pr2_path)).parse()
```

```python
pr2.bodies

pr2.connections
```

To get the body of a specific name, you can use the `get_body_by_name` method:

```python
pr2.get_body_by_name("base_link")
```

To get the pose of a body, you can use the `compute_forward_kinematics_np` method:

```python
pr2.compute_forward_kinematics_np(pr2.root, pr2.get_body_by_name("base_link"))
```

This will return the pose of the body relative to the root link of the PR2 as a 4x4 transformation matrix.

### Transforming between body frames
In some cases you need the pose of a body relative to another body or a pose relative to a body. If that is the case, 
you need to transform the pose of the body to the desired frame.

The semantic world provides two methods to transform poses between body frames:
* `compute_forward_kinematics_np`: This method computes the pose of a body relative to another body.
* `transform`: This method transforms a pose or transform to be relative to aother body.

Both of these methods return a 4x4 transformation matrix.

```python
from semantic_world.spatial_types  import TransformationMatrix

pr2.compute_forward_kinematics_np(pr2.root, pr2.get_body_by_name("base_link"))

origin_pose = TransformationMatrix.from_xyz_rpy(x=1.0, reference_frame=pr2.get_body_by_name("torso_lift_link"))

pr2.transform(origin_pose, pr2.get_body_by_name("base_link"))

```

### How to use the inverse kinematics solver
Controlling a robot means setting the position of its joints, however, this is not always the most intuitive way to
control a robot. Instead, it is often more intuitive to specify the pose of the end effector and let the robot compute the joint positions that achieve this pose. This is where inverse kinematics comes into play.

The part that computes the joint positions for a given end effector pose is called the inverse kinematics solver.
The Semantic World provides an inverse kinematics solver that can be used to compute the joint positions for a given end effector pose.

To use the inverse kinematics solver, you need to specify the end effector pose and the body that represents the end effector.
```python
from semantic_world.spatial_computations.ik_solver import  InverseKinematicsSolver
from semantic_world.spatial_types import TransformationMatrix

ik_solver = InverseKinematicsSolver(pr2)

target_pose = TransformationMatrix.from_xyz_rpy(0.4, 0.2, 0.8, reference_frame=pr2.get_body_by_name("base_link"))

joint_positions = ik_solver.solve(pr2.get_body_by_name("base_link"), pr2.get_body_by_name("r_gripper_tool_frame"), target_pose)

for joint, state in joint_positions.items():
    pr2.state[joint.name].position = state
pr2.notify_state_change()
```

For convenience there is also a method to calculate the inverse kinematics directly associated with a world:
```python
joint_positions = pr2.compute_inverse_kinematics(pr2.get_body_by_name("base_link"), pr2.get_body_by_name("r_gripper_tool_frame"), target_pose)
```