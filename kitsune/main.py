#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs

sys.stdout = codecs.getwriter('shift_jis')(sys.stdout)
sys.stderr = codecs.getwriter('shift_jis')(sys.stderr)

from Person import Kansaijin, Kantoujin
from Noodle import Udon, Soba

def main():
    people = (Kantoujin(), Kansaijin())
    noodles = (Udon(has_age = False, has_tenkasu = False),
               Udon(has_age = True,  has_tenkasu = False),
               Udon(has_age = False, has_tenkasu = True),
               Udon(has_age = True,  has_tenkasu = True),
               Soba(has_age = False, has_tenkasu = False),
               Soba(has_age = True,  has_tenkasu = False),
               Soba(has_age = False, has_tenkasu = True),
               Soba(has_age = True,  has_tenkasu = True),
               )
    for p in people:
        for n in noodles:
            sys.stdout.write(u"おっす、オラ %s 人！\n" %p.get_location_name() )
            sys.stdout.write(u"\t%s の %s は" %(n.get_topping_name(),
                                             n.get_noodle_type_name()) )
            try:
                sys.stdout.write(u"「%s」ですね\n" %p.call_name(n))
            except Exception as e:
                sys.stderr.write(u"%s\n" %e.message)

if __name__ == '__main__':
    main()
