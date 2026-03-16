#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_summary.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ny-araza <ny-araza@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/16 11:11:14 by ny-araza            #+#    #+#            #
#   Updated: 2026/03/16 12:50:03 by ny-araza           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_garden_summary():
    name = input("Enter the garden name: ")
    number_plants = input("Enter the number of plants: ")
    print(f"Garden: {name}")
    print(f"Plants: {number_plants}")
    print("Status: Growing well!")
