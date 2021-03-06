#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs

sys.stdout = codecs.getwriter('shift_jis')(sys.stdout)

from Person import Person
from Define import *

def convert_gender_to_string(genders):
    if type(genders) != list:
        genders = [genders]
    try:
        gender_names = map(lambda x: GENDER_NAMES[x], genders)
        return u",".join(gender_names)
    except IndexError:
        return u""
def convert_lgbt_to_string(lgbt):
    if type(lgbt) != list:
        lgbt = [lgbt]
    try:
        lgbt_names = map(lambda x: LGBT_NAMES[x], lgbt)
        return u" & ".join(lgbt_names)
    except IndexError:
        return u""

def main():
    people = (Person(phisically = MALE,   mentally = MALE,   loves = MALE),
              Person(phisically = MALE,   mentally = MALE,   loves = FEMALE),
              Person(phisically = MALE,   mentally = MALE,   loves = [MALE, FEMALE]),
              Person(phisically = MALE,   mentally = FEMALE, loves = MALE),
              Person(phisically = MALE,   mentally = FEMALE, loves = FEMALE),
              Person(phisically = MALE,   mentally = FEMALE, loves = [MALE, FEMALE]),
              Person(phisically = FEMALE, mentally = MALE,   loves = MALE),
              Person(phisically = FEMALE, mentally = MALE,   loves = FEMALE),
              Person(phisically = FEMALE, mentally = MALE,   loves = [MALE, FEMALE]),
              Person(phisically = FEMALE, mentally = FEMALE, loves = MALE),
              Person(phisically = FEMALE, mentally = FEMALE, loves = FEMALE),
              Person(phisically = FEMALE, mentally = FEMALE, loves = [MALE, FEMALE]),
              )
    for person in people:
        message = u"I am phisically %s, mentally %s and loves %s\n" %(
            convert_gender_to_string(person._phisically),
            convert_gender_to_string(person._mentally),
            convert_gender_to_string(person._loves)
            )
        message += u"\tthey call me %s\n" %convert_lgbt_to_string( person.get_lgbt() )
        sys.stdout.write(message)

if __name__ == '__main__':
    main()
