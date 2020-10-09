#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import requests
import random
import re
import socket
import time
import sys
import uuid
from PyQt5.QtCore import pyqtSlot,QThread,pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from main import Ui_Dialog
import os





prox = []
for i in open('proxy.txt','r').read().splitlines():
    if i == "":
        continue
    prox.append(str(i))
s = []

account = []
for m in open("myaccount's.txt", 'r').read().splitlines():
    if i == "":
        continue
    print(m)
    account.append(m)


print("""
        # Free Python Bot Spam #
    * All rights To Mexaw Alotebi : IG @31421 | telegram @mexaw
    * Falcon Digital Cumminty * 
""")
class Main(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)

        QMainWindow.__init__(self)


        self.setupUi(self)
        self.setWindowTitle("MEXAW REPORT SPAM V1")
        self.UIchange()

        

        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.attack)



    def UIchange(self):
        self.tabWidget.tabBar().setVisible(False)


    def login(self):
        global text
        
        
        user = self.lineEdit.text()
        password = self.lineEdit_2.text()
        output = str(socket.gethostname())
        
        QMessageBox.about(self, "LOGIN WORKS", "Keep Attacking and Have Fun :) ")


        self.tabWidget.setCurrentIndex(1)








     



    def attack(self):

        if self.radioButton.isChecked():




            self.thread_started = Threadclass()
            self.thread_started.start()
            self.thread_started.text.connect(self.label_4.setText)
            self.thread_started.userps.connect(self.label_7.setText)
            self.thread_started.fld.connect(self.label_5.setText)
            self.thread_started.messagestatus.connect(self.label_6.setText)





        else:

            self.thread_started = Attack2()
            self.thread_started.start()
            self.thread_started.text.connect(self.label_4.setText)
            self.thread_started.userps.connect(self.label_7.setText)
            self.thread_started.fld.connect(self.label_5.setText)
            self.thread_started.messagestatus.connect(self.label_6.setText)


counter = 0
long = 0
faildnumber = 0 

numberreport = 0


