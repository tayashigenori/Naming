#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

LOCATION_KANTOU = 1
LOCATION_KANSAI = 2
location_names = {
    LOCATION_KANTOU: "関東",
    LOCATION_KANSAI: "関西",
}

class Noodle:
    TOPPING_ABURAAGE = 1
    TOPPING_TENKASU = 2

    PREFIX_KITSUNE_STR = "きつね"
    PREFIX_TANUKI_STR = "たぬき"

    _topping = None
    _location = None

    def __init__(self,):
        self._topping_names = {
            self.TOPPING_ABURAAGE: "油揚げ",
            self.TOPPING_TENKASU: "天かす",
        }
        return

    """
    topping
    """
    def add_aburaage(self,):
        return self.__add_topping(self.TOPPING_ABURAAGE)
    def add_tenkasu(self,):
        return self.__add_topping(self.TOPPING_TENKASU)
    def __add_topping(self, topping):
        self._topping = topping
        return
    def get_topping_str(self,):
        try:
            return self._topping_names[self._topping]
        except IndexError:
            raise ValueError("unknown topping %s" %self._topping)

    """
    location
    """
    def set_location_to_kantou(self,):
        return self.__set_location(LOCATION_KANTOU)
    def set_location_to_kansai(self,):
        return self.__set_location(LOCATION_KANSAI)
    def __set_location(self, location):
        self._location = location
        return
    def get_location(self,):
        return self._location

    """
    name
    """
    def get_name(self, location = None):
        if location != None:
            return self.get_local_name(location)
        return self.get_local_name(self._location)
    def get_local_name(self, location):
        if location == LOCATION_KANTOU:
            return self.get_kantou_name()
        elif location == LOCATION_KANSAI:
            return self.get_kansai_name()
        raise ValueError("unknown location %s" %self._location)
    def get_kantou_name(self,):
        if self._topping == self.TOPPING_TENKASU:
            self._prefix = self.PREFIX_TANUKI_STR
        elif self._topping == self.TOPPING_ABURAAGE:
            self._prefix = self.PREFIX_KITSUNE_STR
        else:
            self._prefix = ""
        return "".join([self._prefix, self._noodle_type_str])
    def get_noodle_type_str(self,):
        return self._noodle_type_str

class Udon(Noodle):
    NOODLE_TYPE_STR = "うどん"
    def __init__(self,):
        Noodle.__init__(self,)
        self._noodle_type_str = self.NOODLE_TYPE_STR
        self._prefix = ""
        return

    def get_kansai_name(self,):
        if self._topping == self.TOPPING_ABURAAGE:
            self._prefix = self.PREFIX_KITSUNE_STR
            noodle_type_str = "(%s)" %self._noodle_type_str
            return "".join([self._prefix, noodle_type_str])
        return self._noodle_type_str

class Soba(Noodle):
    NOODLE_TYPE_STR = "そば"
    def __init__(self,):
        Noodle.__init__(self,)
        self._noodle_type_str = self.NOODLE_TYPE_STR
        self._prefix = ""
        return

    def get_kansai_name(self,):
        if self._topping == self.TOPPING_ABURAAGE:
            self._prefix = self.PREFIX_TANUKI_STR
            noodle_type_str = "(%s)" %self._noodle_type_str
            return "".join([self._prefix, noodle_type_str])
        return self._noodle_type_str

class Person:
    PERSONALITY_DO_AS_ROMANS_DO = 1
    PERSONALITY_SPEAK_MY_DIALECT = 2

    _location = None
    _personality = None
    def __init__(self,):
        return

    """
    name
    """
    def get_location(self,):
        return self._location
    def set_location(self, location):
        self._location = location
        return
    def get_location_str(self,):
        try:
            return location_names[self._location]
        except IndexError:
            raise ValueError("unknown location %s" %self._location)

    """
    personality
    """
    def get_personality(self,):
        return self._personality
    def set_personality(self, personality):
        self._personality = personality
        return

    """
    name
    """
    def call_name(self, noodle):
        if self.get_personality() == self.PERSONALITY_SPEAK_MY_DIALECT:
            return noodle.get_name(self.get_location())
        if noodle.get_location() == None:
            noodle.set_location_to_kantou()
        return noodle.get_name(noodle.get_location())


class KantouJin(Person):
    def __init__(self,):
        self.set_location( LOCATION_KANTOU )
        self.set_personality( self.PERSONALITY_SPEAK_MY_DIALECT )
        return

class KansaiJin(Person):
    def __init__(self,):
        self.set_location( LOCATION_KANSAI )
        self.set_personality( self.PERSONALITY_SPEAK_MY_DIALECT )
        return

def main():
    P1, P2 = (KantouJin(), KansaiJin())
    U1, U2 = (Udon(), Udon())
    S1, S2 = (Soba(), Soba())
    for n1,n2 in ((U1, U2), (S1, S2)):
        n1.add_aburaage()
        n2.add_tenkasu()

    for p in (P1, P2):
        for n in (U1, U2, S1, S2):
            print "in %s %s%s is called %s" %(p.get_location_str(),
                                              n.get_topping_str(),
                                              n.get_noodle_type_str(),
                                              p.call_name(n))

if __name__ == '__main__':
    main()
