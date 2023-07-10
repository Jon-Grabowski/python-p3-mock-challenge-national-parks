#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

# n1 = NationalPark("Yosemite Park")
# v1 = Visitor("TJ")
# t1 = Trip(v1, n1, "today", "tomorrow")
# # t2 = Trip(n1, v1, "today", "tomorrow")

vis = Visitor("Flat White")

p1 = NationalPark('Alaska Wilds')
p2 = NationalPark('Bryce Canyon')
t_1 = Trip(vis, p1, "","")
t_2 = Trip(vis, p2, "","")
t_3 = Trip(vis, p1, "", "")

ipdb.set_trace()
