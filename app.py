from flask import Flask, render_template_string, request, redirect, url_for, session
import os
import json
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'bug_new_secret_key_secure_2026'

DATA_FILE = 'users_data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": {}, "history": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {"users": {}, "history": []}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

ACC_LIST = [
    {"id": 1, "name": "Acc FF VIP #1", "level": "10%", "price": "4.400đ", "img": "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=300&q=80"},
    {"id": 2, "name": "Acc FF VIP #2", "level": "10%", "price": "4.400đ", "img": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=300&q=80"},
    {"id": 3, "name": "Acc FF VIP #3", "level": "10%", "price": "11.000đ", "img": "https://images.unsplash.com/photo-1511512578047-dfb367046420?w=300&q=80"},
    {"id": 4, "name": "Acc FF VIP #4", "level": "10%", "price": "11.000đ", "img": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=300&q=80"},
    {"id": 5, "name": "Acc FF VIP #5", "level": "10%", "price": "2.200đ", "img": "https://images.unsplash.com/photo-1560253023-3ec5d502959f?w=300&q=80"},
    {"id": 6, "name": "Acc FF VIP #6", "level": "10%", "price": "2.200đ", "img": "https://images.unsplash.com/photo-1579373903781-fd5c0c30c4cd?w=300&q=80"},
    {"id": 7, "name": "Acc FF VIP #7", "level": "10%", "price": "5.500đ", "img": "https://images.unsplash.com/photo-1612287233002-ef1d014f3da3?w=300&q=80"},
    {"id": 8, "name": "Acc FF VIP #8", "level": "10%", "price": "5.500đ", "img": "https://images.unsplash.com/photo-1589241062272-c0a000071dfa?w=300&q=80"},
    {"id": 9, "name": "Acc FF VIP #9", "level": "10%", "price": "11.000đ", "img": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=300&q=80"},
    {"id": 10, "name": "Acc FF VIP #10", "level": "10%", "price": "11.000đ", "img": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=300&q=80"}
]

PRICING_CARDS = [
    {"likes": "220 Likes", "price": "4.400đ"},
    {"likes": "1.100 Likes", "price": "11.000đ"},
    {"likes": "2.200 Likes", "price": "22.000đ"},
    {"likes": "4.500 Likes", "price": "45.000đ"}
]

@app.route('/auth', methods=['GET', 'POST'])
def auth_page():
    error = success = None
    if request.method == 'POST':
        action, username, password, gmail = request.form.get('action'), request.form.get('username', '').strip(), request.form.get('password', '').strip(), request.form.get('gmail', '').strip()
        data = load_data()
        if action == 'register':
            if not username or not password or not gmail: error = "Vui lòng nhập đủ thông tin!"
            elif username in data["users"]: error = "Tài khoản đã tồn tại!"
            elif any(u.get('gmail') == gmail for u in data["users"].values()): error = "Gmail đã được dùng cho tài khoản khác!"
            else:
                data["users"][username] = {"password": password, "gmail": gmail, "coins": 200, "claimed_today": False}
                save_data(data)
                success = "Đăng ký thành công!"
        elif action == 'login':
            if username in data["users"] and data["users"][username]["password"] == password:
                session['username'] = username
                return redirect(url_for('index'))
            else: error = "Sai tài khoản hoặc mật khẩu!"
    return render_template_string('''
    <!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8"><title>Auth</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body{background:#030712;color:#fff;font-family:'Orbitron',sans-serif;display:flex;justify-content:center;align-items:center;height:100vh;margin:0}
        .box{background:#0f172a;border:2px solid #38bdf8;padding:25px;border-radius:12px;width:320px;box-shadow:0 0 20px rgba(56,189,248,0.3)}
        input{width:100%;padding:10px;margin:8px 0;background:#030712;border:1px solid #334155;color:#fff;border-radius:6px}
        button{width:100%;padding:10px;background:#38bdf8;border:0;font-weight:bold;border-radius:6px;cursor:pointer;margin-top:10px}
    </style></head><body>
    <div class="box">
        <h3 style="text-align:center;color:#38bdf8;margin-bottom:15px">BUG NEW AUTH</h3>
        {% if error %}<p style="color:#fca5a5;font-size:12px;text-align:center">{{error}}</p>{% endif %}
        {% if success %}<p style="color:#86efac;font-size:12px;text-align:center">{{success}}</p>{% endif %}
        <form method="POST"><input type="hidden" name="action" value="login">
            <input type="text" name="username" placeholder="Tài khoản" required>
            <input type="password" name="password" placeholder="Mật khẩu" required>
            <button type="submit">ĐĂNG NHẬP</button>
        </form>
        <hr style="border:0;border-top:1px solid #334155;margin:15px 0">
        <form method="POST"><input type="hidden" name="action" value="register">
            <input type="text" name="username" placeholder="Tài khoản mới" required>
            <input type="email" name="gmail" placeholder="Gmail bảo mật" required>
            <input type="password" name="password" placeholder="Mật khẩu" required>
            <button type="submit" style="background:#ec4899;color:#fff">ĐĂNG KÝ (1 GMAIL)</button>
        </form>
    </div></body></html>''', error=error, success=success)

@app.route('/')
def index():
    if 'username' not in session: return redirect(url_for('auth_page'))
    data = load_data()
    username = session['username']
    user_info = data["users"].get(username, {"coins": 0})
    return render_template_string('''
    <!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8"><title>Shop Bug New</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body{background:#030712;color:#fff;font-family:'Orbitron',sans-serif;margin:0;padding:15px}
        header{display:flex;justify-content:space-between;align-items:center;background:#0f172a;padding:12px 20px;border-bottom:2px solid #38bdf8;border-radius:8px}
        .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px;margin-top:15px}
        .card{background:#0f172a;border:1px solid #334155;border-radius:8px;text-align:center;padding:10px}
        .card img{width:100%;height:100px;object-fit:cover;border-radius:6px}
        button{background:#22c55e;border:0;padding:6px 12px;color:#000;font-weight:bold;border-radius:4px;cursor:pointer;margin-top:8px}
    </style></head><body>
    <header>
        <span>⚡ <b>{{username}}</b> | 🪙 {{user_info.coins}} Xu</span>
        <div>
            <a href="/blind_bag" style="color:#f43f5e;text-decoration:none;margin-right:15px;font-weight:bold">🎁 Túi Mù</a>
            <a href="/logout" style="color:#ef4444;text-decoration:none;font-weight:bold">Thoát</a>
        </div>
    </header>
    <h3 style="color:#38bdf8;margin:20px 0 10px">🔥 KHO ACC FREE FIRE</h3>
    <div class="grid">
        {% for acc in acc_list %}
        <div class="card">
            <img src="{{acc.img}}" alt="">
            <p style="font-size:12px;margin:6px 0">{{acc.name}}</p>
            <b style="color:#22c55e;font-size:12px">{{acc.price}}</b><br>
            <button onclick="alert('Liên hệ Admin qua Facebook!')">MUA</button>
        </div>
        {% endfor %}
    </div></body></html>''', username=username, user_info=user_info, acc_list=ACC_LIST)

@app.route('/blind_bag', methods=['GET', 'POST'])
def blind_bag():
    if 'username' not in session: return redirect(url_for('auth_page'))
    data = load_data()
    username = session['username']
    user_info = data["users"].get(username, {"coins": 0})
    msg = None
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'claim' and not user_info.get("claimed_today"):
            user_info["coins"] += 200
            user_info["claimed_today"] = True
            data["history"].insert(0, {"time": datetime.now().strftime("%H:%M"), "text": f"{username} điểm danh +200 xu"})
            save_data(data)
            msg = "Nhận thành công 200 Xu!"
        elif action == 'open':
            if user_info["coins"] >= 75:
                user_info["coins"] -= 75
                r = random.choice(["50 Likes FF", "100 Likes FF", "Acc VIP", "Trượt mất rồi"])
                data["history"].insert(0, {"time": datetime.now().strftime("%H:%M"), "text": f"{username} mở túi trúng: {r}"})
                save_data(data)
                msg = f"Kết quả: {r}"
            else: msg = "Không đủ 75 xu!"
    return render_template_string('''
    <!DOCTYPE html><html lang="vi"><head><meta charset="UTF-8"><title>Túi Mù</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body{background:#030712;color:#fff;font-family:'Orbitron',sans-serif;text-align:center;padding:20px}
        .box{background:#0f172a;border:2px solid #f43f5e;padding:20px;border-radius:12px;max-width:400px;margin:20px auto;box-shadow:0 0 20px rgba(244,63,94,0.3)}
        button{background:#f43f5e;color:#fff;border:0;padding:10px 20px;font-weight:bold;border-radius:6px;cursor:pointer;margin:5px}
    </style></head><body>
    <a href="/" style="color:#38bdf8;text-decoration:none">⬅ Về Trang Chủ</a>
    <div class="box">
        <h2 style="color:#f43f5e">🎁 TÚI MÙ (75 XU)</h2>
        <p>🪙 Số xu: <b>{{user_info.coins}}</b></p>
        {% if msg %}<p style="color:#fecdd3;font-size:13px">{{msg}}</p>{% endif %}
        <form method="POST"><input type="hidden" name="action" value="claim"><button style="background:#22c55e;color:#000">Nhận 200 Xu Điểm Danh</button></form>
        <form method="POST"><input type="hidden" name="action" value="open"><button>Mở Túi Ngay</button></form>
    </div>
    <div style="max-width:400px;margin:auto;text-align:left;background:#0f172a;padding:15px;border-radius:8px">
        <h4 style="color:#f43f5e;text-align:center;margin-bottom:10px">📜 Lịch Sử Chung</h4>
        {% for h in history %}<p style="font-size:11px;border-bottom:1px solid #1e293b;padding:4px 0">{{h.time}} - {{h.text}}</p>{% endfor %}
    </div></body></html>''', username=username, user_info=user_info, history=data["history"], msg=msg)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('auth_page'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
            
