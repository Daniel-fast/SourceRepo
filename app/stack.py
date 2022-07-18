import logging
import logging.handlers
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
 
class TlsSMTPHandler(logging.handlers.SMTPHandler):
    def emit(self, record):
        """
        Emit a record.
 
        Format the record and send it to the specified addressees.
        """
        try:
            import smtplib
            import string # for tls add this line
            try:
                from email.utils import formatdate
            except ImportError:
                formatdate = self.date_time
            port = self.mailport
            if not port:
                port = smtplib.SMTP_PORT
            smtp = smtplib.SMTP(self.mailhost, port)
            message = MIMEMultipart()
            message['From'] = "danielsdn0725@gmail.com"
            message['To'] = "daniel@fasti.digital"
            message['Subject'] = "This is a test"
            message.attach(MIMEMultipart("Body"))
            msg = self.format(record)
            msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\nDate: %s\r\n\r\n%s" % (
                            self.fromaddr,
                            string.join(self.toaddrs, ","),
                            self.getSubject(record),
                            formatdate(), msg)
            if self.username:
                smtp.ehlo() # for tls add this line
                smtp.starttls() # for tls add this line
                smtp.ehlo() # for tls add this line
                smtp.login(self.username, self.password)
            smtp.sendmail(self.fromaddr, self.toaddrs, msg)
            smtp.quit()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)
 
logger = logging.getLogger()
 
gm = TlsSMTPHandler(("smtp.gmail.com", 587), 'danielsdn0725@gmail.com', ['danielsdn0725@gmail.com', 'danielsdn0725@gmail.com', 'danielsdn0725@gmail.com'], 'unable to find Error!', ('danielsdn0725@gmail.com', 'Dash@0129'))
gm.setLevel(logging.ERROR)
 
logger.addHandler(gm)
 
try:
    1/0
except:
    logger.exception('FFFFFFFFFFFFFFFFFFFFFFFUUUUUUUUUUUUUUUUUUUUUU-')
    
    
    
