#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 22:12:32 2018

@author: koichirosato

GmailからDocomoにメール送信。Gmailの設定を許可しないとLoginでエラーになる。
"""

import smtplib

smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.ehlo()
smtpobj.login('koic.sato@gmail.com','jpn36483648')
smtpobj.sendmail('koic.sato@gmail.com','k0o9i0c5h5i3r9o3s6a9t1o@docomo.ne.jp',
                """Hello!!
                I'm Python
                """)
smtpobj.close()
