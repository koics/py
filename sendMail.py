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
smtpobj.login('from_adress@gmail.com','password')
smtpobj.sendmail('from_adress@gmail.com','to_adress@xxx.com',
                """Hello!!
                I'm Python
                """)
smtpobj.close()
