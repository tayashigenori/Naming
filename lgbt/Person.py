#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Define import *

class Person:
    def __init__(self,
                 phisically = MALE,
                 mentally = MALE,
                 loves = [FEMALE]
                 ):
        if phisically not in (MALE, FEMALE):
            raise Exception("Unexpected phisical gender")
        self._phisically = phisically

        if mentally not in (MALE, FEMALE):
            raise Exception("Unexpected mental gender")
        self._mentally = mentally

        if type(loves) == list:
            for g in loves:
                if g not in (MALE, FEMALE):
                    raise Exception("Loves unexpected gender")
            self._loves = loves
        else:
            if loves not in (MALE, FEMALE):
                raise Exception("Loves unexpected gender")
            self._loves = [loves]
        return

    def get_lgbt(self,):
        # results can be more than one
        r = []
        # T: need to check self._loves only
        if self.is_T(self._loves):
            r.append( BISEXUAL )
        # B: need to check phisical gender and mental gender
        if self.is_B(self._phisically, self._mentally):
            r.append( TRANSGENDER )
        # G & L: need to check all
        if self.is_G(self._phisically, self._mentally, self._loves):
            r.append( GAY )
        if self.is_L(self._phisically, self._mentally, self._loves):
            r.append( LESBIAN )
        if len(r) == 0:
            return [STRAIGHT]
        else:
            return r
    """
    https://docs.google.com/spreadsheets/d/1-y9vlGV9OrRkGmbTgLlycXSqeN4fATVrpXFtLYf0xqU/edit?usp=sharing
    """
    def is_T(self, loves):
        if len(loves) == 2 \
           and MALE in loves and FEMALE in loves:
            return True
        return False
    def is_B(self, phisically, mentally):
        if phisically != mentally:
            return True
        return False
    def is_G(self, phisically, mentally, loves):
        if phisically == MALE and mentally == MALE \
           and loves == [MALE]: # MALE in self._loves ?
            return True
        return False
    def is_L(self, phisically, mentally, loves):
        if phisically == FEMALE and mentally == FEMALE \
           and loves == [FEMALE]: # FEMALE in self._loves ?
            return True
        return False
