"""
-------------------------------------------------------
[program 6
-------------------------------------------------------
Author:  Anshul Khatri
ID:      193313680
Email:   khat3680@mylaurier.ca
Section: CP164 Winter 2020
__updated__ = "2020-01-30"
-------------------------------------------------------
"""

from functions import postfix

string = "4 5 + 12 * 2 3 * -"

ans = postfix(string)

print("Answer: {}",format(ans))