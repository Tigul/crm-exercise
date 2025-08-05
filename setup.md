# Setup 

## Dependencies
These exercises are based on the [Semantic World](https://github.com/cram2/semantic_world) project. 
So you need to clone the repository and install it. 

You will also need to install ROS2 Jazzy: 
https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html

## Installation

### Setup a virtual environment
To avoid conflicts with other Python packages, it is recommended to create a virtual environment. You can do this using the following command:
```bash
python3 -m venv crm-venv
source crm-venv/bin/activate
pip install -r requirements.txt
```

### Install the Semantic World
Now we need to clone the Semantic World repository and install it.
```bash
source crm-venv/bin/activate
git clone https://github.com/cram2/semantic_world.git
pip install -e semantic_world
```

