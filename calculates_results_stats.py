#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */calculates_results_stats.py


def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results.
    Args:
        results_dic (dict): Results dictionary.
    Returns:
        dict: Statistics dictionary.
    """
    stats = {
        "n_dogs_img": 0,
        "n_match": 0,
        "n_correct_dogs": 0,
        "n_correct_breed": 0,
        "n_images": len(results_dic),
        "n_notdogs_img": 0,
        "n_correct_notdogs": 0,
    }

    for value in results_dic.values():
        stats["n_match"] += value[2]
        if value[3]:
            stats["n_dogs_img"] += 1
            stats["n_correct_dogs"] += value[4]
            stats["n_correct_breed"] += value[2]
        else:
            stats["n_notdogs_img"] += 1
            stats["n_correct_notdogs"] += 1 - value[4]

    # Calculate percentages
    stats["pct_match"] = (stats["n_match"] / stats["n_images"]) * 100
    stats["pct_correct_dogs"] = (stats["n_correct_dogs"] / stats["n_dogs_img"]) * 100
    stats["pct_correct_breed"] = (stats["n_correct_breed"] / stats["n_dogs_img"]) * 100
    stats["pct_correct_notdogs"] = (
        (stats["n_correct_notdogs"] / stats["n_notdogs_img"]) * 100
        if stats["n_notdogs_img"] > 0
        else 0
    )

    return stats
