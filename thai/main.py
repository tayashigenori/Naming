#!/usr/bin/env python
# -*- coding: utf-8 -*-

TONE_MIDDLE  = 0
TONE_LOW     = 1
TONE_FALLING = 2
TONE_HIGH    = 3
TONE_RISING  = 4

MAI_0 = 0 # NO TONE SIGN
MAI_1 = 1
MAI_2 = 2
MAI_3 = 3
MAI_4 = 4

tones = {
    MAI_0: TONE_MIDDLE,
    MAI_1: TONE_LOW,
    MAI_2: TONE_FALLING,
    MAI_3: TONE_HIGH,
    MAI_4: TONE_RISING,
}

class ThaiSyllable:
    def __init__(self, init, vowel, final = False, tone_sign = False):
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
        # self._is_long = True
        return
    def create(self, is_long):
        self._is_long = is_long
        return

class ThaiConsonant:
    def __init__(self, char, height, sound_as_initial, sound_as_final = False):
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

class ThaiToneChecker:
    def get_tone(self, c):
        if c.get_tone_sign() == False: # without tone signs
            return self.get_tone_without_signs(c.get_init(),
                                               c.get_vowel(),
                                               c.get_final(),
                                               )
        else:
            return self.get_tone_with_signs(c.get_init(),
                                            c.get_tone_sign(),
                                            )
    """
    with signs
    """
    def get_tone_with_signs(self, init, tone_sign):
        # LOW or not
        if init.is_low:
            # TODO: throw error if tone_sign == MAI_3, MAI_4
            return tones[tone_sign + 1]
        else:#if init.is_low == False:
            return tones[tone_sign]

    """
    without signs
    """
    def get_tone_without_signs(self, init, vowel, final):
        # ALIVE or DEAD
        if self.is_alive(vowel, final):
            return self.get_tone_without_signs_alive(init)
        else:
            return self.get_tone_without_signs_dead(init, vowel)

    def get_tone_without_signs_alive(self, init):
        # non-HIGH or HIGH
        tone_sign = NO_TONE_SIGN
        if init.is_high == False:
            return tones[tone_sign]
        else:
            return tones[tone_sign - 1]
    def get_tone_without_signs_dead(self, init, vowel):
        # LOW or non-LOW
        tone_sign = MAI_1
        if init.is_low and vowel.is_long == False:
            tone_sign = MAI_2
        return tones[tone_sign]
    def is_alive(self, vowel, final): # 平音
        return self.is_dead() != True
    def is_dead(self, vowel, final): # 促音
        if final != False: # with final consonant
            return final().get_fsound() in (u"-k", u"-t", u"-p")
        else: #if final == False: # without final consonant
            return vowel().is_long() == False

def get_chars(filename, separator = u"\t"):
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
    chars = get_chars("./consonants.txt")
    print chars
    return

if __name__ == '__main__':
    main()
