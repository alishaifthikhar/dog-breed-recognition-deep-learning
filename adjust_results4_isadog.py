#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */adjust_results4_isadog.py


def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to indicate if the labels are of dogs.
    Args:
        results_dic (dict): Results dictionary.
        dogfile (str): Path to the file containing dog names.
    """
    # Read dog names from file
    with open(dogfile, "r") as f:
        dog_names = {line.strip().lower() for line in f}

    for value in results_dic.values():
        pet_label_is_dog = 1 if value[0] in dog_names else 0
        classifier_label_is_dog = 1 if value[1] in dog_names else 0
        value.extend([pet_label_is_dog, classifier_label_is_dog])
