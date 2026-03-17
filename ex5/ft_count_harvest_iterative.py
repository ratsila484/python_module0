#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ny-araza <ny-araza@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/16 10:35:24 by ny-araza            #+#    #+#            #
#   Updated: 2026/03/17 08:56:27 by ny-araza           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_iterative():
    days_harvest = int(input("Days until harvest: "))
    for i in range(1, days_harvest + 1):
        print(f"Day {i}")
    print("Harvest time!")
