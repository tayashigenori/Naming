#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ThaiTone import ThaiTone

class ThaiSyllable:
    def __init__(self, init, vowel, final = None, tone_sign = None):
        self._init = init
        self._vowel = vowel
        self._final = final
        self._tone_sign = tone_sign
        return
    def get_init(self,):
        return self._init
    def get_vowel(self,):
        return self._vowel
    def get_final(self,):
        return self._final
    def get_tone_sign(self,):
        return self._tone_sign

class ThaiVowel:
    def __init__(self, char):
        # TODO
        self._is_long = True
        return

class ThaiConsonant:
    def __init__(self, char, height, sound_as_initial, sound_as_final = None):
        self._char = char
        self._height = height
        self._isound = sound_as_initial
        self._fsound = sound_as_final
        return
    def get_char(self,):
        return self._char
    def get_height(self,):
        return self._height
    def get_isound(self,):
        return self._isound
    def get_fsound(self,):
        return self._fsound
    def is_low(self,):
        return self._height == u"L"
    def is_high(self,):
        return self._height == u"H"

def get_consonants(filename = "./consonants.txt", separator = u"\t"):
    r = {}
    f = open(filename)
    try:
        for line in f.readlines():
            line = unicode(line.strip(), 'utf-8')
            (char, char_name, sound_i, sound_f, ipa_i, ipa_f, height) =  line.split(separator)
            r[char] = ThaiConsonant(char, height, sound_i, sound_f)
    finally:
        f.close()
    return r

def main():
    consonants = get_consonants()
    syl = {
        "init": u"ต",
        "vowel": u"อ",
        "final": u"บ",
        }
    TS = ThaiSyllable(consonants[ syl["init"] ],
                      syl["vowel"],
                      consonants[ syl["final"] ],
                      tone_sign = None)
    print ThaiTone(TS).get_tone()
    return

if __name__ == '__main__':
    main()
