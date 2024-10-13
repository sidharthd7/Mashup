import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv('EMAIL_ADDRESS')

def send_email(file_path, recipient_email):
    subject = "Your Mashup result is here"
    body = "Please find the audio file attached"
    
    try:
        yag = yagmail.SMTP(sender_email)
        yag.send(
            to = recipient_email,
            subject=subject,
            contents= body,
            attachments=file_path
        )
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email : {e}')