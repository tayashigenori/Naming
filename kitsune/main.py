#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
sys.stderr = codecs.getwriter('utf-8')(sys.stderr)

from Person import Kansaijin, Kantoujin
from Noodle import Udon, Soba

def test_call_name():
    sys.stderr.write("### test call_name() ###\n")
    people = [Kantoujin(), Kansaijin()]
    noodles = [Udon(has_age = False, has_tenkasu = False),
               Udon(has_age = True,  has_tenkasu = False),
               Udon(has_age = False, has_tenkasu = True),
               Udon(has_age = True,  has_tenkasu = True),
               Soba(has_age = False, has_tenkasu = False),
               Soba(has_age = True,  has_tenkasu = False),
               Soba(has_age = False, has_tenkasu = True),
               Soba(has_age = True,  has_tenkasu = True),
               ]
    for p in people:
        for n in noodles:
            sys.stdout.write(u"おっす、オラ %s 人！\n" %p.get_location_name() )
            sys.stdout.write(u"\t%s の %s は" %(n.get_topping_name(),
                                             n.get_noodle_type_name()) )
            try:
                sys.stdout.write(u"「%s」ですね\n" %p.call_name(n))
            except Exception as e:
                sys.stderr.write(u"%s\n" %e.message)

def test_get_noodle_from_name():
    sys.stderr.write("### test get_noodle_from_name() ###\n")
    people = [Kantoujin(), Kansaijin()]
    #people = [Kansaijin()]
    noodle_strs = [u"きつね", u"たぬき",
                   u"うどん", u"そば",
                   u"きつねうどん", u"きつねそば",
                   u"きつね (うどん)", u"きつね (そば)",
                   u"きつね（うどん）", u"きつね（そば）",
                   u"たぬきうどん", u"たぬきそば",
                   u"たぬき (うどん)", u"たぬき (そば)",
                   u"たぬき（うどん）", u"たぬき（そば）",
                   ]
    for p in people:
        for n_str in noodle_strs:
            sys.stdout.write(u"おっす、オラ %s 人！\n" %p.get_location_name() )
            sys.stdout.write(u"\t「%s」は" %n_str )
            try:
                n = p.get_noodle_from_name( n_str )
                sys.stdout.write(u"%s の %s ですね\n" %(n.get_topping_name(),
                                                    n.get_noodle_type_name() ))
            except Exception as e:
                sys.stderr.write(u"%s\n" %e.message)

def main():
    test_call_name()
    test_get_noodle_from_name()

if __name__ == '__main__':
    main()
