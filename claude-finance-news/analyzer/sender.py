#!/usr/bin/env python3
import smtplib
from email.message import EmailMessage
from datetime import *
import os 


def sender():

    with open ("antwort.txt" , "r") as file:
        context = file.read()
    print(context)

    # Datum in kurzes Format bringen 
    time = datetime.today()
    time=str(time)
    cut_datum = time[0:10]
    print(cut_datum)

    GOOGLE_KEY = os.getenv("GOOGLE_KEY")
    GOOGLE_KEY=str(GOOGLE_KEY)
    

    #app - pw unbedingt nach Fertigstellung löschen 
    ACCOUNT="megimesser96@gmail.com"
    TARGET="heinze.obach@web.de"

    msg = EmailMessage()
    msg["Subject"] = f"{cut_datum}"
    msg["From"] = ACCOUNT
    msg["To"] = TARGET

    msg.set_content(context)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(ACCOUNT, GOOGLE_KEY)
        smtp.send_message(msg)


