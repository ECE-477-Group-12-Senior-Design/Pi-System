# Main.py
# 
# ECE 47700
# Group 12
# Brace for Impact
#
# October 01, 2021
#

from GUI import launch_start
from Setup import setup
from EmergencyAlert import *
from SetupEnvironment import *


def main():
    set_environment_variables()
    launch_start(setup)


if __name__ == '__main__':
    main()
