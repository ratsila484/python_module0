#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ny-araza <ny-araza@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/16 10:46:41 by ny-araza            #+#    #+#            #
#   Updated: 2026/03/16 11:09:18 by ny-araza           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_recursive():
    days_harvest = int(input("Days until harvest: "))
    i = 1
    ft_count(days_harvest, i)

def ft_count(days_harvest, i):
    if (days_harvest == 0):
        print("harvest time!")
        return 1
    else:
        print(f"Day {i}")
        i = i + 1
        return ft_count(days_harvest - 1, i)