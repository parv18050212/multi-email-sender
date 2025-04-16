from flask import Flask, request, jsonify, render_template
import smtplib
from email.message import EmailMessage
from flask_cors import CORS

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

EMAIL_ADDRESS = 'nupur@vize.co.in'
EMAIL_PASSWORD = 'ogio wzhq cdwc nyrg'

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/send-mails', methods=['POST'])
def send_mails():
    data = request.get_json()
    recipients = data['recipients']
    subject = data['subject']
    content = data['content']

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg.set_content(content)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            for email in recipients:
                msg['To'] = email.strip()
                smtp.send_message(msg)
                del msg['To']
        return jsonify({'status': 'success', 'message': 'Emails sent!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
