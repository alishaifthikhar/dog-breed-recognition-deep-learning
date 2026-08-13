#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */get_input_args.py

import argparse


def get_input_args():
    """
    Retrieves and parses command-line arguments provided by the user.
    Returns:
        ArgumentParser object containing the command-line arguments
    """
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument("--dir", type=str, default="pet_images/", help="Image folder")
    parser.add_argument("--arch", type=str, default="vgg", help="CNN model architecture")
    parser.add_argument(
        "--dogfile", type=str, default="dognames.txt", help="Dog names file"
    )

    return parser.parse_args()
