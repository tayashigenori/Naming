#!/usr/bin/env python
# -*- coding: utf-8 -*-

SOUND_K  = u"k"
SOUND_KH = u"kh"

class ThaiChar(str):
    def __init__(self, height, sound_as_initial, sound_as_final):
        self._height = height
        self._isound = sound_as_initial
        self._fsound = sound_as_final

def main():
    return

if __name__ == '__main__':
    main()
