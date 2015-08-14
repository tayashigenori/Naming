#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Define import *

class Noodle:
    def __init__(self, has_age, has_tenkasu):
        self._has_age = has_age
        self._has_tenkasu = has_tenkasu
        return
    def get_noodle_type(self,):
        return self._noodle_type
    def get_noodle_type_name(self,):
        try:
            return NOODLE_NAMES[self._noodle_type]
        except IndexError:
            return ""

    def get_topping_name(self,):
        if self._has_age == False and self._has_tenkasu == False:
            return TOPPING_NAMES[NO_TOPPING]
        r = []
        if self._has_age:
            r.append( TOPPING_NAMES[TOPPING_ABURAAGE] )
        if self._has_tenkasu:
            r.append( TOPPING_NAMES[TOPPING_TENKASU] )
        return ",".join(r)

class Soba(Noodle):
    def __init__(self, has_age = False, has_tenkasu = False):
        Noodle.__init__(self, has_age, has_tenkasu)
        self._noodle_type = NOODLE_SOBA
        return

class Udon(Noodle):
    def __init__(self, has_age = False, has_tenkasu = False):
        Noodle.__init__(self, has_age, has_tenkasu)
        self._noodle_type = NOODLE_UDON
        return

if __name__ == '__main__':
    main()
