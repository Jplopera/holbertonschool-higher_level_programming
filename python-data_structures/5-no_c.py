#!/usr/bin/python3
def no_c(my_string):
    c = {ord("c"): "", ord("C"): ""}
    return (my_string.translate(c))
