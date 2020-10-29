# this just mails the ip of the external so we can get in when needed
def mailer():
    import pandas as pd
    import smtplib
    df=pd.read_csv('infos.txt',sep="=",header=None)
    f=open("ip.txt","r")
    sendAddy=df[1][0]
    print(sendAddy)
    sendPW=df[1][1]
    print(sendPW)
    destEmail=df[1][3]
    print(destEmail)    
    smtpServer=smtplib.SMTP('smtp.gmail.com',587)
    smtpServer.starttls()
    smtpServer.login(sendAddy,sendPW)
    smtpServer.sendmail(sendAddy,destEmail,"SUBJECT:"+str(f.readline())+" ip Report ")
    f.close()
    smtpServer.quit()


#MAIN 
mailer()

# note you need an infos.txt file in the following format : in the same directory 
sendAddy=senderemailaccount
sendPwd=senderemailPassword
server=smtplib.SMTP('smtp.gmail.com',587)
dest=destinationemailaddress

