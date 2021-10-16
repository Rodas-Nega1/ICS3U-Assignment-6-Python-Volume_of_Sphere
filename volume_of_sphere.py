# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Oct 2021
# This program asks the user for the radius of their sphere
# and outputs the volume


import math


def volume_of_sphere(radius):
    # calculate volume

    # process
    volume = round(4 * math.pi * pow(radius, 3), 2) / 3

    return volume


def main():
    # this function calls the precedent function

    # input & output
    user_radius = input("Enter the radius of the sphere (cm): ")

    try:
        user_radius_int = int(user_radius)

        if user_radius_int < 0:
            print("")
            print("That is an invalid integer.")

        else:
            calculated_volume = volume_of_sphere(
                radius=user_radius_int,
            )  # call function
            print("")
            print("The volume of your sphere  is {0} cm³".format(calculated_volume))

    except Exception:
        print("")
        print("That is an invalid integer.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
