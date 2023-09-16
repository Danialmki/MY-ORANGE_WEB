from flask import Flask
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__, static_folder='static')  # 'static' should be the folder containing your CSS file


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        recipient_email = request.form['recipient_email']
        sender_email = 'danialmokhtari1999@gmail.com'  # Update with your email
        sender_password = 'hrhs biuh wskl ixnh'      # Update with your email password
        subject = 'YOU ARE GAY'
        message = 'GAAAAAAYYYYYYYY.'

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            server.quit()
            return redirect(url_for('index'))
        except Exception as e:
            return str(e)

if __name__ == '__main__':
    app.run(debug=True)
