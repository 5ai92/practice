import smtplib

#Content for the email, we can use mimetext for more than text features
content = "Hi I am testing email script"

#Always store credentials somewhere else :p
with open('mailingstuff.txt' ,'r') as f:
   creds = f.readlines()

# This may change. depends on ur file structure
email_account=creds[0].split('\n')[0]
password = creds[0].split('\n')[0]

#reciepents list
receipents_list = ['dama.bhargavsai@gmail.com']
if len(receipents_list) > 1:
    receipents_list = set(receipents_list))
    receipents=','.join(str(acc) for acc in receipents_list)
elif len(receipents_list) == 1:
    receipents=recipents_list[0]
else:
    receipents_list=''

#sending email through smtplib
mail = smtplib.SMTP('smtp.gmail.com', '587')
mail.ehlo()
mail.starttls()
mail.login(email_account, password)
mail.sendmail(email_account, receipents, content)
mail.close()
