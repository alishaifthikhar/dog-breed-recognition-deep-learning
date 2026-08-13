#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */classify_images.py

from os.path import join
from classifier import classifier


def classify_images(images_dir, results_dic, model):
    """
    Classifies pet images using the given CNN model and updates results dictionary.
    Args:
        images_dir (str): Path to the folder of images.
        results_dic (dict): Dictionary of pet labels.
        model (str): CNN model architecture.
    """
    # for key in results_dic:
    for key, value in results_dic.items():
        image_path = join(images_dir, key)
        classifier_label = classifier(image_path, model).lower().strip()

        # Check if pet label matches classifier label
        match = 1 if results_dic[key][0] in classifier_label else 0
        results_dic[key].extend([classifier_label, match])
