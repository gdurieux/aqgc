from __future__ import absolute_import
# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.2.0 for Linux x86 (64-bit) (November 18, 2022)
# Date: Thu 11 Apr 2024 09:37:34


from .object_library import all_orders, CouplingOrder


QCD = CouplingOrder(name = 'QCD',
                    expansion_order = 99,
                    hierarchy = 1)

QED = CouplingOrder(name = 'QED',
                    expansion_order = 99,
                    hierarchy = 2)

NP = CouplingOrder(name = 'NP',
                   expansion_order = 99,
                   hierarchy = 1)

NPE = CouplingOrder(name = 'NPE',
                    expansion_order = 99,
                    hierarchy = 1)

