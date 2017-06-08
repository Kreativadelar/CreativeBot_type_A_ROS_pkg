import robot_upstart

j = robot_upstart.Job(user="pabi")
j.add(package="mbot_ranger_bringup", filename="launch/teleop.launch")
j.install()
