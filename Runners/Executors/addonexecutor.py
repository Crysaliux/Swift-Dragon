from os import listdir
import os


def AddonWalker(list):
    addons = listdir("Addons/")
    for addon in addons:
        if addon.endswith(".py") is True:
            list.append(f"Addons.{addon[:-3]}")
    return list