class Threadclass(QThread):
    text = pyqtSignal(str)
    userps = pyqtSignal(str)
    fld = pyqtSignal(str)
    messagestatus = pyqtSignal(str)

    def __init__(self,parent=None):
        QThread.__init__(self,parent=parent)
        self.isRunning = True

    def run(self):
        global counter
        global long
        global faildnumber
        global numberreport

        mytarget = open("target.txt","r").read().splitlines()
        user_target = mytarget[0]
        print("your target is ",user_target)
        rlogin = requests.Session()
        loginuseragent = "Instagram 93.1.0.19.102 Android (21/5.0.2; 240dpi; 540x960; samsung; SM-G530H; fortuna3g; qcom; ar_AE; 154400379)"
        rlogin.headers = {'user-agent': loginuseragent}

        url = "https://www.instagram.com/" + user_target
        r = rlogin.get(url).text
        try:

        

            reg = re.findall('profilePage_(.+?)",', r)[0]
            s.append(str(reg))
            print("user Id ",reg)


        except:
            print("try again later")
            sys.exit()
        while self.isRunning:
            try:



                with requests.Session() as r:
                    counter += 1
                    if counter == 3:
                        self.fld.emit('''<p><span style="color:#fb6666;">[-] TIME TO SLEEP 60 SEC[-]</span>''')
                        counter = 0 

                        time.sleep(60)
                    if long == 3:
                        self.fld.emit('''<p><span style="color:#fb6666;">[-] Long Time sleep !![-]</span>''')

                        time.sleep(200)
                        long = 0
                    url = "https://i.instagram.com/accounts/login/ajax/"
                    main = str(random.choice(account))
                    user = main.split(":")[0]
                    password = main.split(":")[1]
                    self.userps.emit('''<p><span style="color:#fb6666;">{}:{}</span>'''.format(user,password))

                    uid = str(uuid.uuid4())



                    url = "https://i.instagram.com/api/v1/accounts/login/"

                    headers = {
                        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "en-US",
                        "X-IG-Capabilities": "3brTvw==",
                        "X-IG-Connection-Type": "WIFI",
                        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        'Host': 'i.instagram.com'
                    }


                    data = {
                        '_uuid': uid,
                        'password': password,
                        'username': user,
                        'device_id': uid,
                        'from_reg': 'false',
                        '_csrftoken': 'missing',
                        'login_attempt_count': '0'
                    }



                    loginreq = r.post(url, data=data, headers=headers,allow_redirects=True)
                    text = str(loginreq.json())

                    target = str(random.choice(s))
                    if text.find("is_private") >= 0:
                        r.headers.update({'X-CSRFToken': loginreq.cookies['csrftoken']})
                        numberreport+=1



                        urlRep = "https://i.instagram.com/users/" + str(target) + "/report/"
                        datas = {
                            'source_name': '', 'reason_id': 1, 'frx_context': ''# Spam 
                        }
                        req_SessionID = r.post(urlRep, data=datas)
                        if req_SessionID.text.find("description") >=0:
                            numberreport+=1
                            self.text.emit('''<p><span style="color: #00ee0b;">Works:{}</span>'''.format(str(numberreport)))

                        datas = {
                            'source_name': '', 'reason_id': 6, 'frx_context': ''# Hate Speache
                        }
                        r.headers.update({'X-CSRFToken': loginreq.cookies['csrftoken']})
                        req_SessionID = r.post(urlRep, data=datas)

                        if req_SessionID.text.find('description') >= 0:
                            numberreport += 1
                            self.text.emit('''<p><span style="color: #00ee0b;">Works:{}</span>'''.format(str(numberreport)))
                        time.sleep(1)
                        if req_SessionID.status_code != 200:
                            print("[-] TIME TO SLEEP [-]")
                            faildnumber+=1

                            time.sleep(30)
                        datas = {
                            'source_name': '', 'reason_id': 7, 'frx_context': ''# Harassment & Bullying
                        }

                        time.sleep(1)
                        req_SessionID = r.post(urlRep, data=datas)
                        time.sleep(1)
                        if req_SessionID.text.find('description') >= 0:
                            numberreport += 1
                            self.text.emit('''<p><span style="color: #00ee0b;">Works:{}</span>'''.format(str(numberreport)))
                        if req_SessionID.status_code != 200:
                            print("[-] TIME TO SLEEP [-]")
                            faildnumber+=1
                            self.fld.emit('''<p><span style="color:#fb6666;">Faild:{}</span>'''.format(str(faildnumber)))

                            time.sleep(30)

                        datas = {
                            'source_name': '', 'reason_id': 5, 'frx_context': ''# Violence or threat of violence
                        }

                        req_SessionID = r.post(urlRep, data=datas)
                        time.sleep(1)
                        if req_SessionID.text.find('description') >= 0:
                            numberreport += 1
                            self.text.emit('''<p><span style="color: #00ee0b;">Works:{}</span>'''.format(str(numberreport)))
                        if req_SessionID.status_code != 200:
                            print("[-] TIME TO SLEEP [-]")
                            self.fld.emit('''<p><span style="color:#fb6666;">Faild:{}</span>'''.format(str(faildnumber)))

                            time.sleep(30)
                            long += 1

                        datas = {
                            'source_name': '', 'reason_id': 4, 'frx_context': ''# Nudeity & PornGraphy
                        }
                        req_SessionID = r.post(urlRep, data=datas)
                        time.sleep(1)

                        if req_SessionID.text.find('description') >= 0:
                            numberreport += 1
                            self.text.emit('''<p><span style="color: #00ee0b;">Works:{}</span>'''.format(str(numberreport)))
                        if req_SessionID.status_code != 200:
                            print("[-] TIME TO SLEEP [-]")
                            faildnumber+=1
                            self.fld.emit('''<p><span style="color:#fb6666;">Faild:{}</span>'''.format(str(faildnumber)))

                            time.sleep(30)

                        datas = {
                            'source_name': '', 'reason_id': 2, 'frx_context': ''# Self Injury 
                        }
                        req_SessionID = r.post(urlRep, data=datas)
                        if req_SessionID.text.find('description') >= 0:
                            numberreport += 1
                            self.text.emit('''<p><span style="color: #00ee0b;">Works:{}</span>'''.format(str(numberreport)))
                        if req_SessionID.status_code != 200:
                            print("[-] TIME TO SLEEP [-]")
                            faildnumber+=1
                            self.fld.emit('''<p><span style="color:#fb6666;">Faild:{}</span>'''.format(str(faildnumber)))

                            time.sleep(30)
                        datas = {
                            'source_name': '', 'reason_id': 3, 'frx_context': ''# Drugs
                        }
                        req_SessionID = r.post(urlRep, data=datas)
                        time.sleep(0.5)

                        if req_SessionID.text.find('description') >= 0:
                            numberreport += 1
                            self.text.emit('''<p><span style="color: #00ee0b;">Works:{}</span>'''.format(str(numberreport)))
                        if req_SessionID.status_code != 200:
                            print("[-] TIME TO SLEEP [-]")
                            faildnumber+=1
                            self.fld.emit('''<p><span style="color:#fb6666;">Faild:{}</span>'''.format(str(faildnumber)))

                            time.sleep(30)
                    elif text.find("/challenge")>=0:
                        print(f"user:{user} Password:{password}")
                        self.messagestatus.emit('''<p><span style="color:#fb6666;">Secured{}:{}</span>'''.format(str(user,password)))

                    else:
                        print(f"user:{user} Password:{password}")
                        self.messagestatus.emit('''<p><span style="color:#fb6666;">Ban</span>'''.format(str(user,password)))

            except Exception as e:
                
                self.messagestatus.emit('''<p><span style="color:#fb6666;">{} </span>'''.format(str(text)))


                    
    def Stop(self):
        self.isRunning = False
        self.wait()

