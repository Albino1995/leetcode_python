#!/usr/bin/env python
__author__ = 'Albino'

class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        from collections import defaultdict
        result = []
        cpdomains_dict = defaultdict(int)
        for i in cpdomains:
            cpdomains_dict[i.split()[1]] += int(i.split()[0])
            for j in i.split()[1].split('.')[1:]:
                if j == i.split()[1].split('.')[-1]:
                    cpdomains_dict[j] += int(i.split()[0])
                else:
                    cpdomains_dict[i[i.index(j):]] += int(i.split()[0])
        for k, v in cpdomains_dict.items():
            result.append(str(v) + ' ' + k)
        return result


s = Solution().subdomainVisits(["3325 lrp.rbg.co","8712 jeq.iux.com","1146 auv.jtg.team","6992 lfn.us","1512 jnb.hwu.team","1556 ocf.ca","1105 zqk.us","219 ser.team","1227 ytn.us","484 mgu.rbg.org","3855 cdv.jkx.net","7872 gqs.co","4870 jnk.mkw.net","7682 wqv.net","8013 btv.team","2854 ena.zfz.co","883 tgr.bfo.network","6878 llq.ksc.com","480 gjf.co","4823 knr.gdw.org","6222 hal.ca","94 zqk.com","1623 gxz.team","6512 hwu.ca","841 irv.network","267 xhe.network","4658 zqk.com","3665 gqi.network","5638 ihs.gxz.us","5063 fly.org","1493 jaz.kwd.co","9917 dze.tjy.ca","227 ois.gbq.co","7382 ser.network","3554 kup.vbo.us","222 eei.ara.ca","3042 gbq.com","928 kye.gjf.ca","6874 coo.yvs.co","5105 blt.gxj.net","8165 smw.dfa.co","3341 lwa.zfz.org","6290 wuq.fff.com","3685 wip.network","7549 dfa.com","425 tna.gqi.ca","301 kmz.us","9933 gas.srp.network","3054 irv.org","4678 prl.gqs.org","6065 cfv.nva.net","9587 kmx.us","9267 lmm.network","3363 tgg.epf.network","7320 fzx.com","7838 uzz.tnr.net","8399 yyw.qgx.net","2849 aon.co","72 gnr.tjy.us","5679 jfz.net","7969 bgq.wqv.com","7457 soq.wsv.network","8067 ajl.com","4420 ulz.us","2094 uyy.ca","1929 euz.zhy.org","2630 ocf.org","8328 wsv.team","3039 ksc.co","8160 ioc.okv.com","4898 rcz.ixi.com","374 rbg.ca","2846 ltq.net","2596 amr.com","4252 hwu.network","2451 ocf.team","6480 zhy.co","6117 gqi.net","4670 kmi.co","8838 jfz.us","4628 fuc.wph.org","9675 gqi.us","9437 wqv.ca","6940 lmm.org","5488 lbc.ulz.co","5859 tfm.us","7025 krx.arz.team","5231 xdm.jkx.team","512 arx.hkt.team","3061 xxp.uyy.com","9948 nkw.net","2838 buf.team","9513 jkx.co","1560 asq.cwn.team","6910 gjf.us","108 avl.buf.net","1781 hnl.co","7245 kam.ara.co","5864 ltq.team","9487 mhs.htq.org"])
print(s)