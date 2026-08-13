#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */get_pet_labels.py

from os import listdir


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based on image filenames.
    Args:
        image_dir (str): Path to the folder of images.
    Returns:
        dict: Dictionary with image filenames as keys and pet labels as values.
    """
    results_dic = {}

    # List all files in the directory
    file_list = listdir(image_dir)

    for file in file_list:
        if file.startswith("."):  # Ignore hidden files
            continue

        # Extract label from filename
        label = " ".join(
            [word.lower() for word in file.split("_") if word.isalpha()]
        ).strip()
        results_dic[file] = [label]

    return results_dic
