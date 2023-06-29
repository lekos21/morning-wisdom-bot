import functions_framework
from flask import make_response
import openai
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

openai.api_key = 'your-api-key'

def send_email(subject, message, to):
    from_email = 'sender@gmail.com'
    password = 'your-password'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    server.send_message(msg)
    server.quit()

@functions_framework.http
def hello_http(request):
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Quote a cool and positive sentence from a philosopher's book, then proceed to explain its significance. I will read it after I wake up to give me the energy for the day, so in the end add some general advice for the day."},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    sentence = response['choices'][0]['message']['content']

    send_email('Your Morning Wisdom', sentence, 'receiver@gmail.com')

    return make_response('Email sent!', 200)
