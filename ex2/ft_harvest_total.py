#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_harvest_total.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ny-araza <ny-araza@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/16 10:18:16 by ny-araza            #+#    #+#            #
#   Updated: 2026/03/16 10:22:17 by ny-araza           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_harvest_total():
    weight_one = int(input("Day 1 harvest: "))
    weight_two = int(input("Day 2 harvest: "))
    weight_three = int(input("Day 3 harvest: "))
    total_weight = weight_one + weight_two + weight_three
    print(f"Total harvest: {total_weight}")