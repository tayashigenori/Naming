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

class ThaiTone:
    def __init__(self, c):
        if c.get_tone_sign() == None: # without tone signs
            self._instance = ThaiToneWithoutSign(c)
        else:
            self._instance = ThaiToneWithSign()
        return
    def get_tone(self, c):
        return self._instance.get_tone(c)
class ThaiToneWithSign:
    def get_tone(self, c):
        return self.get_tone_by_init_and_ts(c.get_init(),
                                            c.get_tone_sign(),
                                            )
    def get_tone_by_init_and_ts(self, init, tone_sign):
        # LOW or not
        if init.is_low():
            # TODO: throw error if tone_sign == MAI_3, MAI_4
            return tones[tone_sign + 1]
        else:#if init.is_low == False:
            return tones[tone_sign]

class ThaiToneWithoutSign:
    def __init__(self, c):
        if self.is_alive(c):
            self._instance = ThaiToneWithoutSignAlive()
        else:
            self._instance = ThaiToneWithoutSignDead()
        return
    def is_alive(self, c): # 平音
        return self.is_dead(c) != True
    def is_dead(self, c): # 促音
        init = c.get_init()
        vowel = c.get_vowel()
        final = c.get_final()
        if final != False: # with final consonant
            return final.get_fsound() in (u"-k", u"-t", u"-p")
        else: #if final == False: # without final consonant
            return vowel().is_long() == False
    def get_tone(self, c):
        return self._instance.get_tone(c)

class ThaiToneWithoutSignAlive:
    DEFAULT_TONE_SIGN = MAI_0
    def get_tone(self, c):
        return self.get_tone_by_init( c.get_init() )
    def get_tone_by_init(self, init):
        # non-HIGH or HIGH
        if init.is_high() == False:
            return tones[ self.DEFAULT_TONE_SIGN ]
        else:
            return tones[ self.DEFAULT_TONE_SIGN - 1]
class ThaiToneWithoutSignDead:
    DEFAULT_TONE_SIGN = MAI_1
    def __init__(self,):
        self._instance = ThaiToneWithSign()
        return
    def get_tone(self, c):
        init = c.get_init()
        vowel = c.get_vowel()
        return self.get_tone_by_init_and_vowel(init, vowel)
    def get_tone_by_init_and_vowel(self, init, vowel):
        v_ts = self._get_virtual_tone_sign(init, vowel)
        return self._instance.get_tone_by_init_and_ts(init, v_ts)
    def _get_virtual_tone_sign(self, init, vowel):
        if init.is_low():
            if vowel.is_long() == False:
                return self.DEFAULT_TONE_SIGN + 1
        return self.DEFAULT_TONE_SIGN

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
    TT = ThaiTone(TS)
    print TT.get_tone(TS)
    return

if __name__ == '__main__':
    main()
