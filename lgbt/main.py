#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import codecs
import getopt

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

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

def usage():
    sys.stderr.write("%s -p m -m m -l m,f\n" %os.path.basename(__file__))
    sys.stderr.write("%s --phisically=male --mentally=male --loves=male,female\n" %os.path.basename(__file__))
    sys.exit(1)

def main():
    # get options
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   "hp:m:l:v",
                                   ["help", "phisically=", "mentally=", "loves="])
    except getopt.GetoptError, err:
        # ヘルプメッセージを出力して終了
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    phisically_str = None
    mentally_str = None
    loves_str = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-p", "--phisically"):
            phisically_str = a
        elif o in ("-m", "--mentally"):
            mentally_str = a
        elif o in ("-l", "--loves"):
            loves_str = a
        else:
            assert False, "unhandled option"

    # if values unspecified get them interactivelly
    if phisically_str == None:
        sys.stderr.write("Enter your phisical gender: ")
        phisically_str = sys.stdin.readline().strip()
    if mentally_str == None:
        sys.stderr.write("Enter your mental gender: ")
        mentally_str = sys.stdin.readline().strip()
    if loves_str == None:
        answers = {}
        sys.stderr.write("Do you love male? (y/n) ")
        answers['male'] = sys.stdin.readline().strip()
        sys.stderr.write("Do you love female? (y/n) ")
        answers['female'] = sys.stdin.readline().strip()
        loves_str = ",".join(
            [gender for gender,answer in answers.items() if answer.lower() in ('y', 'yes') ]
            )

    d = {
        'm': MALE,
        'male': MALE,
        'f': FEMALE,
        'female': FEMALE,
        }
    person = Person(
        phisically = d.get(phisically_str, False),
        mentally = d.get(mentally_str, False),
        loves = [d.get(l, False) for l in loves_str.split(',')],
        )
    message = u"I am phisically %s, mentally %s and loves %s\n" %(
        convert_gender_to_string(person._phisically),
        convert_gender_to_string(person._mentally),
        convert_gender_to_string(person._loves)
        )
    message += u"\tthey call me %s\n" %convert_lgbt_to_string( person.get_lgbt() )
    sys.stdout.write(message)

if __name__ == '__main__':
    main()
