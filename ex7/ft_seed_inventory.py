#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_seed_inventory.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ny-araza <ny-araza@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/16 12:50:28 by ny-araza            #+#    #+#            #
#   Updated: 2026/03/16 13:37:58 by ny-araza           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    if (unit == "packets"):
        print(f"{seed_type.title()} seeds: {quantity} packets available")
    elif (unit == "grams"):
        print(f"{seed_type.title()} seeds: {quantity} grams total")
    elif (unit == "area"):
        print(f"{seed_type.title()} seeds: covers {quantity} square meters")
    else:
        print(f"Unknown unit type")
        