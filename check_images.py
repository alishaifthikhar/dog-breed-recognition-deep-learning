#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */check_images.py

# Imports python modules
import time

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results


def main():
    # Start timer
    start_time = time.time()

    # 1. Retrieve command-line arguments
    in_arg = get_input_args()

    # Function that checks command-line arguments using in_arg
    check_command_line_arguments(in_arg)

    # 2. Get pet labels
    results_dic = get_pet_labels(in_arg.dir)

    # Function that checks Pet Images in the results Dictionary using results_dic
    check_creating_pet_image_labels(results_dic)

    # 3. Classify images
    classify_images(in_arg.dir, results_dic, in_arg.arch)

    # Function that checks Results Dictionary using results_dic
    check_classifying_images(results_dic)

    # 4. Adjust results for dogs
    adjust_results4_isadog(results_dic, in_arg.dogfile)

    # Function that checks Results Dictionary for is-a-dog adjustment using results_dic
    check_classifying_labels_as_dogs(results_dic)

    # 5. Calculate results statistics
    results_stats = calculates_results_stats(results_dic)

    # Function that checks Results Statistics Dictionary using results_stats
    check_calculating_results(results_dic, results_stats)

    # 6. Print results
    print_results(
        results_dic,
        results_stats,
        in_arg.arch,
        print_incorrect_dogs=True,
        print_incorrect_breed=True,
    )

    # Stop timer
    end_time = time.time()
    tot_time = end_time - start_time

    # Computes overall runtime in seconds & prints it in hh:mm:ss format
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time / 3600))) + ":" + str(int((tot_time % 3600) / 60)) + ":" + str(int((tot_time % 3600) % 60)))


if __name__ == "__main__":
    main()
