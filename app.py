import smtplib
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Import CORS
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/thanks')
def thanks():
    return render_template('final.html')


CORS(app, resources={r"/send_ticket": {"origins": "http://127.0.0.1:5500"}})


def send(fullname,email):
  server = smtplib.SMTP("smtp.gmail.com",587)
  server.starttls()
  sender_email = "f20241009@pilani.bits-pilani.ac.in"
  server.login(sender_email,"ocxw uyzs bhdp xkzy")
  subject = "Ticket for Entrepreneurship Summit 2024"
  message = f"Your ticket for the summit is {fullname.split()[0]}_2024.\nThanks for attending!\n\nThis email was generated as part of CEL Tech Task 1 by Medhansh Khandelwal."
  text = f"Subject: {subject}\n\n{message}"
  server.sendmail(sender_email, email, text)
  server.quit()
  print("done")

@app.route('/send_ticket', methods=['POST'])
def send_ticket():
    print("app is working")
    data = request.json
    fullname = data.get('fullname')
    email = data.get('email')
    send(fullname, email)
    return jsonify({"status": "done"}), 200

if __name__ == '__main__':
    app.run(debug=True)

