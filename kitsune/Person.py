#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Define import *
from Noodle import Udon, Soba

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
            prefix = NAMES[ KITSUNE ]
        if noodle._has_tenkasu:
            prefix = NAMES[ TANUKI ]
        return u"%s%s" %(prefix,
                         noodle.get_noodle_type_name())
    def get_noodle_from_name(self, name):
        result = {}
        for n_int, n_str in NOODLE_NAMES.items():
            for p_int, p_str in NAMES.items():
                if name == "%s%s" %(p_str, n_str):
                    result['prefix'] = p_int
                    result['noodle'] = n_int
            # prefix なし
            if name == n_str:
                result["prefix"] = ""
                result["noodle"] = n_int
        try:
            if result["noodle"] == NOODLE_SOBA: r = Soba()
            elif result["noodle"] == NOODLE_UDON: r = Udon()
            if result["prefix"] == KITSUNE:
                r.add_topping( TOPPING_ABURAAGE )
            elif result["prefix"] == TANUKI:
                r.add_topping( TOPPING_TENKASU )
            elif result["prefix"] == "":
                r.add_topping( NO_TOPPING )
        except KeyError:
            raise Exception(u"%s なんか知らねえよ！" %name)
        return r

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

    def get_noodle_from_name(self, name):
        good_combinations = [
            ( KITSUNE, NOODLE_UDON ),
            ( TANUKI,  NOODLE_SOBA ),
            ]
        bad_combinations = [
            ( TANUKI , NOODLE_UDON ),
            ( KITSUNE, NOODLE_SOBA ),
            ]
        result = {}
        for (ni, ns, pi, ps) in [(noodle_int, noodle_str, prefix_int, prefix_str)
                                 for noodle_int, noodle_str in NOODLE_NAMES.items()
                                 for prefix_int, prefix_str in NAMES.items()]:
            if name in (u"%s%s" %(ps, ns),
                        u"%s (%s)" %(ps, ns),
                        u"%s（%s）" %(ps, ns)):
                if (pi, ni) in good_combinations:
                    result['prefix'] = pi
                    result['noodle'] = ni
                elif (pi, ni) in bad_combinations:
                    raise Exception("%sは組み合わせおかしいやろ！" %name)
        # noodle なし
        for pi, ps in NAMES.items():
            if name == ps:
                result["prefix"] = pi
                if pi == KITSUNE:
                    result["noodle"] = NOODLE_UDON
                if pi == TANUKI:
                    result["noodle"] = NOODLE_SOBA
        # prefix なし
        for ni, ns in NOODLE_NAMES.items():
            if name == ns:
                result["prefix"] = ""
                result["noodle"] = ni
        try:
            if result["noodle"] == NOODLE_SOBA: r = Soba()
            elif result["noodle"] == NOODLE_UDON: r = Udon()
            if result["prefix"] in (KITSUNE, TANUKI):
                r.add_topping( TOPPING_ABURAAGE )
            elif result["prefix"] == "":
                r.add_topping( NO_TOPPING )
        except KeyError:
            raise Exception(u"%sなんか知らんわ！" %name)
        return r
