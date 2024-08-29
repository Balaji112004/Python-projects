import smtplib
smartObj=smtplib.SMTP('smtp.gmail.com',587)
smartObj.ehlo()
smartObj.starttls()
smartObj.login("k.balaji112004@gmail.com","K.balaji1@$")
smartObj.send_message("Subject:This is test mail","k.balaji112004@gmail.com","bk8735904@gmail.com")
smartObj.quit()