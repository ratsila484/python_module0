#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_age.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: ny-araza <ny-araza@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/16 10:24:16 by ny-araza            #+#    #+#            #
#   Updated: 2026/03/16 10:27:24 by ny-araza           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plant_age():
    age_days = int(input("Enter plant age in days: "))
    if (age_days > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow")