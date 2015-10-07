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

class ThaiTone:
    def __init__(self, c):
        if c.get_tone_sign() == None: # without tone signs
            self._instance = ThaiToneWithoutSign(c)
        else:
            self._instance = ThaiToneWithSign()
        return
    def get_tone(self, c):
        return self._instance.get_tone(c)
"""
with sign
"""
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
"""
without sign
"""
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

