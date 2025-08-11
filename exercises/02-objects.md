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

# Object Designator
In this exercise, we will implement an object designator that can be used to refer to objects in the world. 
This designator will be used to identify objects based on their properties and relations to other objects.

The main purpose of an object designator is to provide a way to refer to objects in the world in a way that is independent of their specific representation. 
Meaning you can describe an object without referring to its specific Body in the world.

The code for this exercise is located in the `exercises/architectures/objects.py` file.

## Setup 
First off we need to set up a wold in which we will work.
```python
from archtitecture.world import setup_world

world = setup_world()
```

This world contains an apartment with a kitchen, the PR2 robot as well as a Milk bottle and a Cup on the table.

## Exercise 1: Implementing the Object Designator
You need to the `__iter__` method of the `ObjectDesignator` class in the `exercises/architectures/objects.py` file.
The `ObjectDesignator` should iterate over all possible solutions as a generator.

```python
from architecture.objects import ObjectDesignator
from architecture.relation import Relationship

on_relation = Relationship(table, SpatialRelationship.ONTOP)

milk = ObjectDesignator("milk", [on_relation])

```

```python
from architecture.objects import ObjectDesignator
from architecture.relation import Relationship

on_relation = Relationship(table, SpatialRelationship.ONTOP)

milk = ObjectDesignator("milk", [on_relation])

next_to = Relationship(milk, SpatialRelationship.NEXT_TO)
cup = ObjectDesignator("cup", [on_relation, next_to])
```

