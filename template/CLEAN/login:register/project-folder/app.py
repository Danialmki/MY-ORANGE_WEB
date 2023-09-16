from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    print(request.form)  # Print the form data for debugging
    email = request.form.get('email')
    password = request.form.get('password')

    sender_email = "your_email@gmail.com"
    recipient_email = email
    subject = "Your Password"
    message = f"Your password is: {password}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, 'your_password')  # Replace with your actual email and password
    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)
    server.quit()

    return "Email sent successfully."

if __name__ == '__main__':
    app.run(debug=True)
