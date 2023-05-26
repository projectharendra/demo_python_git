import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

#An app password is a 16-digit passcode that gives a less secure app or device permission to access your Google Account. App passwords can only be used with accounts that have 2-Step Verification turned on.
# https://support.google.com/accounts/answer/185833?hl=en

server.login('project.harendra@gmail.com', 'rvvpefvvgnqwstjb')
server.sendmail('project.harendra@gmail.com', 'hkumarisandhya@gmail.com','Mail Sent from Python')
print('Mail sent')