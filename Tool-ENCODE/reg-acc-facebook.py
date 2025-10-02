"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║             🛡️ FACEBOOK REGISTRATION TOOL - BẢN QUYỀN BẢO VỆ 🛡️              ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║   📛 Tác giả:            TỪ QUANG NAM                                       ║
║   📧 Liên hệ:            tuquangnamht2007@gmail.com                         ║
║   📅 Năm phát hành:      2025                                     ║
║   🏢 Bản quyền:          © 2025 TỪ QUANG NAM. All rights reserved.          ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║   ⚠️  CẢNH BÁO: BẢN QUYỀN VÀ ĐIỀU KHOẢN SỬ DỤNG ⚠️                          ║
║                                                                              ║
║   • NGHIÊM CẤM sao chép, phân phối, chỉnh sửa dưới mọi hình thức             ║
║   • NGHIÊM CẤM reverse engineering, decompile, hoặc phân tích code           ║
║   • NGHIÊM CẤM sử dụng cho mục đích bất hợp pháp                             ║
║   • Chỉ sử dụng cho mục đích học tập và phát triển phần mềm                  ║
║                                                                              ║
║   🚨 VI PHẠM BẢN QUYỀN SẼ BỊ XỬ LÝ THEO QUY ĐỊNH CỦA PHÁP LUẬT               ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

🔐 FILE ĐÃ ĐƯỢC BẢO VỆ BỞI PROFESSIONAL OBFUSCATOR + PYARMOR
📅 Thời gian tạo: 2025-10-02 23:15:52
⚡ Phiên bản: 3.0 | Security Level: MILITARY GRADE
🛡️  Mã hóa: 7 LỚP + PYARMOR SUPER MODE
  * Vui lòng liên hệ tác giả để được hỗ trợ! *
  Zalo: 0888385536

