import smtplib
print( "1.Google Mail Server\n2.Yahoo Mail Server")
choice = input( "Enter your choice : ")
if( choice == 1 ):
    server = smtplib.SMTP( "smtp.gmail.com:587" )
else:
    server = smtplib.SMTP( "smtp.mail.yahoo.com:587" )
print()
Email_ID = input( "Enter your Email ID : " )
Password = input( "Enter your Password : ")
print()
Rec_Email = input( "Enter Reciever's Address : " )
Subject = input( "Enter Email Subject : " )
Message = input( "Enter the message you want to send : " )
msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % ( Email_ID, Rec_Email, Subject, Message)
server.starttls()
server.login( Email_ID, Password )
server.sendmail( Email_ID, Rec_Email, msg )
server.quit()
print("\nMail Successfully Sent")
