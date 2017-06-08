import robot_upstart

j = robot_upstart.Job()
j.add(package="mbot_ranger_bringup", filename="launch/teleop.launch")
j.install()
