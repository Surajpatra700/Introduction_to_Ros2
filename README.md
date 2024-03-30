# Introduction_to_Ros2

## ROS2 Publisher-Subscriber Example (Python)

This repository implements a simple ROS2 publisher and subscriber in Python.

**Project Structure:**

* `ros2_ws_suraj/`: Main ROS 2 workspace directory.
* `ros2_ws_suraj/src/`: Contains ROS 2 package source code.
    * `py_topic/`: Your ROS 2 package directory.
        * `setup.py`: Python setup script for building the package.
        * `package.xml`: ROS 2 package manifest file.
        * `py_topic/`: Python module directory.
            * `__init__.py`: Empty file to mark the directory as a Python package.
            * `py_pub_spiral.py`: Python script for the ROS2 publisher.
            * `py_sub_spiral.py`: Python script for the ROS2 subscriber.

**Functionality:**

* `py_pub_spiral.py` publishes the message "Hello! ROS2 is fun" to a specific topic (likely named `/spiral`).
* `py_sub_spiral.py` subscribes to the same topic (`/spiral`) and prints any received messages to the console.

**Building and Running:**

1. **Source ROS 2 setup file:**

   ```bash
   source install/setup.bash  # Assuming your workspace is named "ros2_ws_suraj"
   ```

2. **Run publisher in one terminal:**

   ```bash
   ros2 run py_topic py_pub_spiral.py
   ```

3. **Run subscriber in another terminal:**

   ```bash
   ros2 run py_topic py_sub_spiral.py
   ```

### youtube link:

[youtube](https://youtu.be/iSwJCloTMt8)
