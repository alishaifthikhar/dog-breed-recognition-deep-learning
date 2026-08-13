#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */print_results.py


def print_results(
    results_dic,
    results_stats_dic,
    model,
    print_incorrect_dogs=False,
    print_incorrect_breed=False,
):
    """
    Prints the results statistics and misclassified cases.
    """
    print(f"Results Summary for CNN Model Architecture: {model.upper()}")
    print(f"Number of Images: {results_stats_dic['n_images']}")
    print(f"Number of Dog Images: {results_stats_dic['n_dogs_img']}")
    print(f"Number of Not-a-Dog Images: {results_stats_dic['n_notdogs_img']}")

    # Print percentages in the results_stats_dic
    for key, value in results_stats_dic.items():
        if key.startswith("pct"):
            print(f"{key}: {value:.2f}%")

    # Check and print misclassified dogs if requested
    if print_incorrect_dogs and (
        (results_stats_dic["n_correct_dogs"] + results_stats_dic["n_correct_notdogs"])
        != results_stats_dic["n_images"]
    ):
        print("\nMisclassified Dogs:")
        for key, value in results_dic.items():
            # Either label or classifier is incorrect
            if sum(value[3:]) == 1:
                print(f"File: {key}, Label: {value[0]}, Classified: {value[1]}")

    # Check and print misclassified breeds if requested
    if print_incorrect_breed and (
        results_stats_dic["n_correct_dogs"] != results_stats_dic["n_correct_breed"]
    ):
        print("\nMisclassified Breeds:")
        for key, value in results_dic.items():
            # Is a dog, classified as a dog, but wrong breed
            if value[3] == 1 and value[4] == 1 and value[2] == 0:
                print(f"File: {key}, Label: {value[0]}, Classified: {value[1]}")