"""

# ==================== IMPORTS GỐC ====================
import warnings
import threading
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import re
import requests
from selenium.webdriver.support.ui import Select
import hashlib
import sys
import subprocess
import random
from selenium.webdriver.chrome.service import Service
import platform
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from colorama import Fore, Style, Back, init
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor
import uuid
from webdriver_manager.chrome import ChromeDriverManager
import os

import base64
import bz2
import zlib
import marshal
import sys
import time
import hashlib
import struct
import ctypes
from cryptography.fernet import Fernet

class _MilitaryGradeSecurity:
    """Hệ thống bảo vệ cấp độ quân sự"""
    
    @staticmethod
    def _anti_analysis_check():
        """Kiểm tra chống phân tích mạnh mẽ"""
        # Kiểm tra debugger
        if hasattr(sys, 'gettrace') and sys.gettrace() is not None:
            print("\033[91m🚨 PHÁT HIỆN DEBUGGER! Chương trình sẽ tự hủy.\033[0m")
            os._exit(1)
        
        # Kiểm tra sandbox/virtual machine
        if _MilitaryGradeSecurity._detect_vm():
            print("\033[91m🚨 PHÁT HIỆN MÔI TRƯỜNG ẢO HÓA!\033[0m")
            os._exit(1)
        
        # Kiểm tra thời gian thực thi (chống sandbox)
        start_time = time.time()
        _MilitaryGradeSecurity._complex_calculation()
        execution_time = time.time() - start_time
        
        if execution_time > 1.0:  # Quá chậm - có thể đang bị phân tích
            print("\033[91m🚨 PHÁT HIỆN PHÂN TÍCH ĐỘNG!\033[0m")
            os._exit(1)
    
    @staticmethod
    def _detect_vm():
        """Phát hiện môi trường ảo hóa"""
        try:
            # Kiểm tra qua WMI (Windows)
            if sys.platform == "win32":
                import wmi
                c = wmi.WMI()
                for item in c.Win32_ComputerSystem():
                    if any(vm_indicator in item.Model.lower() for vm_indicator in ['virtual', 'vmware', 'virtualbox', 'kvm', 'qemu']):
                        return True
            
            # Kiểm tra qua systemd (Linux)
            if sys.platform == "linux":
                if os.path.exists("/proc/1/cgroup"):
                    with open("/proc/1/cgroup", "r") as f:
                        if any(vm_indicator in f.read().lower() for vm_indicator in ['docker', 'lxc', 'kubepods']):
                            return True
                
                if os.path.exists("/sys/class/dmi/id/product_name"):
                    with open("/sys/class/dmi/id/product_name", "r") as f:
                        product_name = f.read().lower()
                        if any(vm_indicator in product_name for vm_indicator in ['virtual', 'vmware', 'virtualbox']):
                            return True
        except:
            pass
        
        return False
    
    @staticmethod
    def _complex_calculation():
        """Tính toán phức tạp để đánh lừa phân tích"""
        result = 0
        for i in range(10000):
            result += (i * i) ^ (result & 0xFFFF)
            result = result % 1000000
        return result
    
    @staticmethod
    def _integrity_check():
        """Kiểm tra tính toàn vẹn của code"""
        try:
            # Tính hash của chính hàm này
            current_hash = hashlib.sha256(_MilitaryGradeSecurity._complex_calculation.__code__.co_code).hexdigest()
            
            # Hash mẫu (nên được tính trước)
            expected_hash = "abc123def456"  # Thay bằng hash thực tế
            
            if current_hash != expected_hash:
                print("\033[91m🚨 PHÁT HIỆN SỬA ĐỔI CODE!\033[0m")
                os._exit(1)
        except:
            pass
    
    @staticmethod
    def run_full_security_scan():
        """Chạy toàn bộ kiểm tra bảo mật"""
        _MilitaryGradeSecurity._anti_analysis_check()
        _MilitaryGradeSecurity._integrity_check()
        return True


_PAYLOAD = "XF)+hK|w-qGjUZkOE+vVbV*WmVryq)b44;vH8VMGb8~HJY-l)ILRLg_a(Y8gY)my~SbAeJXfRn?MR`v!PDo`fUrTp(dNyY^ayV>NVr^7-XhKdoST<xdYd1wfc5Po%R%ducNHJ1XK~Qd2Ra90`dQMbiXE$S7V`NZOSZ;P=LQGRiR8?zkWmrRRT60=xT2p6ia%y5%ZB2S*SWs0#T0t~sEqYE&PEK%bXhlV3Ff?sTSx<RyPdQR;Qdli@Vr)i8c~eAYdR8++NpX5|cX&r~LPchJbWd_oM?o=bSXg;$ZFOu+WJ*DAF*Z3%O*UUsN@8$OP;_WwRx?*HGIVl9Giz>4Xg4@(R4s2!SWh=uQgBK^MtEytY*lPIOiNcWR!22sWl&KyGBk8EHF!2jVM1v(a8ookcv443RY6H>Pj^!>XJcqiSz~f=NJddXRdZEHUrJ|oaCu`fUvYSBT1z){c63NJR%S+ZOEYwNElgNqYkG1pc~v%3X*4Z&ax+XuX;ooyOjL1cGDSI3V^&XUb6IXSQg$$MGD}EbQ8RO2Z%tTjEkSWDQBYwqLs4WjbWSisWk_;ULwIgRLP1A)Rd7>va!+S*UwBL~Q)MwoXK7+HbV*7>Q)f$cUv^1waCtXpM`%=9Q(0tbIAV2Zc`-#cV_#K8MN3dcaaU<<MPW2BXhKplH8w;zcsY4bS6DD+N;zj(c0^EXc{y1%GA(6KP%=$2Wo1QEIcHx^WI0H0F;{ItR!?j)WKwu|WN&&jPf<=yVMB2<PDNQyXhdU7cWf<EFl>2iS7kzFI7&}MOmam?V|Qs)W>hV4MPfKLQek;&SZr@GT0<~5G)F;hXmoXYRdF#!S2t2iR#!DpL1i#{Eq6g^d3iZUHA-e?IYe%DSvN>uVMRf3ZZ~goXj)fNcws_LO*u|(dO=S^EmmK2M^;&GF-K2rQ893JVK7g4FgZg?Hg0k<b~j~WdPX!_XF+#yXhAJiNOVd>Lqm9HZZcv^Q#M0iOl>rHMp#F0K|^FhX-#QrPjN?QIWT5#R9I+KcrjKvGjMWtZd7h!SY=vyZ*_G|W@|!rLs?{XO-EK%YH>?8Nl8aHSyEbGWJWDDa$z`da!Yh|X?1TzSy)OiG;w)Yb#7KMYB5c5aX~|LZcb%$N@;5_c|k2-NOx#sL_>2zO)ye7I81nJS!7Q&GkQ%{WlvUTP)Rm9Fimt<aC2*4FhXx-Y(+9rO-ff)O*UFiQZQCba&UHGM{7n)aau}ic5G-ea&u*JRd`A^S2AftVtRRTF>5hQbW}odX*73KWOYzdGhb$NN;g$ScSK2Mb}(T?Pc3e0MKD!!QY}|Qb4*WBH*H5PG*V%7L^5VGL2Wd6I8jq!cxgjsVOB&)OlUY{OmR&_a&UP$H)?loXjeiuH&bIbGE8o0N@Zz7YeHd5c~wJ8P;g2!bW1I9VrngUS9ecXQF3uPGg5UhVrphEQcrb3OHp`pV`MWoUp0DYV>DW5V{J}mO=4v-RC-ZFMn^(UGc$NNY-&X_OmT5TGfqixR8C@XVM}93O-x5QH)LyeR#H?^cR@Bdc4ahCc}_<{O+#pMFfC_OaAZnxc~@g&XIep8Y;S5fb3u4iVRkWid1psTMMzL(Z*MeTHfL#2Z8Ui{Q(8$mMQ&I_K{a1xXjODbZd7tDF-L4LS57u@Sy3%AHFGpES87IAHBoGEG%|2EVpch1Z)aIoRWvp@c4%T>Z8ceFLs&RTc1(0lPBCjyX*N<yVR&+BdPh`nZ8v#kR&q2%H9};0Nor<jaCt~eG+9AuLOEq>OloOOIdXDSVM8-jbW}q`Pf##<LT7bCXGvLOadlZ)abHq$IbwHmV@E<mYiC13H+gJkP+~P>Z8CI6H%@M9UsqLDVR~_NZ)ZbBP<3TOS8zc{Em>t~Pj+o(bV*ZfVpw-$cU5UuP%%Yla#wRSby;a>H(66hMo(`|F?eEgVs=PyX<>3&YIrzuWJYFLcS~qca4}F&Z$vFZLo;MrGHY#ZLw0&dM0j>octvVtRbq57MoDsZO>=o?Y)xV@PGM+QXH`{gbyikuOiOJxdNy!*T4-Z8I8szCbw*QfN;FJyc28wdM{iejGf+%wSyx6dR8o32HaAdsHC0%0Wi?57Vp3#vL~L1jdO<f(F*q|;Mm9}(SXDzgOKMgzHA{IyG-NSkd2BgsXjV;gQ*dfic1ks3ZhAIYXm5E$aBVe9dNoCFd0AFtO=MwVc~59HIZsAGL~wLtL}o@YV@+dnZ&*S%X*or3Z#iy9QEo&*cTYGocu`Mnb~kQhN<u+$b}%_qSVAx|OlNj*MoU6sN^wnaSXWk6IW{&_OEOG0VKZYlXKi&~X=Zh3F;;a>R!DVGG-YyiLrO|iYczOiH8U__WkN)1LsM^MM{8ADL^nlwK{PXTS4dV`MRhq%G-g?Ob~$rVG<J1iO+{{1Vpmo{ba6;VN-aoBPgX>8V>U8LY*R&RS7A|KPE|%~Mn^_kbaO*#L18jPMNx4@PD*G+aBEOjR8v+@QEW|id316_YDh;yRyk`&G-Y>8HAq)@Y-TW1NmxN|VM<ahb2e9cZDvhcO>RqdO=4|GVQg-9ayLk8RAY8;O;l%cFmY&0a%@y)GI(}XYG*-TVp@7}VrDfhX-Ho+Z8mXZICO7LbVEu(adRznFhpopZ*xUuEoWm{OLIzCS7lmILTfQuL1bf0G-hf~OfyV2Pcm(8Y;03<Lt#;6WkgvvQ%f~LT1Z!9PB2AqbUAHpSWH()L}5`mPBdjPHa0PAZ8t4eabiX=X-7s!N=$Tfa9DCVcS&YxRZ(FyRY+DvFmYjWabI_4Q&urSYDs!6K~7ILc}iq4Rb@vlXlrnEVstP$V^4W+Ml*0_ad=5>NLXWQH!(_cPc2bpQ&lrUZf9k7b9QxSXGly~Vp48vMq^oMMt4|8RYgiLQc+PjayK_kcVB66LOEA0XGw8uIcY&pHZ^)SLpfP`Q&Cr9F*IdIaYA8FQZh3zUvX$QEkkudK{H8Ma$jsua7%P}Y;sFNcWH7mc0)F3Z!l&ya(6jQcsNZtdQw?ZVrMvJa!qe+OK@~&ZBTV_b3}S>QEPZ#Fj+@)T1{D4ZcKJJOHOMvYcpweUui8<VmM(>V|HvyXEjcCPDL?EdSXvzNK{vJLvBx3L^eZDUu{TJGHF9fF-b92QC2NDT2?k^K~F_>L~w06VJ%oRGf^^mMsj6FS#VZ)G*E6gXHs%(Qdl!daB5dWVR1!oXGwWyLSIr&X=8aeH#AXMQEEnTIB9E0XGSzcN_9{&RaQ(#S$AJ?aAq@UWoBh`ae8iNXE9??S2J37S2aU5W@T?ub4GA)F*bR1Mn!fpM@nRGOEpbabarx3WO_4NLuzSnWO;Q`bxJouS!->2S4(GYXJ}$rXJ>Uwbz)R;Q$<oVWHoeZIa4`AR#{pzPIz%<Zee0ML|RixNM}%NHaJyCNi$+?bS*V$S5r4%PDgl0Ekb&BFmX$6IYe`7F-$jFRdiQ1X?k#9a%yvVb9i<&H#RnDGEZN5IBPIkcymKJLQpkSXGm^nH&;wFcyCi-WK3yic0*)VPB&0DS!YK^c|~DxWp_ekM`To2M_Fn~SVv=1Swb^QLT5E=Ms`+NS8ZQbZgVj+O+<GsbvH_CczQTccy@X@WNdO$c0*D*P%=R{EpswiVRS}cN;E-kF<5CsXiIfpYfn{XZdGJZNo!_WRdzybRYfvGYf~*kXLeO-Sw>ZQRx~$IOHXPrVNr8wc~(?HWKv8tMQvYHMNut7Vp(^3RZMG6Xjx-sGea$6T1RPgUtvK_FfuJec{oQwRY*=~Pgi1ES8QlDPf=1qZ)|jSc4shgOiy`2YIRO+W@&6=RAESNT55SkGHP*nQ#g5TI8jbhPI-89WO;5+EpK>sG&p5fG;l?4QgB9TW=1nPS9D2aUpZMxaCT5OR$p~vOh<EePfckuQ7~y_SVT8-R%bz1G)H)5NO?zfVK`(_Gj&Nsa4l9vcv4hDZ*)>tS#f%FHEl9hWLHUYHA_o&X-`CHRa0eVSz2^9F)?aUdO~z}V{v&wLt1orHA*sRGg4w-ZA3J9b~AKxUq@$7MKe=QRyA{3W?xWIHfmIPZ9!9FVMughbvA2MaC0_aLUK@bW@}M5X+m01Yf*A+c~4AVZb(dIX>K-iOLAm#Ia63mVn=gTLTWWiS!+W#dNnmOXh~;UNmW#Oadcr{b#--1Q*>8oWJxebZ*WgkY)COsHDOjnGedfHLvC|+WnxNUGcikbPhn|PUv(`<M^QI-X=!XqS!ZflVlZfLc~NC+N_22;M^Z#?Yic({OLcflLQzIZSx_=)L{~(2Qf75TOF30USYc{(QB-DQZ(}$?YeYk5Hc4VnOiNNnSxhl&Ia)MdWKMByYg1}sb4N)`MN@Awax!LjNN-hYHf%;`ZbD{HV@-NANii*Vd3JhbWHMx8curJCGiG^3Uw3#{dSzi#M?o-XPh&SsN?2i6I7)C+S5Q$%Pjz`^G(lr?R8?+9bU`>ULuoc@R%%B{WOqnSY*ROPT1QWFVsB7ZW@#~ZGIdi)Nmgt&X>V{hI7u{GQ%f;RIaxMmNoPxNX>VtDYjZL!Lt}S(M>jHOZZs`%LT)itPdH3UIcjK7Q$=@oS5$CQIBG>QVJ&4rMs#;<SY&xaR#SRGQAsg2HCi`!b2&Idc1me=GErqkR&{e#L3(j@ac@ynUw3a`Q+Ih+VP<hxL~ulRL~VFDX=q79RCH5VZ$VW^GIn)mZgWj|XjX1xF*!0xV>3%iG<SM&No#FOF-}rANOU$yNP22kL^5${H*$40Pe)NUY)V5$LRwK{Z#Yh6XmD&uUvyVQQbuTIGGTH=W;aiBL~l?*QgTOmQ)xnLb6I$7YejBxMrT@BX>3nKV`f%xR!K^FWJqygMM5ohb8>f2H&ktBc{oT(QcE!{V@qptWLHi?QDrc2Ml?}1b~rd!MOs-hFk~%tSw?7iWJ6zcNn=)bW;AMHZE0z6cW7f&GG#b2N=I-~W^HmgN>W5JT1R7PXLfpRH%&}fX;y1*X>3JAS~){=by8zZM{jCYXG%^{G%`$6SyV=2Y+*N1LT*NQW>{`DYjZMbML0M?a4}LwMpk7qG*xLeZ#H#scu;IsSWi)FYAsh#HBK;dP+3JrNKRxoayeNoH8W6fW_5XHFn3CKZb4aCN>*e~W^hwtQD!w)N?&4lc5qr#S9ncUSS@8@NknN@OgLyXEig-EVQE(}OJPT8P)b!{I6-%8L^FCdOjt)bb}?UZHCRJ8b7XQdMoUReEizX^VMAp!XlqbvS7j}8K`}^TdN@LNH*siBN-||(bTvkIW-V-5R8C}MPfTY;Uu`o)H+Xt!PHJyXT5xPKHZ)5|N<w&9V_!!yGev4nGiy>bL~~3{T54H#Ge|gYOKM0tWL9=YOmRkUH9|CBLTXuJYj`<gZ)h<~Y*#fgYDP0cT4!NcOLSv)XhBnET4i}-GgL}yN=i(1OD#D<Y*;l`F=<V5LpNefb!K*IRYg&HR!MboWN~^hV^(2MIB|J;YI!wQS#&u<aAa{~cTPn&GIw@TXJmFnWKdsrVM#4(XGv*SGD<{ZWJpR>Vlp^TZANfqT6QyURA(?ZdPQU~cxrWYLP0f9SW-7IH(En<G*4MqVOeiwb#-E4cWg;RF?4r9R(N+sI5A6hQaE^DFiBKOZc{B*OGR#SQCfCaO*d0?Z8<P#Gi7B_c4=ZvEjLwic4<aZZ+J6IX;EW$LM>=XP&QIaFm_IKQZPwKSTQwhPikLeOlC(pYBEAiElqc7GgEXyGB$5iHbO8nR8m(-VMb9cVKq!hZ&XT1a&=UCQ*vf8STa^hM0IRsS~Ep5SZ_8*cR^B5aAq`VXLNQnZ7^s|IC^1La9A-mP;N3zS1n0xNlP*<HE1z+VKFmEWlC~Ra%4zmLu55XGHf|fFg8nVR5x{3MPYa|RWN8xQ*3ukMtDtAS7vW<Lr+OCLsD5uM|5~tLM==!YcP3OS3_xeV^}e6Y%*nKbzes_PBCX%ctvhwX-;QtM?_;cOh!|3HE4HQRX12gZFW;hR7-1NG-^&$V>4q<H%(+%cTQP%L0>U3ST|ZnL|S%aPj^BzOENH0aB*=(bYpdQZCPk|PGvbwF-383LNrb=Lq&8@bV@X1RAELrLuFx1H)cjvY)W5AQf@|OXj4a2NLg@Ha5z|MX;651Of79tba66fG*EVMQ9(CKQg26ELsU0-HfJ$!G-p<8Z)a{+IcYX}Id?KePIWLsV?%6mQ&40!LTXq^OK@>lH+e%=PH{*@aY{u>ICE4jcQ#jXP(o31Oj<2ULqtVGcSJ@|Fm6|2R8w+ANmpi9Gc;-~ZAf!+O-OPvV{>R%MoTz1b8b0wS$bnKYHWFKPEIjGYI8_3VQXbAP%>9hcu;FZZ+c&2c~nhGHhN@lIciT<YBf+nQhIk|XE|76HgQ;RG-PUFP;@g!Lv?dvS#)o2a&=63W>aHHbXP=SPeE^LHB&KiGk9@!ZZkPFM>cLoOm1yqYBx`CM@nU8b9Y&0VJ&A<a4lwWLT+kHN=!jEPIhH6RXAl$ZAf!*Ep<&Xa&%)yPi=ZdXIgMLH#K5NH%MzvT1aDdR!4GgEqFF+Wo&tRSx+r6N@h}NSW|jKQcGklR%dHCF>E$DYGE=?WpGh-V{AD&QFlaTY)CduXL@cqPIgU2cyU2-RbgdWHZ@CTWmjWGW^{U1LTOYvby8SUF-cEFL030bc`-zAV|Ya~Lu77FcVcsQZb4ctcuG`ccV<;}O>kIuP)tm2QBFs5V{vU(O)_+MFgRFBIBRQqW^Y+EW-(QCHDNYdO=mSqOlD6pZ8B$ZUv6(&NLpeuXmnp^M>02gR76@~R5ep%VK+*8dR1>&R!Kx-ZfQ3`L{LOEMl?BcOKneWVoEJET6#%Cc0w{ZNM>wFO?qQfIWbmiT4QuFY(_0)OJ+AjZclAzbWT!Gc|=A`O<`11W<zN;MpbfmHhDsGdRbCYQC2i>HF<eea9CO~a#v$yGBiO#NK`^IS~*sBO=LqdLw0ImIZj4eG+1v@HdbM9Mn-8cN^fg2G;S?dP;g{fV@-BXSbA4cO>8hvLv%%WP*6`*W;t+fXj)24LUvYZZ%jvKEoNbFb8TNmW=(fgYBN$_LRLdoZB#{NWo}PTVO338PB(N>Pgi13Ibm~mX*oD?M`Kt;G*M1fcS1!*c4{<3P*iPMIA=I?QaDFJaaL$)QA$r@H&1jzcw<;CG-g*)Ur}XMVQP19HfDKkNNGtpa#%rfICn-jPiAX&X+&%?M{-MJXGwNhOEE@8H!x^ZOK*8;EqF9nMNd{ZMPo2`R(LjaM07_qV@^Y8V_9ZNMMF|CN^NgwI9E`2PHs0wXHqaQZ)8+odUJD0G*VYbZ(m4BH)BacY&J1aRWxdHIagRPSY=IBI7T^oW?x}*RYEs-Q8`mrYIS)+SaL;6YE5u#OL|l}XHaW7XhU*FWN1rJaZhqBGiXS8Z&FooQfgF5T5V!tXGdr`a&2E_VK-}QPIgpdVrM}@SXWkKLUDRhNpf&#aWQjeZ)8s`Em>|fVQErvGH^~fNmplUL_uFea58#Qa#DFlP)$K!V`4aQLuyVqX)<nSNH%qFWH3=hH)k+cW=u_4b8#?gQEN_1cXC--IaXS9Vs|$-SVT~1L3l@BZeKD(b471LdPZk!bZT)}H!@*iN@7NAa8)xcQ*d!jbvQL@Q!-^@Om9>zUvNxrRatpuaY$}<Ni9)HL1{8WH)3^mFltU;H8(*<Y-KlNctb^UWJft>NJCmTc}`ACX+=j_ZF6{VP&80wW?wZ?S1mbuM^kHUM`Tw*MMOe(L`P^(GD%rYV{&G3cUmx2L}M~~HDpD2M_+eNM`uZQK{;_zXJT(@Qdlxlby`<-S64wnXm~?VdPqx5Q%`AbZDB$)OLJptWlu74cuh7<GI?ZlHgZ>MOmJ2?X>xBeLsm&rXH-})RYy5wUtd=+OjUPcH#bmAOIAT{ZF*}%ctUJpMNfG_IBIl3HBE4JPB~FyH%3QMQ)**+R98+)H&ZQPP+wR@c6V}WGiWVLSaonQQA}$$LrXVBd16sSa#J)+byZDhEoWm$cXDnsPIXXePiA^EVp(xzLohjNUod1^Y*#o%c|mS1XiIiPK}1JnNLE!wcUMkOL0MBWH91O0aZW95aAadbXKge%S8`BPcQs5mN=q?yGdXKFdNFlGMQBHKX;4CIMnrZ|LM=@+GfZ)LHgj%lWl&>ANMklnR&`H!aZ@*GayT$gHArt%P%>{qSYkm}Wpp=MVL3T%K{9YvVMlN_OLsv~V{0-&Ye+U(Noj6OWH@&%Uw1HdQB`(ER6}@XFiLGPS8zpFF=297OH4RPZ!KeaMrKo5ZALayGg(4UO=L(mWl?!eIBrQpVqrLQF=t_Pb5Ay3Sz$s^bz@UARC+OLHFa@SVrY4GT2N&~aAQ_db~9N`NmzD9O=x3kO*3vtL3c1jYI#RPY-vO{X<tHmN<=nfMs!SfNNH?MLTpWJQe<H`XGv&ELR3ymQgBXgPfT_>by8PiVN+E&XL3w4M|4k4WK3{SPFY_$MPF2UW@1fecvNjsYBFSKSw~-YW-?59Mny$8bb47+K~iIAXftthS6@>>cSdz^Gfro8H)dmOdQEP1GD|~wI8s_uF*i3gWovPIIWa{>Qh8NTGFVJ!WlK>@H%l{gIWRP2SW0J4X?S{dHf}{YbWmeBcW_v2b4*4tRW)u-XG3RSG*3iXM|o;=aCKEtSS?9#N=a}rH8^E=Q+8QSb98cMS!-W7SyfP1QAcYyLr-#2d2ViZOi@yKGIDb{a6(^eOF>3PV`wyHXlOQAQB_fHNLNr}R7Gf3S9wM)O)*MjZB1!TQ#nLJOixy0M@Ts|HfvUKSY$YLIeBVgUr}>UH*#=kEn`JQR$p*sH)B?2VoF0&SY}#LRd!=_M^0sWQ+0THZdq|qId5VyaB^@`Emb&gaZ*!cS8!8ROfpbrY*k}0VMT2)R7p8wL^Er6dT4k}HA!DsLNQ5iR#az2OF?ycK{RMJLwQ+BV`?={a7a`$X-|4`F*tBAW;acAF*a;kM09R&GH6wFad~NRHcx0sI5=x<OE-EqS87l)Ff}+dQ(|RkHDPFLa#u29Om8q%QB^Z(Ml&{Va7Ix>PkKgISZFqEcT7}GLPRxZUovh_XGKkBM_OM|S~hlTRZ4YBN_uiPLNZHpY&1-AV?=diY<72OLP>97L`zmtQ8Q;SHbF6CH&94XHa0MHNoG!1FjiPYQbad$Q$%lYO>!`KEkRf<d3sZ9Oi685WmH6KX-Y|BaB5OCQ8;-+Oh##GFjs10M|yd1V|rz9Zgp#6V>nrET5EbyWI1qBYE4;nPEmAmY++7!ZbC^{R%du)S7bFyP(*bwP*rqsa!Ge_RZwv`Lpfn=O?PrQb~Qq6VK;G2a#B!nOH5)yX)rQ(ac*r`ctlB5P;Pi+WoczYQ&co=GjvuqbVO@(VM;evSxaA3Z*^vNZCEl=Yf)KgEo?AUUvzA0XHhj;X-H9HLUd0?ctdq<LRxP(c`Z|QcX~}^W@=btcX@ewYc)tqP;GTBXlr3hYfeI9Q)pUsH%v8VRCsx3Nl!UAc6n)aLQgPhc1dnpY)WfOM^{o`MMqLtVRlqPQ)6yQM^H~KM`1*CVsbGtL^4KSLUedCa$ieRbZ=;FWMf1~ax+PCZ$d{gL}El~VmEAabYD3{a6xWYGcs&KQDs_9XLmDoMnz?LV{~6|OH4#!c|~PfQ+aMlX=r9zc5+f@aAr49b8tseRXA95OLKQMGHh5^PH#|ZG-qa5Mr=t@ZDK`BGeveeOgBa?Z(?OuLUv+qadu@jNmN%yV|h4uY*JNYY)WQzb#GEnXl!CmK~pw3Z#8)`a!hzeacN0mLPb|-MpSfHZZbtQEk{#zP)2K6N^oyRL^)7!VRJ%CX-GqFGIeJ~X-Y|CUvqU|Fi2lib~Z*%HDYvRGFN&rX>Dq6WlK^}a%DAcNHudgS~WFlX-;1`F*R>PXGTF|O>$07R!CwnctUeac58N1GiPT*NM&tsV|X$xH$!q%Uo>G*L`rxvb5Lw;F-3MvY&ULaVmB~Kd0JsXbwPAwNj7msZbw2_VnJm~S93OTYBN|hdPhucN=8mpZdNT(Qc^K?UutM?IW;zRHZx9aOHyrCQfE#~G+1+RNMA8CMRhf1bVhkLNkwl^ac)#+XHRW8XEAq6P(e6Cc~Nd_R7YueH$+EfEoE<VPEl`3F)cSaQgBBybU8<CH(E4UHcn$<Z#6StN_I|8IX6L2G<9E0ICw)>b#_Hpc{Md|Oj2-laz!?DHEU8~b2NBnXKZ$Ga&b9Lb7E*vb8kaWIXGl%Q$%erH)Bp>Wk_s6RySf(OJ-qoM|X2LQ8_kobZJsEF=bRSSTJpNMon~fcsEW*Id^$6MMiEiXjoV?PDN!hMO1indNp%JX)tp^a6w~iYi2QKZeK=1PfA32HZ*8+MMrQoP;NG1Wi>NWYEDWmEni4<ZaGFvc6MnoGjdUSZDd4nGDkvpc5XFOYf&<EWLY$FLqj%sV{l_+YB^d_N@r_xR7GV(Q&mz_Om1{*Re5(sbVo>UEpBT$I52WyI7w<vQ%F~3YiD*rdRkXaT1iJrRd6kDSvhu8ZDBHOOKUbxR6}h_YBfPPF?mKtNMcxJRAEL?a7H&(SW913S9EqpYeiI5Pjg3cQ)yLMM`KrXYePyxY&b(pSTHn2b#7@_Q)E_mV=-h;ac*#Ga%(d|O;JumO>Iv@bUAA^OGS4@NMATJG;ldIS$aZRZ&EmOFkfv)MQCMlUtd>FQfxVASXoYQVp=U!cWh00Ohb5cF<3A{N=-{yH%Lo%YDF_PGEFyYc4bvEb7W;qWi?GkXK7hWdR9V8Z(mV&Fh(#<I7vrDRZK%RRWfyAT4iQ7F-2=bPi|jgQ))~|NKSe~G*VA+O-)&5PcUslYe;T4S!*pqFf(FUZBI`}VN6PGLqlXWW>{`|WI|GCM_6k`Hh4`?ZFyNYdQmu0F>^vSb5(CjMrwF-LRnK)PG3uQMR9g5G-Y*jT1hQbbS*_}IB#!eG*C7{Hdjh8O>a$WWjIDxR8crfR%U5QGIw=BR6#{UXmDmlLNqi*cx-qxR9{OqIaEzYQ&CD~LS#uXMR|B^SXeb|L0@e}XJ<2PW>s2AHbP@{bWkyNS7mv2azRmbba6LiPGl`JHezLEazRQ<Sz$4DFkv}WWMg)CbYwM0cVt9tRzYzwN<%nhHg|7sN@;g?Qd4t5SU6Q}HA_NgXhcYAd2cu|Pjp06RYyZLVPi>aO-NC1LtkoDayW8IMnrZwc~DArbuDdSa7{x)IBHXOPg!|UVnS6zYgbcwdT~Z%d1rBHGIumlMr3z6Mq)8zL`7|ESwwI%Fjr7ZGix$hHDpycOEqg{M{Gz^VmNCyOE4{Sb}d#>ZEaIuXfbDMO?GrnR&{DjSw><@RclN%YH4>dWk+gHOiMISY;7|_c6UuVElx)<X-_g)GH*#@Lqc_7b1iFQaY#cpacyC9WH>@~aB6Z{Qh7N-I7wPjQ$%)maWybxc}Q?EM|w6xQEgCDXh|(eHfc0aUpGN%Z&G7)RbfqIV{%S8FmzvEc4t*zQ!p`aMpHs-MR7%PVnt*%F=$O^QdDPGM|WX!G<sN4NM<#1OG-;&S9x_)L18p&cvDJROLAH^Nl`d7O>j<9G)ib+YgI=^M_71tP*qD<F-cWQLSij9NK;2mPhV0=aB475b~SlbVp&;Ja#cYwb8>fPEn#*<K{YmPK}S<aHFI<|VJ&Myc~WRvPj^c*FnVP-IYLx<I7Mw$L}@r>Y;I#kVn|D6Y&2+0GGtFVR#a(EHdIA-RY5RFGdWd5bzf0<HCRYRIaNnXc1SlyNOVs}I7d!UR%~!uM`CqBdP7DwGGSzSSyDN6bwx`~NHuJ1G<r&Ca#BiAWouVaYC}19cvn|6ReE1eR4`6rEiF+}cQrIhF;g>9Q#4m!R&zl`YhhGLHA-z?V>eGTH$g#Zcrto)ZcBADLuNB_M0#X&Y*Si9GdD<1NOeRra7T1*b3<iBQdw<oYDhssNlSTgQ7}(YEqYlkOF>F7ba-)VV{2=0ZF6HYYHw6xH)b<zPdQ~tV?kkGLN;!3O;KraY;9?7NHSPTX?8eYdSOR7F*A2xYj`zub3;o)NpMALO>bp!a&u8*Npn_eW=A(_VPjNvVOn!HR6$uvZ+A#GacOf^QciPeM{8wJNKrvcQcyHnXIOYiYD`#cQ%6=sc{x{fMrm_-R$^s2d0$6pa#uqzaC3B3F-&)JUvEimH#l&4L}prJXiQCdGFoF$N_ST>MoVEdV^>92cx_WHFluynFjH7fX>3SvGD%o4IaYK~N?}?~NLqDFbXQ4eY(*_idNFZzLU3|%Lt%4MS6FU1W_NfrOixx<OJzZ1MnghsY;IUXSywGZc}+uYVn%c}H)2G3Q*AbOX>oH;Gk13~QZrdNUwAcCQc+oNcyo1iYg$S<FjPlTVncRCXHHL4Y)*Q0T5vWnPkCBFc4lQkO?gZ<WLj5ON>olcLS|n!P;PNZIWjF+T3R`BGebyfH+E<+V>U@tICNomO<H0`RY+=dW-wPvdU8%$VnH-fNMkcuH(5DlGB;mDW<f<XNoZ3<YFJciZ+Lc7WkzXMZ(~+8LrrmdMr$=;S#(xvSusO0Xm3?jHDq{face_%XH8TyPi1FWP%vd;S7TFgXlZ0sR!Db3Q*L)RYe_grF-=5bLP|$NR!?(bPH#<YF*Qs{aYbTjP&Z^^XF+d8F>rEvY)o}TQ8G0{Sz#?qZb?T{Rxwd+bXR(FWk+aKHAHMmZd7tfP*!1WS5+-gM=eomc5qj8Vrpz|RA)muXk#-^S9nrHWmPswUsY#Ab5>YONLMv)G&4k6Rx&kAR#j+lGE^;1IW}5JG%#poYH?0-FmrH9Wk@kJLvBV&QE5$BZb>s!O<z!SYiCPwcUCfXOgL?5I7dNrYE&>qc~>z+L_v0QH)}IOFf?mTPDV~|Mqxr?Q*KyVQ+RMTNMBZOb~8s(WJPl_LN!!0FhN&LbaGT-b~$r1OE^qrb1`yKQe;zjZ*FxtN>DU&Oj3DvY;QSIWN1%Cb8$vULv~kCLV0$1IaF?HW?^DTIYLcgY-w6+HdI)7Wlb_uYgI5sVMumoO-)TxGFUfBIdwNzL1IKSZgEaQYg%efH%)PCbYwF*Xmn^YS5rz(NLWo*H&a(;Fl0qBGiP>BV?<d`MnO1iS#30DM_)EMT1<LPY;;#hMRrtcN=`O-H!U<zSa2~dX>(*jabGevS9(u2Xg60`XGm>IN;x=7YezLxGe}2gPE}AxS7LZebwhMlUv_X|No#6BOGz^_b2x5SNKZsJG<HZtT0=B$XGvpqPijb1RYgrpX-hF?R6%1zVQ+6!PkL)JHf3pJLTh4XR%29fLoHcSabasPFivY@SVwwlG&E~sbW%uaMPE=wdP!}1EmKf;P(f5dM`vb4HDgR~MOQabT5U0BNi#}UIZahjN^xgwElX}>P(m^`VoZ59aC3KOb8bmwNj6C}XKG4zLqj-pF+^BubX9O@ZZR`MP;yOoNlG|rNli&)Y*%VCL{}|kLo`HCIYc!=VNhXDK~FO{OJ7fPZ&OBDbb3K%QF=HuGHzE+SZhmBG*n@1X<9-=H%2#TQ8+L-H91x{bysR>c}{L-OJQ|TZe~JoEoWFYMomjuXisxEXf`=(VpKF}HFa`iW@1QeMr%q?XIC^|S~y8|X*o$WXEHK5Vqar9c}HS(byjvZc1Uz+LrphWW>Q6IN=#E^V@75)R5VRPI5JjJRcJSLUsFj>Zdh+ua#(YBZf8|bVtO@Had0weaC35MbX9mTHfBd=LPu6NSz%*TLo#VOQ80CLQ!r^bXh}zONm@BAW_oiiHh6ATX=rOSYH(*!bxuxiG+A&@NI6qzZE|o%Y(a2mRWnd(VN+#xEp0Pma6@xPPiALSPf9jZSxahoYHn#yHfk_oHAz-qXmepna5Zaob9HE0G;T9>W^6PubxC(aX=!G1LUb);LoqN)Sxjp=c64i5Rc2vkWM6JkT0uudX*oeeWkFSMEoW|SMs;mccQbi+G*4kva6@Nmbu?dVNlR)-P*pH7PdHaqLU&JgaCJ;qc63WoH+FVvL{4EgG-hH)OhjjSHdk18ICfWPS~N0kNJv&@Ur9N1I8ZlOEpkm*N<&v+VR=hdLPT+MEp2#tOlN5}R6{gjGgM}5QA%tvI5;#dQf4)CSygsqNKa)|YI;ppLU?XebXQbPVpv96Z8b1XEl^iwPia;;Xg6+XXH8^QFmh{gH+OhMYHnFDFl$p}dN^2TYfpMGGId#HFm_c#VN6(OZeetHQ*=XLPH1R!VR2b{O-)R5V_I!$S7A3cW>Io!OHD{qW@lnBIaG2pR9Z7ddP_(*M>cnDGc;#$SW{U=dM$5wX=-jnElyH!QCMtca!X=oYgtxVNHIZ6dN*f6dTCTyZE$BnLPj=4HF#Aqd2dQ@aAra?LUna=Q8sXBWnyDhXKGAsc1n6vXnJ%^WqNW-X;Wx5Y*=VWFn3T!QFm=EWoCCwW=?QHUuZ`$K}RuPHBv-lc58S!MtWFuRZcZ)LwI8~Ni;-LL~=uJd2B;pbzekgP%~9eadJa$WpQmoWj9D)YIZX;Of5%AZ%<cMdP!_VI7w%ELR4XAPeycib69z4a#&?}ab{s;aau`AbWvk%a5G3xMKLuvO*2|mHg0S)V^K?aS!YRQYHMU~H*9TsX;OD;YFAZtdTKF9X>N8<G+|9qS!{VkN=s2OK}t4aVQqF*P;PcdQ#52vML9EabU|1#WNuDWWll14RZ%oFHe+9PZZ%j-LP~L0YfyMmdN4Uta(FOgMsHt7Qes+Bcywn*a#cn}F;r|tGhs@0Qbu=5X*O&~T1rYoMlx$bH8nFdQb{*uM|VtgZ9;BuQB6&6NO*NJT25|OLt=DCPc~yxL{M`vOK5dVYiL7EPF7?yWOzekVp4c>P<ldocX~2pQEozKQEoy@Ohq_SI8<U!ZE;aBLRd~|N?CeMOjdR^Us`T<M{hJrVs=zXNL5WmGDLJTM{PJTXk}-4Ol)s;Y;9q8csO%VEkQU`V|GbXd16jla7T1Ec~Eg$YeI2xK}1A%N<~LbNH}(IOEpMOLuqzOXk$WIK}TywUr%C7Uq?-FLUU<ScWrN0ZE-kEaV=D5ZFf*oL19{FVKZ`iV_{G@V|ZaPWn?yHLp5niWp7YUXJ>9WYH43BP)SXAS~+zxSV%Z%LOFOrPee0ULU%Q6G*NF#Wp8J1LO3*XOk+b%dUaScG*Ci9PAzCbW^Xb~WpYP%Y<GBNPBm6vOJQ+RWJW<lcV=j9Zcj!yFgQ#^F>FItYiCkOMr2fJVPq{%YD!2|Y)NQUbZt#dZ89`RL1|%cH)L{ZR!Dj{c``9?Z*Fx=M^a*WN_a7KQ&2ExbS+;kZckW2IcPUDSXNXpaYSoKWMpe?RYO8&N=kQUcv3e{VOmyLOm9wXH%@g+XJJ`$HdSO<MPGPkRxMFeFh*8qS79+`ZfbdGS~*TJP*Pe)HA!<$RBC8RSV>29FgSBLbwpE1L33GaZ%-{ZH$+M}IXQG%V`F1@Wpp<=M@x26OHxO5Yi3JKYgkxWOE_guML9K6Sb9`aS!`KWVOc_MQEYQkZc#C3H)}CVFf(&ZY;ZVANm@r*dQUKMRcmWwWkqH*Wl(5RdP!J%S8+LJMsPGSIaM%cGfH}9Wm80CYDP#%ctde5MO0B(cTZw@b1+{;R7Ws5c1?CNLTzqma!qSgX+&;fLr!&RMp|%VVpv%=Z*oI8LP;<+RWdYJT3St7Gg>(}S3!7mHc&)qT6Ho{NM~YER8KfWWm$JIEpJ+NSa?iQS5P)-c0q45S!+2#Y(;W6W>YnCP;f?hO?fnCMMO$@RdZBYRBkbGdNf8=XKhhdV^wWzZ$dalGkP>dc{fLTNkL6@adUBHPBd0IWL8*5NN00sb#FmAF=#nPb$3;5OfYpdF)c7?V`w#DLUvVDa#KQabW~P3byIFbL1s8?VNQ2)H#bvKUv_$CXk}`6ZD~$zbxdk&MN(F0a93@5GjvQaK~ZgJY(#8zP+Dw9I5=Z1WL8pEV`fWFK|@q>a(G{4Wj0iLO-)N-PFPu0LV8V5GBit5G+|A1HbHrEVKzf$VoqmyRYgd8Z%<iBO>KH#W<zXLc1lJ@YdK?6GA(IuSWjj$PGK`yVP{HJNJdLVP<T^$Xh=0PX*hRuP-0eAGf**7VoG^*Fim+@OKwF*P)Jy1advP;cT-VAZ&^`hLNiKhWmHIKGjefpQ8zSbYfLgiL03dKT2)bVbTv0&S4d$}ad&iTQ$;~UHhF7dSa3*jUs)|vR##<VPDfKjcSd+QUo|ywcvWLILULh6R&sPvIWtUUMN&~lZ%tH1EmnDFXKht%Ye-9BW_fopGD=@XaCJyHF<4VYc2rqVGC6KHNHI2TV{>M5IZtYHVMlCQNknORSyxp>H8)dwc4BZxOE7U?Eo?bxM?!3LF-&h%HbzuNZ%1Tnb9QriL3eF(HdRn_QD`wYcsOQlaAQ$YW=d#GHg7^zNqB5;c0oosXJa>0HFi=^c|mtgZdZ42cWh)ZPj*ORcWN>=c2-nnF?2X=LsWJxb!s$YWp!FiNH}3xYfMi}IZ8-*HA-(mYfy7TY(q&ocxHN8F-&)NXj3tGbZ~HQG-zxwG)`ngUq?1_S$9}NdTm5yR8>nyc6vlbLp5h-cvEv~cvEXPOk-MbRarT8OLk;wZEZ+qWKKdeXizb8YgIx{MoDWjFhguuLpLo%M@?C7Em1Q?GE--EGId39RY_TNK{rD(L@hQ)Zcjx=c6WGiOm=c#MORrtac@?7RCzXJS7|v#G*>i8SYu&pNqKp7baX*NF+puMOG$4_YD_ascTF=vYhQ6qIALvZVN+ssYeP<HGH5qASvOxoV@*Y0M^{*PV|aFSM@dOabwgEGb4X2JXhM2aSxRh4G;K;UPeF7!WkqmMZBtoLR(4o0a5z<ALNZE7azbrLaW^nfY&2m}QDSsBM@w>bSxZz@Y+qt}OGi?0N^V+VQfyyNVQ5ZhLUL_#F>!TycSCJBQDreQYB6a>Mp<ckXh<+bS}<c|GG}*WZa7eEGjDceYeH#hdSz}iOi^xVNJMoqcy?McMt6EgH)2I*Mn-u=N?2}8Elx~jHdIM%LPv9RLPSYZZ$@WSZ*na~Uv6+^MtEd)NJeo&Uut$?R7P}UF?mjAMq))*Id@`jW^q|HO;Bw%IcH3Hacg)_IAwZMSWZ+=I7DqyW@=GMGEp*RG&gQ>Mr3+*H*<1JWlKawV{T7vMNc$NEonthR%uLkF;_KdEj2AfOh#jQG(k*Ab5>eML3S;AZe&GnRd_UMd3QNiQ#V6-O;<HcYF2hvWMNuqUrTT{R#bImR5EjASaVoUZgpunLq=qBcuH4OM@~piY<5LvMnX_mY)>swWNb%FEj3e8V`f54c2+evLoH=DX=_w-W;aq%I5J;GS5{+TNqKBcPiJsVOgVRUPFOQ&XKFcDPfce*aXC3LPDD3Fb!SjVEq6^<c}rPMY%*#wX?H_nNJK_POJOiMdQ5V2Wq58#Hbr?vQ+8N2FhNjxEmJgEVn;_}dUsb&GjMNcNp*O3ZC5olX=7wWN^wSWPEJ8}W>;iJW@1(`T3T;yP;zorIAd^iLNr)fVp29VO=D{?Ibn2WZ$)86VpCH>Z8CUlcTQh5H)t(sWI;7&EjTxHb4_V9Sxr}TVsS=6I4xR7O=U+=LqTn0WpYJRXGnH&ZFovVZDTn#SVV4BOle_ZW=Ll+YeHXHV|q+tMNCR^cwsYEc62mTb5eJBEpcO4R!?G8Ic|7*G-Xm*GD&80Lr!>FIA%;VF*Z?OG(llPc~UhnPc24rG&D9(Hdt<Na#c4^GfhHTS$R-7Yjs*kb~8~iO>$;1HaTZRW^Xn`W<hLXZc%wncSB!UGImXGb5UAYa!gMxdUixMXgF*zbZ1UObv99IZbC^xPcUyeQe{(Ed0$sVPC;-vNn>U+aV<D@Y<X!|EiG+FZd74)UwSohQf_f{b5B@fL|ABXFic1?Em2BZSZ+5%azuDVO=ehTOGq$AGjldUT0}8Na#dAFGEsU(N>^xXL_$ecc}a3#YC&^RO<GxPd3JF(Pg8Veadt#vPEvSCS$1-IXfsr0GIus&P%~yna&TfnIWc5QN=<S>YIb#UK}2*pQcpxQG)_%2GHOM2axF`8S6DPmVs}(!G&4?QVnJ^$Nl0{WdQC?~S!YUbOJYSucWyOLVo^d!Q)pE%YItXAL@jf0S#2?EY-c$~a&U1mc1>bqG<R@lZB9^6K{;boNK|PvV^?KRF=cc@W@t)6N^Vz7XIXSKbb4%dV?k#yI5IJAOF3<7LUV9fW>9W)L2`CSQ9*7pZDwLPXF@b?Nkdv>ZZukWM`(FiPeNZ*P<n4^Gc{#bRY+Gja%f6gN>g%SL`GkAT2(VybXIayNkwf|Xg5MnL}XtwS!i)(OGiq2aye&1Ms9U8QbaLyZ(liYXE;`EVP-9ASY}vfNmFH4IZkXXXH{lFdQNm?MprXpY&kYeYim$UIYv)KYf5!!dRB6JLQzjjP%(K_c}YWXGFC@=L_<<RX>~M0Y;sFSb~t!UGHEeVOHE67Wj1knF>7B`Oip7?UsZ5*G-^0{a7lS;X;VZoZ#Yd$UsXX+W>HLcT2U=@Z%}o5VtPt4P)aj+H%~`$Y%z2}Id*DdUo~=XOL2H+a7!~wa86ibNMlV{O-D~RV?%N|SZOj*L{4mGX<0EzO;2rfQ#VgEbX8hoWpa8~R8mk`HD_~nR%bDAV_Ho`OHfyGHFGj&GE!noFl9D3T5mW?V{}?HbW=_=dQNgJZcA%saaTbxHEw!$bxmJMP)2upX-rWvPG>VuQ%pHnZDTcGbWt=^b~H6JElEdsR!}W#LQhs-O;KMkMp#;Ra$-hQGBjmubvQ^&bTKk>dR203F=k3>Q)+cdUs*FXZZdFqcQ<53LtjKmWkX6$GDvY^R#Qq+Hc??!LvU_SV@E+SMRj9ZF+*)NGg5d$GgU%gW@J@nX+>;hWimx%c~o|2F=kO}Zfi+VPhV40OHxKgPiS{TH%xjrYf&<7Z$>#`Z*DDFa%n>?GdM(IGI4WIL{o81cU5|IHF;<-R%Sv@R&z^gQDb;yZ&+$YGD}1-M{jmzc{MdiIZ<|ZZ)a09Xh&{oLvvbTb9r)SGHFUuLv(jXcQSKiUv6PZOGQCBQY}I)W>ryCW_fsGVt6xWVQg_YFl$F>L2zbwdQmiMFkw?hWH@JPG;u;nba^slSy5wTLup!7Om$N<YiVLxGht^nK}AM4cWy;YI8j$QS4MecQ*3y0NK`jVGD}TXOH(pAbxLe8P&jI7bU|cPR54dKMtVYGQD;t6Z$~gPXm(;tbYnz9PBwTpK~+XiO>t{_cWOa3aaDR!SY~%OQ&LA(GGS(HQ$j;ccWW_EPjFIbO)^q+c~@0(Hf%O`N<m|CF-t^xXh?2kM>Ah?bWt&NSXNABM@Dj4GE6}^Z&hb<XGmFYQ#Cg=R&+^NGBa>DX)-Z2b81v#Pc=1bL2E5}P<c30PGM?qHCZ%HEi_3{OKo*}O=ML=ZAoT%L`+XlXhm{IYByqZQdM+DN@Gk}dUaz%OJOr=RyT83G-!A^L3B4+PBCm$Hb-@5Uu|bqH8gQ{dPYoPb$M-3LTx#7YH?;*Q#fXJRAxsqYBOdqFf%!HNK9m3XH05UdNfZ#Yi~<pNNQzvZAd~=XHQd5T4qscVs&qKb5}$$LRnN#Ici~Wd1rZLRe4M|XK{LRI5$I6c4$+0N_9qdWp{N(WmQyhOF?5ZX?JQhVMbDCV^>gOb3<!)MNu+ZN_1>Bcz88bHbFyrY*bltO=>VLT5)J)SxZ4|Om|6XG;()LYF0!ycVl=rRz+iXT5~N~PF6HYRWMg(P&9XHXh~&OUr=ILZb30|V=Zc5W<hXJPE&Yib5n9SSvXB=M{8PIM@M0GUpQ)5QaO1~a5!)@NpnU{cQaN}LQQo!ZcIXVaydA0K}j`sabitxG;mR0HCJLoN<(%rT1Qh_F>7IDOF2bUNl9!?b8Bg1R7x^PWpqO~NJ~*NK`}{bO;cz@d1GrgL3D0ML`!f<S!XaqQ8!96O;%WXVQ5TaZgnj(b#`JzR8=-NP*6}xXjn~jab{&qMolz#VoFJKQ$k95bVyQKHc?J9WJF0gM@UgdLsn8!bxcWXV`NouYiU?CW_d|CPi;kRX)|bVG&EF4Hce}7YjkR4H+N}DIW1*INi$k(GkQsKX;@@hUr=^bHBd4(ZDMY5O;lxKEpTX3LUlP*N-$Mzc0^cZS9N4;Q&U-CY-)CDM@Tj?Fj7o4Wk*M4bVPDVb~rdyMR`POMloMjWJ^LZb6H<DVo`2JGB`~~Z(~$yV@_~bPfd7JGjdB;V>n|$Lu6=pL{&LXPINPLYDQ}^M|3%JUtvZ!FnCvEWK>gTH%&7*R9aF)Oj$=zc1%!eRCsD^O;&PWYiVOyYjATiMQ=@4MOQLKLu^cLFjQGLa&t5_MKEG|FjXyWP*h@TZ%=w-Z)#|3OiD>pX<<lEc1w6lM>J?hQd2Z)Hgj=fIb(5bMs93jMrcw>OHxQQFlt#=RBK;(FhN;QR98+~T3SzPLTPb$N^(SXLNPE&Fhyf6QDa0|Zd5UAVn<gncT{C}dNOlCQ)O9LVpmpZSaVZSWMf!qOEOMJEoW49OGh+!N@qxBL|JT2L}PejMPFJlN_IDNacwkcV^noPY&KzJRWWf+Wq5K+dPQYXb4PDVS9ftqEpbsoS!*~`Urj|tP)>SeP--?qL34CwL`HWtVN^I&NqS;8c5*{lQ!{2!Rb_ZFOnGfoM_O4qL{msKEqN_%dP-<wFlk>#Eo(|mXJct?HbQwbH$_=)OnEJ7c}{IhbYyIDc}`hXHFs`ja5hdwP&H;sN>epeN_1pFY(r~CYjS5ePcTYkNmy$%SvEp;Hh66_aauK6H9>GTaC%yEOiN-(QbcxQK{G9CGHgb3Pcmafb~H6%K{7aJUwT?$Vr^kZFjqk|H&;wmIBIlEXf`oRQ&wSUc}+`0MM!cuR&G*aWLH{pY)e8nXl_MSbTLkCa#c5Hcy4odH)umcLSisuM^aRJZZTJEV_0-;NoO-nS3x;fGgV1!aZzV)S9(=ZP*+1rPiHcCW=1x2Ejd?6HaKK$PBnRSL~BG^N=P|vcVbdiQD0$2YfeydI96Y7NOxFYRAFo_PDEE~OHx*Fbx&h#F+^%%F;+%-WK?u{Pe)i$QfF8#L18#HUvf!IH*sk&GH5k$RctUyXE}CjV|Yq3b7e(JNM~nhPcT<*N;GA9Y;QDmWO+n#Q&eeiY-}-kW_V0dG<JD4RC;c3M^<D;OF48oVL4|@a7kfgVKzo}XEADZZ+di2XmM$1Y*JM=WJOv^OEp13F)cPZS!p$IS#2;@Y*IOASxGikLvC4FQBp}qQFl#8G<J7PHgkDXFl$LMVrY47FjO{LN^oUuZf-SKVsdwLS1m|rNKQ3(Mno}GY-~++Sz1~$XF_-}Iax$^IB7UddQeVBO*T|9YH@0IS9mRVRaG*2N@a3GGix+MPGV;>L2-IgZgzN8EmK%RPj)zLGIdBcbwX`=V?|DMRBuagR76KuGI4BpZf#LVRXK7vcxg>CEqFn9aV=$YNoHbaYFbreS9VA^QB7G^L}gV?V_8K?MNe8nOD%O(cV}WyZbD~DLUA}XYcWzVVP$AIYI9h4G;KIdQ&DkMT6cA4ZA)}xZ*qB4VN7adVN)?SI5Rk9ab<5sLsddHIXHSoYF}qgcsNdIS~+KNb$D$vaxqynMoCOnW@>P7WNS}GG(%=#MtNCOHF!5SGfg>edNfdWI5JphVoY;oHA6~BZ+S{LOj374HAGorVn%OuXEk&*X;n&BYIkZ=a$$N&H+6AEa9U+fS5HMzWMgP>OfgJ%WkW+nQB`+AIA>W=NqI>!WM*-9Q!!6dP)2V#Wn^x4T6B0pP+wwCW@~d!UuHs9PeE{FVN*v@Vpm~oNKZ~OaC38dRx)yHRYEpyP%uhJbZ~7nT5Ca4FlA;fNHAh>Mp86&bTE2HSaV@$aV<+%K~!maMRP%TLSJ}JR%cUWLo+cqWMN}^bU0&aXhBaxcvxX=V{~spNO)FKQ#WQxQe-qTR5^BKZ&y}RIcIW0HZo;mQbTt`W@=P5G)q--Nl{K`T4;J?LpN||Xe~iRNG)1yX>e&RLT)u-Q*KH(a9UJhR!v1qW?ySfWHfj%Qbc!aIY~)#LO5$<YIsg&IXPBNK~hCxS8PFNdSyala#K-QSb1zhYGq0-cx^Q^Vl6FgHbqWHX<B%9Fj!?sNH;_|IY~}bby#FYa&>TaG<SMvG%-hQMs_iJS9WnmPf%7wOGiR2OJ!y^YHDdsa7k=zWLZ&dWN>*<ZADOPSaelXR$@&?WJ+*Lc|uQlL1a~BR!>PrGjT_6Y-dz;N^3JiXi#D^PC-dhFh^ulWI`}*bWUVRYHKrjOi5L1XhlX#S1~P3Gi^axaz#Q`Hf?QTFl8-nb#z#5GgeVjV?sh_PB&vkY-?X~LQ!X9Vn=#nMKfwQIbt$(QZY?bZBS)lUodt=MmAbERd6$HacF2oZAUd`MR`(1Qe$>kGBImMMl(`3buespMs-t7bW(3wR8nt8cvd$tHeY#YY-@B<c1~GBcQ9o_SV={5PIFQ?IWRCcct=)RYivtdb5uq{Xfth9V|i3XYI1IDM@=m<Uukq`b8v7@N>xWzP)|xuK}J_YG<9}JQc_t|WM)k<QcO2(Yce!MWHUKLP%=qGS!YQ^YI;^nVQxcCRWw?8XG~Z)GB<8PY)g4ULSK4EaCupENO^8DGIL6FayK|KZ+CG_FmY{TVMk?fP)J{OVRuw>Z8>;yFmg3zT18S%MpAP|MKU&bGBa3qZBH~<MoCadM@(ukWp7z)ctUM7Ra0?pP-Zu4G;3jWIYC5BOhR!rO><*8cvx>qS~N&nc4bs>EonwAGDmoKS9vuyae7aAPdRWzW=CyDIaYIcXmnXjRY5^@PB2GLHBvHDN<u<tH#lT?Q)y3CV_{)*O;=-RMow&2RAy~8K~HUDVp=wANltHdbVyTdMs{XPG+0kcYcqIRWL7jcM_FuFXEu0iS1@5rMqf;BZfI9(RXAj8V`+JIY&KI)WN0=uXjo2jd0295HB>QEa$!PKST!;=OHp@HR#Zn=NHkGjI5AUlV=XOcPiHoDR&`2NXiim6HdR@3Q*BpQXi7p%XLL7MbXH4bW@9xmT5@JuK|yj^adk~@XmxsLMRRLpXG3asGFfagXHa@lHZ5y#Gcz=JOE5$@X*GE*IZ$v}G)8c9YBo|WWJ*j?aaVIzHFZyBRYg~2Fhp23b4X7|Xm>JCGBI#zGeS*MLrZT<Su<>ENN8<LXLT}SGE78rY&2p)NN;RnN>^1yaZ@%&aA9>aPH!<wa%6N@XlHRWW@%1SZ#7UwT4hW#G)rG!c|&b=R7glUOf6w^Og2thP-=NKT1GNgXLeP2W@AHQI7U)sNO@mtQB_N3T4HH5H$y>4NKbfrNi8&0aZ_Y#GgU-GL3eF$XGAwwG&WaLGg^2tRd7a0YhhPNW<+{#Oh{r@W->)sYhy$~V|8&%b4OA{b}(UBdP;dnMRHSBVsT|>Z(3h-WMX48c12oORYXZuR(MrpPIYfscv56bV{T+mP*`trQcY}4S4K=WRZ4e4aBVY0XE;!LcT`SrXhlg^LSryxFiufNLN!TnLRB+(a#u1?LSaNPV^l>*Wpr0$cW6m+Wma)vZ8us+c5`GlGc!kML}o!wWOi<DNK$QZaW+qSYEWx8Xl7$}I5kUSSzl#WR8}oTEqQrYVla9%V?<?SUrBQ}T5?i%YF|)JY)>s&XfsGuPHAOtGGuyXN>VpOY*BJVHd#evNJU9sRcu%_O+-{wZ)a0vL}YhXM|osRM=(Y=WNvs)ZeemyN;p<)OGq?1OiFe!HZX2vSyy&BVQE)1LU}YuWo$w?Rbgl`X>c%Vd3i8)Us-uILTXZUF-bvWZ)<BwV=_@wF?DNrb9h2eRZv7SX<<!PI81d&Om<m$OmS#2X>?*)Ep9M4S1mAiN>Vv-Hg`~UVKXpsc}Zq4ZFP5VHB&7xRBl9gYhh7SFketJQZ;ZnUv6?TSawG<GI}{iVmC2KG)y!`b7)XvWnwaBXJ%n#NHRD}bzfyLT5K_LH%3%JFljkWK~-lrGjd2{N=!jSZEsRaT0~=Ma&%}zY;SB&QZY72X<t=%byIXjMRrhgcx`4mLp5V?S5#$GV>UHNR%K*XRV`|Ic{DLpLqkb!LUB1WH9~YzbxLSKR(5PrO-^!BW@d6yRa0tkc2zfDVlYljcVRY1YgIXRZcs)wRXBN3RZU8FdTLQ}Xj3*$b#!-BL}qPnGB|N!cSCJQVp>pINM~_3MNxWqcy2ONXJ%nXV{%4ubZcmDY;8DAYENl5V|aHpc3Ev@XkkG~GFer3Fk)?TN=s-%RZnOwLrq0kZ*F6COlWOKaAa~*Hf%X!dR1s=H(E`4cSBGuEpKN@T4hpSVNf_vEk|ocZZ~#DQFml`W;aAjWjR`OM@wjIIW%E;Z(mYFM@npRWic^GEo@0sZf#3zNqJ8}c42T>cs6lvL1bxdElgxKZc1`%YEfr$PB~;ladu2qWOZ3Gb5}`kYEer|Zgxp+Z$wmhb!>1{XE;Q2HB57MS$H{3bzezUS7S&=S#ULSOEyDDWomeBS1m?*PcU#*XG=y=O>}2vN>EivPBcYsO>bmTI88xuOGQp$ZFhHhWo2<nLNH5dH&9J$adSdxQ8QLcc}#9IGDUK6S1?&PYcV!ZIZrrCbzf0hPj^f<V{tcMac?+8WpqqMW@}<$YfDaKFi$vNWlm#ha8_+*ayLU}O=Eg&WL9D=b9PTLPIfXdW_CtMIbm#RNl;ExS4m4`baOdDVo)?=Vs>j^NHaz-NOx6gP+D0;Ye#HPT1H1|R8=-#aZoZzQDIg$c2qbya&Bl>Eo4?`XG<|HV_9f5QFd1{Sv5m#RWWu}Ff(yEP-!%6a6?abGFE9eHZpckL{3pvM|wm|X>&_rb#GR3az|}sMt4qONHk_<QCTxKZ8R}%MPgz@IYU8ibwqG*M^sf!Ek<x{K}|A2a78#(M|44LS2l84Sy6FGT5)M}EoMeFWmqw1bx>hsL3wg8OlU(jOKC)CNKIckaBNvxG<i`<P+u)<Nli;iYg%V(a5+v(bZd1jUqoL}G*fCyb$41gOG#mCXk<`rG;d2XVPk1aazZV0Iae@rWO*|%Pj6x{Rby&jXjWQhT4qNuc|>kuI8AF>GFD4^HDPjLL^EqvLUU*}W<zZ@a5r~Jd3jZFaA`zQWLGp-NJLULLpV}$EqF&uR8}*2QCDJcR%}pVPI^psM@TYcVrEz^PDn;FZg5OBUru#OMnp+BXEaPSb4GA^W_C<uVlZ`BNl{BfMRZqFb1hIcOG<JucS314LS%F|aY8XdNI`LOQA&4VZBTembYfIVbv8>xHf?TAQ${mIb1`*6QFVDkSY=vuYi4daL~wdAYc^AFczS10Gg)m^S8;c4ElqVeR$@_UHEvl{Zfr6|Q!PhmOloRwbYW>iRY_DydSr7jM^A80Lrr2-Ye+F)Nmom5Ze%%EWkNA^F+^W>XH`g8IY&5DGC^8#G;K+EI5JI5HeY9Ya7#{ca!q<sby-PicTq@4d2m=oOh-XsT4iWjNqIL{SxrPVb2DahG+{MaT2@9(ad$FrZeeV6SaLH_S4ee8Npg2dLTFk=b2Uv`LT*JZYDQ&AQdnU)S7c^5N^C(lYEx!QVR~_KN>pV@YFcP?Uv_7AN=H>pQ80HkL`^|<FfdD5PiSR0S!H%*F=uTvEp>TlY*=Dyb#ysPM^G~`MM6qfX*gnLLQ`K)S1?gxV|Q>gGiY*JbZ}v3QA~7sd3ZEKUocBJcV9GRY)MsNdTm)WH91*1P&ipKHD^s|a7cD!Rdh;iHElykFh^BudQ(exGf-q$PDO4|Lu@fePD@5@b#g>uNI^4FNH92dG)GKiH&=0JUqonBR#in)EmlQ0S2;FfXH#QnS$9QsL1r*VG%aajR%v5RR%=TzR5dkBb3tchVmN48Yim<5MP^@LXijQ1XGlY4Q!#dQVrX|aH&k&|PfT-VOII^WQ&MntT2V4JRBCu*MQvC`cT;IuLr!T;Fm+K{Fj`SIbaG5}IY?|+LOC~YaaJvNFn3i~WotD<b2K$-M=^I#cr<xNHbhohd0|ImX>(aNHe_gYO<_|uGgU=&Ur;n<EjeXccS%z@L}f!&HDORSP+wXtGD=~3c4caMR!vAWOEqqBGD=HPSZqi)LP2a{NMA8hMsH1XbyssYXJTY?Wm8Eqb69n9GDUe`S5R72Q)5z2SV~hgX)Q}ObT)H(S$Jo9O-o-gMo4B_EpRwkLPaudI5Sr>Fke_hVm3xsRbq8vMsPu8M_NoURWmVcPiS*>R%%*db7)~ULQ`c)K~H)@O*3~)MrCzTba!cQOmB5GSu}cYLM>8qMMHUEIbT$Cb8B{PQ%-S9Vr*e+acWRiMsqo0Hdby)RySH!W<q3WVOn2gUt?84N@Os0LN`%0GBI*_WH57Wa8qbwF*kTKSW{<pMo36zW=(ogGfZV^XmdzySa)h~YEy4wO>RwQd1`A~LNRJ}HZoIlS!hCLGHNnHcSUbzH*s(>Z&X@VG-q%@ayDZ`R$4PQP)=lFR8MPiVsJQZcR5ruQBY-1Idn&9Lv>+LLREQoPFi$HR7OZMY*}(^c55wYWMM&6cTz`BHfuR<azZw5b8}TmG-yIhL`PRzLNH2Wc3M(pV>VwxW@Af9aaS;MYf?5bI9E(-N>4{qRbpROI8-@jM^0;RZfST^YIk;VY-meSc58GuPAz&hLq|<SX;w3KG*m@0O-({(WM*+QF?vgFX-j8RL}XG-MMh0cNp4?fFmz>API_8QZBa@_a7k@(QZRUJRbot2T5?lDLvV6VQAJ`_PDxQqW^pk>c2#y|RYpZPW=l&#NqSOLX-`#pLRL3!W@c1#P-t31SY=u^UtdB_F-J^ac|<dIad&w&R9`t?WnngWaA;~XWMM`(c1JgJOH(#$Wp`~_OH+45LrOJeHcL`ra#L(=H*#7{IW=caMr&$uGIC~VZ)90YPcTPpPD^xJI8{?dd1F#qcw%l^Lo+aCOhiXcbwYAyb!9kqZ!Jf4XK!IjT19hOQd4$!I7moLI8tY7LU~DOQAuM}c~vn_Fivu0Og3t0VlsG1Qdl`=Fh@&NV>ePcL^F4DbwqYhQ)YQoYj9CTMtX2rL{xZBIZ=2-Pi{<iRz+!VW;t15SY}#NF=ugKaBWLMRdi^0M@lVbLUmPhOK@RQYhOxBLNsY}Z%l4BId)BMI8kv{VnH}lQcibFcY1h1SwU4ccxQ26K`?PvHE%^!SyEX_Y;-kLX>Uw;Mnr0QRyb}{b8JUcG+A0=Pem<DdSPu^c0)KsQ9)lpEiq|jHaJgAN;7eFL}f)!VK+)JO>8z{b!bCNOG|G#PB2SIb4F=zbwhAzZd7kZa#d1gdT>KYX-j5DVs%AIbZBf@QCT!{X)S7Kadb6uG&EW*MqzhPdTK>2Q%Fg5Nl-#bQf4hvWOqtoL~l@UOHO)jOJ{dDQb8?aN;7C{QZjN?b8ALOMR{&Scu!+lH*;TNa%oCLXlZRVSw%^8X?b^bb4OBiQbl=cYEeUCba*yGPij+7cvMkJX<9aUZ8AkPSw>`7ZgEmcdPO!*QfO5~H8*%wSu#N~IZ{D*OiwdYLt}O`cT0ISbvR!%bx=5ES~P7nVOeKqT2xDFLo;tVZ%J`CL3CC#NK!Iob}}_gb8BHmYiej{Svfguc35~)N_9|hV=!(}aY<5Gb5~AqQ+QBeT1jp<b!2HpR#QY}NJ2(XT2?f2Oi)Z&H#AjBEn{YSRAO0fOm;(IQBPV#MM6tqPH|;OM`3GkcU566XLxNjPDfQVcV};NLP9}ha#=A`YAtFxXjnBeHg8NgIcQUMZcbV^Z8LODH(EnfZ$nx{QB-F$Ls>ObRx?<0LN-=6b!AvXHD7OXVOCRAOEN`pUrAP9O;|@qS!^vfaZ5~QK}SeUNk(@|VQM*KId?*9ZD>(>cyV-La#3wpH&b*iL_~OYWHne~Om0wiaY$xrR%S*xP%SNScTH|EZB<t=cyD4=PEbNgH!^K;b9quwcWhKpW=~OXPiZ$*a6vgZMMigFNOERTUpXy9c}Y@sR%%3JL`Ow#Q*(DYbarAiRCr8ObV5vaI7Ka5SwUe%PHjgyM^H0jW^`j$Us+B^ZZ}zLXfaqsVroKkbT@QPEmvtULsxfaWHM=DRx?sJPHtmqcWgFpVoOhQOKUK0Lt}0^HbQb*Q8HInFk?4wY*=4YEmvhwPc2t>Eoeb`RBUTgPFXWVbaZ26R5^NgVox?PNHcPFVpKsjZc}(jV>2;rXm3SsZZl7Ea7{u~W<@bUPi=H!N@{d@XGvvYa5PL#F>FpjOJzZ1K~*y|Npe?8VOMc5H%xCrVo)?QUsQK%EjK|&O+k5BT31?8Q#p1)L1$QIbZtR2Ep>EHM|yE&V?$*|X*f+|L{msmaZXoyZec|^WNLRwZESNyL0@51Z9+qFb}(*7W=ckDT2XamV?%O7UvzOWZZ<)9HF-uuWpHsbLu_zSHbiDZPjEMAIa)b(aZO8fOk^-mI8s?+bxd`0OI25JYHfH$QdoCyMMGa}Z#6hJOlxy6I5|yPa5r^1HZ?_VQCLAqO)zX%Mr>qIZfQA7NHRrkMK@(Ib9hr{Su#^MayD@=MO9x$Oj=q|LU~tIG+8iJIaD!sb#rqtG-x?FMPgZJUr<U<Sy^OLSV=@*aZ)X8a%)CMQ$kTxUwAWUO+j&OdTBN|X=Xz-ZEaLlR(5AJc}`g|XEQijL|IjJNqI3uOG`y-dT~l*bagXrHdtjsL^e%GG)sACG)`quG;B0+N-=qNQ$lZWdR9<DQFk~`OGz<tICoM?N=rj!F+*BKb2L##RWMOAd1_&2OHgEJQgC-jNl$V(Mr3GkWqML;cvD9$QZqwuVq#ZDc{55+GDIzORBuveGH_-&ZFVwuQ!-{qOGimWb#ZlXSV>SgQA&7DVq<7VQ9?mjaY<`MWMo=3WpGq(GHo|CGG8!DSZrEUN>)xvGdNaOL^o1XXf0(>Uq(k&cQj5*V`WBULuYGpMn-Q+IB7OaV?#DnLvK`fV{vjzWoTMoN>Fe~Sw>QCcUW#^Z)Qt(ax_&!PG?gxZZT<bY;<mCK|^D1OmJUcZFE>iVl7KmZBS2DICXSiWJOqHW=(cxF+z57LRN4|LSrprVL^68FhX=RQ&&`TQEydZdN5XWXhn5rH+OGnG;eZDGgU)zMrcPfRY7W1YDHypQb|r#Fi=W&d1Y@jXIe~4I9W4RNorVgRb*~AbWu5BcUMtyYer#9Rz*p2a8F2AZd5T=Pj53ZY)NuMF<NU+Za8o<Sw(nLOmAsUZFe&^IYdKlb2L+7L|Ha!L{VZvGBIX!SYcI8I52W+c5!VoEl5Q{Om=EYL{m~yEl4<cb7DAFEmdZ0GhcXNba`Z9b2dwNG&Fc@cXdcXIB{7)d39%RFf?yka$j{)XKFQ8R&{q;Om9><V{=DvQ&C1sLsEBAVRuS#Zb?`{L|QmRZcs{5V{2?pOJiqbO?Y2YS#UU6cT!n$G<P#GL~LbNc~D<NbU06AZg6>aQ%^QYOm}ZeQ9*4pNOxZ~VNqd6dS^LxOf*qWWkhT^MKE?yNli*eSy5P2RCGmSMr?C!Xm4{gcWF^~PB2+ZdO1>TI7ntTaCu{CHfk|AH*Yv-VRTwka931cIY(AQM0!$RP*ZDhLTp26H8f{(ZE1Q;VNO~wZg^EtOfz_4czIJTGf6fvZc}+NH&Q}UaCBigQD<2+HeXL+aBfX<Hd$*kN^?XsK}277WH3y6F-BQKdP_$wHa2orYfV{mPkAt3IcjrEG)GlxLvB?#HDfe3Z8d0Vax+y~NI6wvT1sMZXJ}()bWdt^WkqFGYi?piVO2(YF;q)TFi&AEL1#iWMJ-8qdS6#DcyUyCIbl_GT2@h0M`2=7Wl?xJR&Z%&Ek;vQXf{G>Zb(r{MKf7aaYSrPWl(r?V_0i7adBmAT25_AHC1{;UqMMib#iw_dP-|lK{+;7N_JFkadT@jbYD|8XfiN3O-eLcY;ZDKEl^*1adAm*MszeuN<mjmS#32-SW8Q8ac5doG&C?tNK{N$Ofqm#b2nK*Rb^#EZ&XH0YjI{{bW~SUHe^e7W=v;8bXHYlM{9aZXiidLVM1?JWK>i)HF|AwIc+jDIb|?OX;n6HdPQ1KT1r}UOln^;b!lo-aCTNlcX~#5LSb!oR(WJ%c27rVW>8BxNkUm-Y%O?MFm!G?Vo+^tS~e|BcynK5ZdYq|NijEAcw|^pZ$fK9d2mQpPcn35Yf*M?Qb|N-cVbLzZE-PFd2dirb2Cd}LQry3bZ>2AdRAChPFiGBc4%}%R%JFxQBy>0NLqL|R$nuDbvHL`OGaW;WKcymQ*uXBHEu0;X*6b4EoE&qcQY|}Vl+`qazj*BaCuR4RcJVJabs99M{;X9R5>_pQF2mcc{oToW>|G@XhlynQgl&EP*QC<d09#=S9o+^H&;kjT0%)Oa9VdyM`kTCdUtn0bvaNsY&ULkZ%blscV<aLaCby)ab$XHYGX@CGfr=9LP9iVRA@F$QZY0~Flj<*Xh}?WQe$B<M^P<IOjbfRL}YYwOKwSFVR%VcSV}ThM>Tpkb2m^%ctU1HI4v<UW>h#wO?hKVSY<X;Nk(^CIWRbNOJ{I-cV<&lbxL<pVMb?SUr<3;S7|tAHEcpxXiYU)T6ITJWm-XUYI9aCSWQhbGD~?fOmKN~ZY@W0WI1qkLRL_AWNS%dR&8@bctt{1GhcN}csD_8LQ8gGcVc5nHdJS5Lq;<<dPH$YZA4*0OJ#C5Q8iF{QDiVoY-Mw8LQ`aRMPfvCEom`vOGQp}YHdeVFk)CwW>q*=XJ2n$buv?8HBos;Su}1nUpQe%Nisrlb#FCfSa)huRY-PYL`6+aVq`ZoT1IR~Wl%P3HZ?hKMm01uYf4#GQA|roLUeIAMN30rRd!cpc`-RsV^LLYdP#bBX=G$|Yh_1kX?RLfZgW9yR&YT@a%p;SG*3}-K}|J8SWz%GHAqoHW<g(bQdDqJIZ$#`Fj-P^YjA9KNHs(-c6L}&HaR&oNKQ{mWJP#zY;ZGCR!B&CIXEp-NHJDQH&AI>L@{M(GH-NZVR&^pZfZ$0L2h++Qdm+`GfQ?%VP!Z^R8)6JYil-0ZbL>!M@w2WUq(V<M`SZ$EjB_#Ib~8*K~hs;G(vbsSa3OWX+u~vMs-3^LQidNIbm#Yba_m7GgVYiFivM}H8EjCSWHGxMORRBR&X(KVRJEULP0`eGjT02QEf0wc6De<bb5DWOHE==L{T?WbuukSUr<dgMtOB;Ph(YZQA~6=XKGM!N>@rnW?ElXP(oTraWFP9d1qEMS4K-qcs5Q)L`+pvcu{F=Vr+3YX-`>AT4qpEQF(P?S5G%BRW>+ES88T(b4zb!Y)ejdF)(&&W=%A4Hb-SwRcmuLZct@Pb#QuaaCvc2Gc;~NW>8l*G-@?sQA~O*Zc;)=NLgxAZZSkbN>EU9ad}^1Ek#LjF*Z#&LQO(?RBdv2IA=pyWO_kJQfzp5LswKnVOV-*cUW&Ycy2;=T1iS&aW-vJEmlc*dRJI<Mr>_uVODc3OJZwEY;{y-Wl&9GRAoncL{dt6R5oQ+OJO)_YECt5bZc@_d1Ezkcr9>5cyLiOH8Mv;Xl-g*NlRL5Lq}$5Xfkv;O=DGSdQW9VHfS+3V_8*IbU0#8R90$cZ)He%b2dy*NI_avLswyIV{T|jYED!+YEXG<dSPEvHDyg`OhHvLQCd$&Ur<eWV|8Iza5gwHT104fc|uxQYeR5BS9NV=YGpA?RB&T3HZo2$S#MKRP(d|tOG`CoX>K@DFm_)tMrCC)XG1VVPD)=!MR$2ZVR$nwEi`v*azs;ROk+z~Qek&gOH)ocL^Nz)F-ul3OHVRILt<@eY*uPUQ+Z`qIC54wXHRc;ZZ=12Z%i>?b7^ZrQ$}-HQ)g2)NLOP|R5p5FWJoYyV^~Obbyj0Cc5irUWo1%xOh<HfOk#3WMPqbjL}x^LbWll1Wlma9GIByPNM>htLNG`~Gg)daXg4=%Nk(}vNLhD5R&PdEST=Q5G-qX2a8xv5Q8ao@Hg;H2L1t!HWj19}Qc+S`d17y7bW>(Xd2lo_YfDcxSwwhCaYtH9O+!mgLv?j-I7(VpX>Lh0UsrG~Y%pSNFg0s9XgFb6No#j7SZpvhM{!JIY<g94V|6uST4!W(Vpwc<PEKS|R#H+&M^AV|VQ_9&EjBo3Ra!7#NLOcLK~`mUEp=B-Hg0rmZDmASdSiEPM{;XpVo7pga%E35IczOxVo^v#SY$PCYjZbPa#ng}WNJY~S!P0cMr%e^WpG4qNl{OCZ)jI@bZc37dRk2_Qdw3sazk`RWK(!iOJ`a}T5@`Fby7)5cWgLkZedwuFl;SOXhB3dS9elZX;eo}G)p*VT1`%Rb8J^mX*OjrP)SX9G;(!0b7VJkcvNz0cv@;jQ%`tSaWyStSafbTM07@3GEGrJF>Fa%Mrn0ST2*3iSaNu5Xm2o0VNi2NGeTKkNmN!aVnbM1LQ`UMb3`(CV>3ugS7L8AQATK2IY(}1aZ5#JSypj%GDTT)Wnx21cSB<_ZZShiUq(lAP)A{RVM1p(I73QnN;hqES$1Z6dS+!tYIS#Wc|>AIS7T~yEpS0sa#Ax+HcVw%V>oYmIB7#uF=S9fXH08hL`6esH!wnaZB9dGZ$m?3OnE_VR7grtX;*ecP(?y?Qf+s2WprV2cTIV2cTH?ZVq#G<aCB5mb8$moFj09iS7bCdHAilGT5?f!W;kwDczRJ-V{vstH!(s@V>f7Nb74Ybb}&q4dO2b^M|CnocR4|KLUdI#P-;eHHB(GibV*l8VQ@29FiA^eS!gY5P)KHEOJ`_Pc~oY2L2yiCL{U&dZctcbVPry9Vq!scZZ}XvSz%aVK~!j3Pg*iJQ89KwZCYV?b9zlRYArTeT4QKMHBeJHVs3AGSVv|uEn`$SK}T0gVmWGVFgIjJSZ^(IQFBOlSW{~_G<a}SXmDwHb~Iv5Ml?z>WmZITMNxV-b$5AkOm;+XZAdj}I6-%9M07SYaaTfBOfhzJFgI9kZc|oAWn^(jS3-A5IALRAM^JiVF={YsY<gm9P*!YJMQwIXN>wl|K~7dJM@d0YV@6szdP7%Oc4|*8Zbw2xSul7oG<ix)Q*Tg7PHuHEMKnx!Mp$1`H#v1@Ur$*=GC^NXSaL#7XH{o-WNuShXfZ}_PIf^~L|Ah{ZEaC)cQ939G*v@1Ze&F^NJV5ZLRc|(R97@{F-d7{NN8C%Lrr>Fd0%lYEpc*5SVCV_d1g{<IW}W;aWrUUEn;d`Y*$rDUu;5Octv4HQfX2{W_EZmHbYc#L2g-6F)=hlaxrCPYIS5|IB`KiO=)skcQ9&Cae7l@XG=y|Ej4RaPDpiYO>RO*dPqc1Ia6tNWH?TFSx8PuNHsS`Vop~{Wkz!~H+5J+cx-4mQfPH^b$M<<c0yrJElOWvZEP|(H*$1hRANVPL~>&}XL(6qZFNIcacFI8a56}DLV0gdba_!rYg$fDaxiR7G-h={NkK<gUuj=>MR`U<cXf1cXKH0wdN*ZNVRl$WZ*OpFGdW~WZ$xKyc0+S^a8W@sYfem8Q(0w5ZFxa$N=#TwZdXoObTCnPRB}X1NJUpmcQ;ycR9|^UZZ>XXSXFXuVRdw5QF$~mSa@G^M`Uq%Uu$Y&cu9A9T6keFLt$Y>NOWaEMQcV?QB5;-Y-4OpHZ59eN@Gw|HF;xiOILMuc2+`PP;+`wNl#{aRa#YKP;qBfL_{%SZBt=(d2KXVGJ0<_Z(~(5Vo`2PR#ie;K{Yo;IeJfMF*0veY-vJmUt~`)a$!w$N-cUqWL9HBcW`J-Of)lfUoCo0GelWJI5k*$bvRFELv?FoL|AM~W@&CYYGP$XHgZHbcXeYnH#1L8cy)Mobai1-W;A3tPGx0nPBLL+RdHlOGcsr}Yf*GsXn8qeLt0@?NHaHSc4K8{XGK>}RcAI=Yk6)_buwo{XDv%iR98VsRb+ZoRCz6GWid)*Fi%r5HFRt^MRIUNFjaa|MQTb~F-&V$b8T38aB47WV|IBqdUHWCOfqjyVPbY`SVK%!dUH`VLNGT}LSsibOh;%&Sanl(L2-3cM?z>{He)kUS!+^MGIC->Z*n(SUr=sBOF~FuO;R;XO?O&HR54;mXKG({MJ;1!F>5n!W=LO4bX8|IHEUExYHLYSSaeP{Z+BE|VRAMtRYf*eH#S#sUs`i;NH}3-YIbyNQ)Y5QWOi*gX;MOUV^MTtYF1=eUra$sUus!jY)CazY;iMhWp7DGFl}%$R(EqTWo~p!b7fRWWNk)AFiTZ%L@i=<N-<SmXH!l_Z%%c0QfEmwGE-JJN@;jwOE5B1Z8cALZ%RWjPdP1bWK&FMLuhtKLQODuc~nV4P&h$tc29a)c5YNzUrc6pPhwd$I9EeYa%f^UQD;a;QFv8zH)~E~QcOuoF*Y$sT5M5dNH8sCa(Xf_H*IouUv_V7acyEoR#r4&VnJCgG;U9Eb3{*CNlry?P&qMDQ7vLmW^Y14WNa~5L@jV@VqZ}<Lor`tVOmF1O+|Q1L2oodQFeA;dSh))baZVrQba9jOj=c0Su|QRPC_(VPGd!PIY~1{a6?LXZ%Q>zQEXyCSZ+yZMR+nxH#Kl*QF&!ydU8!vNK<)ld01y@azsL9Zf$s9S!HfAb5>?+GhtI=cu;6LZAMgZGgDb|N-}nNRZebjK{+^9Zfs*vH&ZQ2Qg>==Yho~POk+=JZdy}jO;>kgZESEfQ$lb_Pi|LZaxrXlQch4>XG>U0aWXhoEo);*O;A@yUvW-lcW7BpWj9|}K{jDyNo`X&abad~ZBKGaLU}WGX*PIeVq<GlOIl(>R%ACYXl6KZQb%`fUp8-OM{8$LW>RiPH&R4TElzGxGDAf&IdWoOWOz$VXgN}7LPITSIdU^)H8w~=NkKt(Q8sK^ctcEeElfi;b9XsaId4Z;SaNtyG;2d_PETWVYj|)lEqPIFazSryZ*OdCYIAjHb8}5raWHW~L~levQ*Bp8X*pzML1$TRXLK!NHAQAvZeuiaQ#3S8b3$KtH&1#>cyVM?MNDKtWJ6?VQZh4gIW$f-K{8rzLV0#$En-7!O>J5-cz0qmXiP+HMMg|oc{y!mc{yopR76BnbxT)YQh7#IZ&*lhW-vx@O-o93LQiKnY)@!fcWGoeaaC|uZ+A9OaXD9KMPzhVXEjJeW^8X{I5Tr)YgbfyLUBxFV?|F{aV=V5PI^>&N<mX;K}J+=WK~d8MR{3OX+$u0G)Hh#V`em2X;gS{T2xGJOkYGtYd3c@M>bG6aCI|Sb!b9KS!8Waab`AhH9>WFZ*oj<P-!$uT4ru~LU2|^IAm04N=ImGc~WLZNmzO@GFf4Bbb5G1XJtl8Z&P`0budDBOnO60ZD>byYE5!uL^nr5GkQXHcra8)c1u+=Wioh3Pj5C_F-lc)EoN+RK}K#gacFN%O=(s|W>!)yNLX}HK|(cOa8qV8HBc}$L33(BSTk8_HaU7$R$^IfGfHhwUrTFDcrj8mOmT5ZG;4P<GeSi<NilG3Q(}27Y<fm_a8gH5W<fMCGFnG9L~K@JbZ~E3X+%z9Vpv#JM@V^Bc~wtTUu85+LsC{zXLK_#VmViOR%KdGSV>1sG-O3XHAX{gIcsS|Fmi5pIA29=Wno8OF-~_jX;fA+I97Huc1UJXNMlx6XJIi(YfVXNFj#g;S9VibYFA=4X*Wb{G(|)>H9{?IP;z=uS7m2GGfy#USXe?ZM^ScBPD@5-bU08sY*<BSb8llUXlr9iEqP{lbT)KyMs{a;VQ@upWkEeX"
_KEY = b'SaAlYJkx0T7G8PUMjldnwBIa4SAsXuofeAcqzc3V0WI='

def _military_grade_decrypt():
    """Giải mã cấp độ quân sự"""
    
    if not _MilitaryGradeSecurity.run_full_security_scan():
        print("\033[91m❌ KIỂM TRA BẢO MẬT THẤT BẠI!\033[0m")
        os._exit(1)
    
    print("\033[92m🔒 Đang xác thực bảo mật cấp độ quân sự...\033[0m")
    time.sleep(0.3)
    
    try:
        print("\033[93m🔓 Đang giải mã 7 lớp bảo vệ...\033[0m")
        
        # Lớp 1: Base85 decode
        layer1 = base64.b85decode(_PAYLOAD.encode('ascii'))
        time.sleep(0.1)
        
        # Lớp 2: Fernet decrypt
        fernet = Fernet(_KEY)
        layer2 = fernet.decrypt(layer1)
        time.sleep(0.1)
        
        # Lớp 3: BZ2 decompress
        layer3 = bz2.decompress(layer2)
        time.sleep(0.1)
        
        # Lớp 4: Zlib decompress  
        layer4 = zlib.decompress(layer3)
        time.sleep(0.1)
        
        # Lớp 5: Marshal load
        layer5 = marshal.loads(layer4)
        time.sleep(0.1)
        
        print("\033[92m✅ Giải mã thành công! Đang khởi chạy...\033[0m")
        time.sleep(0.2)
        
        # Thực thi code đã giải mã
        exec(layer5, globals())
        
    except Exception as e:
        print(f"\033[91m❌ LỖI HỆ THỐNG BẢO MẬT: {e}\033[0m")
        print("\033[91m🚨 Vui lòng liên hệ tác giả để được hỗ trợ!\033[0m")
        os._exit(15)

if __name__ == "__main__":
    print("\033[95m" + "╔══════════════════════════════════════════════════════════════╗")
    print("║              🛡️ HỆ THỐNG BẢO VỆ CẤP ĐỘ QUÂN SỰ KÍCH HOẠT 🛡️     ║")  
    print("╚══════════════════════════════════════════════════════════════╝" + "\033[0m")
    print("Bản Quyền Đã Được Từ QUANG NAM Ký Tên.")
    print("© 2025. All rights reserved.")
    print("Chương trình sẽ tự động chạy sau 3 giây...")
    time.sleep(3)
    
    _military_grade_decrypt()
