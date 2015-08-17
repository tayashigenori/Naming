#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Define import *

class Person:
    def get_location(self,):
        return self._from
    def get_location_name(self,):
        try:
            return LOCATION_NAMES[self._from]
        except IndexError:
            return ""

class Kantoujin(Person):
    def __init__(self,):
        self._from = LOCATION_KANTOU

    def call_name(self, noodle):
        """
        関東ではきつね・たぬきはトッピングの名称
        ■油揚げも天かすもなし
          - うどん => "うどん"
          - そば => "そば"
        ■油揚げ入り
        油揚げ＝きつね
          - うどん => "きつねうどん"
          - そば => "きつねそば"
        ■天かす入り
        天かす＝たぬき
          - うどん => "たぬきうどん"
          - そば => "たぬきそば"
        ■油揚げ & 天かす入り
          - うどん => エラー
          - そば => エラー
        """
        prefix = ""
        if noodle._has_age and noodle._has_tenkasu:
            raise Exception(u"こんな食べ物見たことないよ！")
        if noodle._has_age:
            prefix = "きつね"
        if noodle._has_tenkasu:
            prefix = "たぬき"
        return "%s%s" %(prefix,
                        noodle.get_noodle_type_name())

class Kansaijin(Person):
    def __init__(self,):
        self._from = LOCATION_KANSAI

    def call_name(self, noodle):
        """
        関西では天かすの有り無しは名前に関係ない
        ■油揚げも天かすもなし
          - うどん => "うどん"
          - そば => "そば"
        ■天かす入り
          - うどん => "うどん"
          - そば => "そば"
        ■油揚げ入り
          - うどん => "きつね (うどん)"
          - そば => "たぬき (そば)"
        ■油揚げ & 天かす入り
          - うどん => "きつね (うどん)"
          - そば => "たぬき (そば)"
        ※きつねそば・たぬきうどんは関西に存在しない
        """
        prefix = ""
        if noodle._has_age:
            if noodle.get_noodle_type() == NOODLE_SOBA:
                prefix = NAMES[ TANUKI ]
            if noodle.get_noodle_type() == NOODLE_UDON:
                prefix = NAMES[ KITSUNE ]
        if prefix == "":
            return noodle.get_noodle_type_name()
        else:
            return "%s (%s)" %(prefix,
                               noodle.get_noodle_type_name())