class Attack2(QThread):
    text = pyqtSignal(str)
    userps = pyqtSignal(str)
    fld = pyqtSignal(str)
    messagestatus = pyqtSignal(str)
    def __init__(self,parent=None):
        QThread.__init__(self,parent=parent)
        self.isRunning = True

    def run(self):
        global counter
        global long
        global faildnumber
        global numberreport
        mytarget = open("target.txt","r").read().splitlines()
        user_target = mytarget[0]
        print("your target is ",user_target)
        rlogin = requests.Session()
        loginuseragent = "Instagram 93.1.0.19.102 Android (21/5.0.2; 240dpi; 540x960; samsung; SM-G530H; fortuna3g; qcom; ar_AE; 154400379)"
        rlogin.headers = {'user-agent': loginuseragent}

        url = "https://www.instagram.com/" + user_target
        print("Getting User ID ")
        r = rlogin.get(url).text
        try:

        

            reg = re.findall('profilePage_(.+?)",', r)[0]
            s.append(str(reg))

            print("user Id :",reg)


        except:
            print("try again later")
            sys.exit()

        while self.isRunning:

            try:
                print("Re Login")

                with requests.Session() as r:

                    if long == 3:
                        self.fld.emit('''<p><span style="color:#fb6666;">[-] Long Time sleep !![-]</span>''')
                        time.sleep(200)
                        long = 0
                    main = str(random.choice(account))
                    user = main.split(":")[0]
                    password = main.split(":")[1]
                    

                    pro = str(random.choice(prox))
                    NewProxies = {
                    'http': 'http://{}'.format(pro),
                    'https': 'http://{}'.format(pro),}

                    r.proxies = NewProxies
                    uid = str(uuid.uuid4())



                    url = "https://i.instagram.com/api/v1/accounts/login/"

                    headers = {
                        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
                        "Accept": "*/*",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "en-US",
                        "X-IG-Capabilities": "3brTvw==",
                        "X-IG-Connection-Type": "WIFI",
                        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        'Host': 'i.instagram.com'
                    }


                    data = {
                        '_uuid': uid,
                        'password': password,
                        'username': user,
                        'device_id': uid,
                        'from_reg': 'false',
                        '_csrftoken': 'missing',
                        'login_attempt_count': '0'
                    }



                    loginreq = r.post(url, data=data, headers=headers,allow_redirects=True)
                    self.userps.emit('''<p><span style="color:#fb6666;">{}:{}</span>'''.format(user,password))

                    text = str(loginreq.json())

                    target = str(random.choice(s))
                    if text.find("is_private") >= 0:




                        urlRep = "https://i.instagram.com/users/" + str(target) + "/report/"
                        datas = {
                            'source_name': '', 'reason_id': 1, 'frx_context': ''
                        }
                        r.headers.update({'X-CSRFToken': loginreq.cookies['csrftoken']})
                        req_SessionID = r.post(urlRep, data=datas,timeout=5)
                        if req_SessionID.text.find("description") >=0:
                            numberreport+=1
                            self.text.emit('''<p><span style="color: #00ee0b;">Works:{}</span>'''.format(str(numberreport)))

                        datas = {
                            'source_name': '', 'reason_id': 6, 'frx_context': ''
                        }
                        r.headers.update({'X-CSRFToken': loginreq.cookies['csrftoken']})
                        req_SessionID = r.post(urlRep, data=datas,timeout=5)

                        if req_SessionID.text.find('description') >= 0:
                            numberreport += 1
                            self.text.emit('''<p><span style="color: #00ee0b;">Works:{}</span>'''.format(str(numberreport)))
                        if req_SessionID.status_code != 200:
                            print("[-] TIME TO SLEEP [-]")
                            faildnumber+=1
                            self.fld.emit('''<p><span style="color:#fb6666;">Faild:{}</span>'''.format(str(faildnumber)))

                            time.sleep(30)
                        datas = {
                            'source_name': '', 'reason_id': 7, 'frx_context': ''
                        }

                        req_SessionID = r.post(urlRep, data=datas,timeout=5)
                        if req_SessionID.text.find('description') >= 0:
                            numberreport += 1
                            self.text.emit('''<p><span style="color: #00ee0b;">Works:{}</span>'''.format(str(numberreport)))
                        if req_SessionID.status_code != 200:
                            print("[-] TIME TO SLEEP [-]")
                            faildnumber+=1
                            self.fld.emit('''<p><span style="color:#fb6666;">Faild:{}</span>'''.format(str(faildnumber)))

                            time.sleep(30)

                        datas = {
                            'source_name': '', 'reason_id': 5, 'frx_context': ''
                        }

                        req_SessionID = r.post(urlRep, data=datas,timeout=5)
                        if req_SessionID.text.find('description') >= 0:
                            numberreport += 1
                            self.text.emit('''<p><span style="color: #00ee0b;">Works:{}</span>'''.format(str(numberreport)))
                        if req_SessionID.status_code != 200:
                            print("[-] TIME TO SLEEP [-]")
                            time.sleep(30)
                            long += 1

                        datas = {
                            'source_name': '', 'reason_id': 4, 'frx_context': ''
                        }
                        req_SessionID = r.post(urlRep, data=datas,timeout=5)

                        if req_SessionID.text.find('description') >= 0:
                            numberreport += 1
                            self.text.emit('''<p><span style="color: #00ee0b;">Works:{}</span>'''.format(str(numberreport)))
                        if req_SessionID.status_code != 200:
                            print("[-] TIME TO SLEEP [-]")
                            faildnumber+=1
                            self.fld.emit('''<p><span style="color:#fb6666;">Faild:{}</span>'''.format(str(faildnumber)))

                            time.sleep(30)

                        datas = {
                            'source_name': '', 'reason_id': 2, 'frx_context': ''
                        }
                        req_SessionID = r.post(urlRep, data=datas,timeout=5)
                        if req_SessionID.text.find('description') >= 0:
                            numberreport += 1
                            self.text.emit('''<p><span style="color: #00ee0b;">Works:{}</span>'''.format(str(numberreport)))
                        if req_SessionID.status_code != 200:
                            print("[-] TIME TO SLEEP [-]")
                            faildnumber+=1
                            self.fld.emit('''<p><span style="color:#fb6666;">Faild:{}</span>'''.format(str(faildnumber)))

                            time.sleep(30)
                        datas = {
                            'source_name': '', 'reason_id': 3, 'frx_context': ''
                        }
                        req_SessionID = r.post(urlRep, data=datas,timeout=5)

                        if req_SessionID.text.find('description') >= 0:
                            numberreport += 1
                            self.text.emit('''<p><span style="color: #00ee0b;">Works:{}</span>'''.format(str(numberreport)))
                        if req_SessionID.status_code != 200:
                            print("[-] TIME TO SLEEP [-]")
                            faildnumber+=1
                            self.fld.emit('''<p><span style="color:#fb6666;">Faild:{}</span>'''.format(str(faildnumber)))

                            time.sleep(30)
                    else:
                        self.messagestatus.emit('''<p><span style="color:#fb6666;">{} </span>'''.format(str(text)))


            except Exception as e:
                e = str(e)
                

                faildnumber+=1
                if e.find("Cannot connect to proxy.") >=0:

                    self.messagestatus.emit('''<p><span style="color:#fb6666;">{} </span>'''.format(str(e)))




                self.fld.emit('''<p><span style="color:#fb6666;">Faild:{}</span>'''.format(str(faildnumber)))
            

    def Stop(self):
        self.isRunning = False
        self.wait()





def second():
    app = QApplication(sys.argv)
    widget = Main()
    widget.show()
    sys.exit(app.exec())

if __name__ == '__main__':

    second()
