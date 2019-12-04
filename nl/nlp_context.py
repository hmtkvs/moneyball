#!/usr/bin/env python
# coding: utf8
"""
Author: marco_bertola
"""


class RequestContext:
    has_verb = False
    category_verb = ""

    has_attribute = False
    category_attribute = ""

    has_player = False
    category_player = ""

    def trace(self):
        print("\n******CONTEXT******")
        print("has_verb\t", self.has_verb)
        print("category_verb\t", self.category_verb)
        print("has_attribute\t", self.has_attribute)
        print("category_attribute\t", self.category_attribute)
        print("has_player\t", self.has_player)
        print("category_player\t", self.category_player)
        print("************")