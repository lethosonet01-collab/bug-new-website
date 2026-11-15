from flask import Flask, render_template_string, request, redirect, url_for, session
import os
import json
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'bug_new_secret_key_secure_2026'

DATA_FILE = 'users_data.json'

# Hàm đọc dữ liệu từ file JSON vĩnh viễn (Chống mất tài khoản khi server ngủ đông)
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": {}, "history": []}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {"users": {}, "history": []}

# Hàm ghi dữ liệu vào file JSON vĩnh viễn
def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        # Danh sách 10 kho Acc Free Fire chuẩn chỉnh
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

# Bảng giá chuẩn cập nhật mới
PRICING_CARDS = [
    {"likes": "220 Likes", "price": "4.400đ"},
    {"likes": "1.100 Likes", "price": "11.000đ"},
    {"likes": "2.200 Likes", "price": "22.000đ"},
    {"likes": "4.500 Likes", "price": "45.000đ"}
]
@app.route('/auth', methods=['GET', 'POST'])
def auth_page():
    error = None
    success = None
    if request.method == 'POST':
        action = request.form.get('action')
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        gmail = request.form.get('gmail', '').strip()
        
        data = load_data()
        
        if action == 'register':
            if not username or not password or not gmail:
                error = "Vui lòng nhập đầy đủ Tên tài khoản, Mật khẩu và Gmail!"
            elif username in data["users"]:
                error = "Tên tài khoản này đã tồn tại!"
            else:
                gmail_exists = any(u_info.get('gmail') == gmail for u_info in data["users"].values())
                if gmail_exists:
                    error = "Gmail này đã được sử dụng cho một tài khoản khác (1 Gmail chỉ 1 tài khoản)!"
                else:
                    data["users"][username] = {
                        "password": password,
                        "gmail": gmail,
                        "coins": 200,
                        "claimed_today": False
                    }
                    save_data(data)
                    success = "Đăng ký thành công! Hãy chuyển sang đăng nhập."
        elif action == 'login':
            if username in data["users"] and data["users"][username]["password"] == password:
                session['username'] = username
                return redirect(url_for('index'))
            else:
                error = "Sai tên tài khoản hoặc mật khẩu!"

    html_auth = """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Đăng Nhập / Đăng Ký - BUG NEW</title>
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
        <style>
            :root { --neon-cyan: #38bdf8; --neon-green: #22c55e; --neon-pink: #ec4899; }
            * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Orbitron', sans-serif; }
            body { background-color: #030712; color: #f8fafc; min-height: 100vh; display: flex; justify-content: center; align-items: center; position: relative; overflow-x: hidden; }
            body::before { content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(0deg, rgba(3,7,18,0.9), rgba(3,7,18,0.7)), repeating-linear-gradient(0deg, transparent, transparent 40px, rgba(56,189,248,0.05) 40px, rgba(56,189,248,0.05) 41px); z-index: -1; }
            .auth-container { background: rgba(15, 23, 42, 0.9); border: 2px solid var(--neon-cyan); border-radius: 16px; width: 90%; max-width: 400px; padding: 30px; box-shadow: 0 0 30px rgba(56, 189, 248, 0.4); backdrop-filter: blur(10px); }
            h2 { text-align: center; color: var(--neon-cyan); margin-bottom: 20px; font-size: 1.5rem; text-shadow: 0 0 10px var(--neon-cyan); }
            .tabs { display: flex; margin-bottom: 20px; border-bottom: 1px solid #334155; }
            .tab { flex: 1; text-align: center; padding: 10px; cursor: pointer; color: #94a3b8; font-weight: 700; transition: 0.3s; }
            .tab.active { color: var(--neon-cyan); border-bottom: 2px solid var(--neon-cyan); text-shadow: 0 0 8px var(--neon-cyan); }
            .form-group { margin-bottom: 15px; }
            label { display: block; font-size: 0.8rem; color: #cbd5e1; margin-bottom: 5px; }
            input { width: 100%; padding: 10px 14px; background: #030712; border: 1px solid #334155; border-radius: 8px; color: #fff; font-size: 0.9rem; outline: none; transition: 0.3s; }
            input:focus { border-color: var(--neon-cyan); box-shadow: 0 0 10px rgba(56, 189, 248, 0.4); }
            .submit-btn { width: 100%; padding: 12px; background: linear-gradient(135deg, var(--neon-cyan), var(--neon-green)); border: none; border-radius: 8px; color: #000; font-weight: 900; font-size: 1rem; cursor: pointer; transition: 0.3s; margin-top: 10px; }
            .submit-btn:hover { box-shadow: 0 0 20px var(--neon-green); transform: translateY(-2px); }
            .alert-err { background: rgba(239, 68, 68, 0.2); border: 1px solid #ef4444; color: #fca5a5; padding: 10px; border-radius: 6px; font-size: 0.8rem; margin-bottom: 15px; text-align: center; }
            .alert-succ { background: rgba(34, 197, 94, 0.2); border: 1px solid var(--neon-green); color: #86efac; padding: 10px; border-radius: 6px; font-size: 0.8rem; margin-bottom: 15px; text-align: center; }
            .form-box { display: none; } .form-box.active { display: block; }
        </style>
    </head>
    <body>
        <div class="auth-container">
            <h2>⚡ BUG NEW ⚡</h2>
            <div class="tabs">
                <div class="tab active" onclick="switchTab('login')">ĐĂNG NHẬP</div>
                <div class="tab" onclick="switchTab('register')">ĐĂNG KÝ</div>
            </div>
            {% if error %}<div class="alert-err">{{ error }}</div>{% endif %}
            {% if success %}<div class="alert-succ">{{ success }}</div>{% endif %}
            <form id="login-form" class="form-box active" method="POST">
                <input type="hidden" name="action" value="login">
                <div class="form-group"><label>Tên tài khoản</label><input type="text" name="username" required placeholder="Nhập tên tài khoản..."></div>
                <div class="form-group"><label>Mật khẩu</label><input type="password" name="password" required placeholder="Nhập mật khẩu..."></div>
                <button type="submit" class="submit-btn">ĐĂNG NHẬP NGAY</button>
            </form>
            <form id="register-form" class="form-box" method="POST">
                <input type="hidden" name="action" value="register">
                <div class="form-group"><label>Tên tài khoản mới</label><input type="text" name="username" required placeholder="Chọn tên tài khoản..."></div>
                <div class="form-group"><label>Gmail bảo mật (1 Gmail / 1 Tài khoản)</label><input type="email" name="gmail" required placeholder="example@gmail.com"></div>
                <div class="form-group"><label>Mật khẩu</label><input type="password" name="password" required placeholder="Tạo mật khẩu..."></div>
                <button type="submit" class="submit-btn" style="background: linear-gradient(135deg, var(--neon-pink), var(--neon-cyan));">ĐĂNG KÝ TÀI KHOẢN</button>
            </form>
        </div>
        <script>
            function switchTab(tabName) {
                document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
                document.querySelectorAll('.form-box').forEach(f => f.classList.remove('active'));
                if(tabName === 'login') { document.querySelectorAll('.tab')[0].classList.add('active'); document.getElementById('login-form').classList.add('active'); }
                else { document.querySelectorAll('.tab')[1].classList.add('active'); document.getElementById('register-form').classList.add('active'); }
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html_auth, error=error, success=success)

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('auth_page'))
    data = load_data()
    username = session['username']
    user_info = data["users"].get(username, {"coins": 0})
    
    html_template = """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SHOP BUG NEW - Trang Chủ</title>
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
        <style>
            :root { --bg-color: #030712; --panel-bg: rgba(15, 23, 42, 0.85); --neon-cyan: #38bdf8; --neon-blue: #0284c7; --neon-green: #22c55e; --text-main: #f8fafc; }
            * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Orbitron', sans-serif; }
            body { background-color: var(--bg-color); color: var(--text-main); min-height: 100vh; overflow-x: hidden; position: relative; }
            body::before { content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(180deg, rgba(2,132,199,0.08) 0%, rgba(3,7,18,0.95) 100%); z-index: -1; pointer-events: none; }
            header { display: flex; justify-content: space-between; align-items: center; padding: 15px 20px; background: rgba(15, 23, 42, 0.95); border-bottom: 2px solid var(--neon-cyan); box-shadow: 0 0 15px rgba(56, 189, 248, 0.3); position: sticky; top: 0; z-index: 100; }
            .logo { font-size: 1.2rem; font-weight: 900; color: var(--neon-cyan); text-shadow: 0 0 10px var(--neon-cyan); }
            .user-bar { display: flex; align-items: center; gap: 12px; font-size: 0.9rem; }
            .coin-badge { background: #1e293b; border: 1px solid var(--neon-green); padding: 5px 10px; border-radius: 20px; color: var(--neon-green); font-weight: 700; }
            .nav-btn { background: transparent; border: 1px solid var(--neon-cyan); color: var(--neon-cyan); padding: 6px 12px; border-radius: 6px; cursor: pointer; text-decoration: none; font-size: 0.8rem; transition: 0.3s; }
            .nav-btn:hover { background: var(--neon-cyan); color: #000; box-shadow: 0 0 10px var(--neon-cyan); }
            .logout-btn { border-color: #ef4444; color: #ef4444; } .logout-btn:hover { background: #ef4444; color: #fff; box-shadow: 0 0 10px #ef4444; }
            .container { max-width: 1000px; margin: 20px auto; padding: 0 15px; }
            .section-title { text-align: center; font-size: 1.4rem; color: var(--neon-cyan); margin: 25px 0 15px; text-shadow: 0 0 10px rgba(56,189,248,0.5); text-transform: uppercase; }
            .card-pod { background: var(--panel-bg); border: 1px solid var(--neon-blue); border-radius: 12px; padding: 20px; margin-bottom: 20px; box-shadow: 0 0 20px rgba(2,132,199,0.2); transition: 0.3s; }
            .card-pod:hover { transform: translateY(-4px); box-shadow: 0 0 25px rgba(56, 189, 248, 0.4); border-color: var(--neon-cyan); }
            .notice-box { background: rgba(239, 68, 68, 0.1); border: 1px solid #ef4444; color: #fca5a5; padding: 12px; border-radius: 8px; text-align: center; font-weight: 700; margin-bottom: 20px; }
            .acc-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 15px; }
            .acc-card { background: #0f172a; border: 1px solid #1e293b; border-radius: 10px; overflow: hidden; transition: all 0.3s ease; text-align: center; padding-bottom: 12px; }
            .acc-card:hover { transform: scale(1.03); border-color: var(--neon-cyan); box-shadow: 0 0 15px rgba(56, 189, 248, 0.5); }
            .acc-card img { width: 100%; height: 110px; object-fit: cover; border-bottom: 1px solid #1e293b; }
            .acc-card h4 { font-size: 0.9rem; margin: 8px 0; color: #fff; }
            .acc-card p { font-size: 0.8rem; color: #94a3b8; margin-bottom: 10px; }
            .buy-btn { background: var(--neon-green); color: #000; border: none; padding: 6px 14px; font-weight: 900; border-radius: 6px; cursor: pointer; font-size: 0.75rem; transition: 0.2s; }
            .buy-btn:hover { background: #16a34a; box-shadow: 0 0 10px var(--neon-green); color: #fff; }
            .pricing-table { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; }
            .price-item { background: #1e293b; border: 1px solid #334155; padding: 12px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; transition: 0.3s; }
            .price-item:hover { border-color: var(--neon-cyan); background: #0f172a; }
            .price-val { color: var(--neon-green); font-weight: 700; }
        </style>
    </head>
    <body>
        <header>
            <div class="logo">⚡ SHOP BUG NEW</div>
            <div class="user-bar">
                <span class="coin-badge">🪙 {{ user_info.coins }} Xu</span>
                <span>👤 {{ username }}</span>
                <a href="/blind_bag" class="nav-btn">🎁 Túi Mù</a>
                <a href="/logout" class="nav-btn logout-btn">Đăng Xuất</a>
            </div>
        </header>
        <div class="container">
            <div class="section-title">🔥 Dịch Vụ Buff Likes & Game FF 🔥</div>
            <div class="notice-box">⚠️ LƯU Ý: Mỗi ngày chỉ tối đa 220 likes / ngày!</div>
            <div class="card-pod">
                <h3 style="color: var(--neon-cyan); margin-bottom: 12px; font-size: 1.1rem;">📋 Bảng Giá Dịch Vụ Likes</h3>
                <div class="pricing-table">
                    {% for p in pricing_cards %}
                    <div class="price-item"><span>👍 {{ p.likes }}</span><span class="price-val">{{ p.price }}</span></div>
                    {% endfor %}
                </div>
            </div>
            <div class="section-title">🔥 Kho Acc Free Fire VIP 🔥</div>
            <div class="acc-grid">
                {% for acc in acc_list %}
                <div class="acc-card">
                    <img src="{{ acc.img }}" alt="{{ acc.name }}">
                    <h4>{{ acc.name }}</h4>
                    <p>Level: {{ acc.level }} | <b>{{ acc.price }}</b></p>
                    <button class="buy-btn" onclick="alert('Vui lòng liên hệ Admin qua Facebook/Telegram để mua tài khoản này!')">MUA NGAY</button>
                </div>
                {% endfor %}
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, username=username, user_info=user_info, pricing_cards=PRICING_CARDS, acc_list=ACC_LIST)
    @app.route('/blind_bag', methods=['GET', 'POST'])
def blind_bag():
    if 'username' not in session:
        return redirect(url_for('auth_page'))
    data = load_data()
    username = session['username']
    user_info = data["users"].get(username, {"coins": 0})
    
    msg = None
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'claim':
            if not user_info.get("claimed_today", False):
                user_info["coins"] += 200
                user_info["claimed_today"] = True
                data["history"].insert(0, {"time": datetime.now().strftime("%H:%M %d/%m"), "text": f"{username} đã điểm danh nhận 200 xu."})
                save_data(data)
                msg = "Điểm danh thành công +200 Xu!"
            else:
                msg = "Hôm nay bạn đã điểm danh rồi!"
        elif action == 'open':
            if user_info["coins"] >= 75:
                user_info["coins"] -= 75
                reward = random.choice([
                    ("50 Likes Free Fire", 10),
                    ("100 Likes Free Fire", 5),
                    ("Acc Free Fire VIP", 1),
                    ("Trượt mất rồi (Chúc may mắn lần sau)", 50)
                ])
                data["history"].insert(0, {"time": datetime.now().strftime("%H:%M %d/%m"), "text": f"{username} đã mở túi mù và trúng: {reward[0]}"})
                save_data(data)
                msg = f"🎉 Kết quả mở Túi Mù: {reward[0]}"
            else:
                msg = "❌ Bạn không đủ 75 xu để mở túi mù!"

    html_bag = """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Túi Mù Minigame - SHOP BUG NEW</title>
        <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
        <style>
            :root { --bg-color: #030712; --neon-pink: #f43f5e; --neon-cyan: #38bdf8; --neon-green: #22c55e; }
            * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Orbitron', sans-serif; }
            body { background-color: var(--bg-color); color: #f8fafc; min-height: 100vh; overflow-x: hidden; }
            body::before { content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle at 50% 50%, rgba(244,63,94,0.1) 0%, rgba(3,7,18,0.95) 70%); z-index: -1; pointer-events: none; }
            header { display: flex; justify-content: space-between; align-items: center; padding: 15px 20px; background: rgba(15, 23, 42, 0.95); border-bottom: 2px solid var(--neon-pink); box-shadow: 0 0 15px rgba(244, 63, 94, 0.3); }
            .logo { font-size: 1.2rem; font-weight: 900; color: var(--neon-pink); text-shadow: 0 0 10px var(--neon-pink); }
            .user-bar { display: flex; align-items: center; gap: 12px; font-size: 0.9rem; }
            .coin-badge { background: #1e293b; border: 1px solid var(--neon-green); padding: 5px 10px; border-radius: 20px; color: var(--neon-green); font-weight: 700; }
            .nav-btn { background: transparent; border: 1px solid var(--neon-pink); color: var(--neon-pink); padding: 6px 12px; border-radius: 6px; cursor: pointer; text-decoration: none; font-size: 0.8rem; transition: 0.3s; }
            .nav-btn:hover { background: var(--neon-pink); color: #fff; box-shadow: 0 0 10px var(--neon-pink); }
            .container { max-width: 800px; margin: 20px auto; padding: 0 15px; text-align: center; }
            .section-title { font-size: 1.5rem; color: var(--neon-pink); margin: 20px 0; text-shadow: 0 0 15px var(--neon-pink); text-transform: uppercase; }
            .msg-box { background: rgba(244, 63, 94, 0.15); border: 1px solid var(--neon-pink); color: #fecdd3; padding: 12px; border-radius: 8px; font-weight: 700; margin-bottom: 20px; box-shadow: 0 0 15px rgba(244,63,94,0.2); }
            /* Hộp quà đồ họa CSS 3D Thay thế hoàn toàn Emoji */
            .css-gift-box { width: 140px; height: 140px; margin: 30px auto; background: linear-gradient(135deg, #f43f5e, #881337); border: 2px solid var(--neon-cyan); border-radius: 16px; position: relative; box-shadow: 0 0 25px rgba(244, 63, 94, 0.6), inset 0 0 15px rgba(56, 189, 248, 0.5); display: flex; justify-content: center; align-items: center; cursor: pointer; animation: floatBox 3s ease-in-out infinite; transition: transform 0.3s ease; }
            .css-gift-box:hover { transform: scale(1.08) rotate(3deg); }
            .css-gift-box::before { content: ""; position: absolute; width: 20px; height: 100%; background: var(--neon-cyan); box-shadow: 0 0 10px var(--neon-cyan); }
            .css-gift-box::after { content: ""; position: absolute; width: 100%; height: 20px; background: var(--neon-cyan); box-shadow: 0 0 10px var(--neon-cyan); }
            .gift-label { position: relative; z-index: 2; font-weight: 900; color: #fff; font-size: 0.85rem; text-shadow: 0 0 5px #000; }
            @keyframes floatBox { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
            .action-buttons { display: flex; justify-content: center; gap: 15px; margin-bottom: 30px; flex-wrap: wrap; }
            .game-btn { background: linear-gradient(135deg, var(--neon-pink), #e11d48); color: #fff; border: none; padding: 12px 24px; font-weight: 900; border-radius: 8px; cursor: pointer; font-size: 0.9rem; box-shadow: 0 0 15px rgba(244, 63, 94, 0.4); transition: 0.3s; }
            .game-btn:hover { transform: translateY(-2px); box-shadow: 0 0 25px var(--neon-pink); }
            .claim-btn { background: linear-gradient(135deg, var(--neon-green), #15803d); color: #000; box-shadow: 0 0 15px rgba(34,197,94,0.4); }
            .claim-btn:hover { box-shadow: 0 0 25px var(--neon-green); color: #fff; }
            .history-pod { background: rgba(15, 23, 42, 0.85); border: 1px solid var(--neon-pink); border-radius: 12px; padding: 20px; text-align: left; box-shadow: 0 0 20px rgba(244,63,94,0.2); }
            .history-pod h3 { color: var(--neon-pink); margin-bottom: 12px; font-size: 1rem; text-align: center; }
            .history-list { list-style: none; max-height: 200px; overflow-y: auto; font-size: 0.8rem; }
            .history-item { padding: 8px 10px; border-bottom: 1px solid #1e293b; display: flex; justify-content: space-between; color: #cbd5e1; }
            .history-time { color: var(--neon-cyan); }
        </style>
    </head>
    <body>
        <header>
            <div class="logo">🎁 TÚI MÙ BUG NEW</div>
            <div class="user-bar">
                <span class="coin-badge">🪙 {{ user_info.coins }} Xu</span>
                <span>👤 {{ username }}</span>
                <a href="/" class="nav-btn">⚡ Về Trang Chủ</a>
                <a href="/logout" class="nav-btn" style="border-color:#ef4444; color:#ef4444;">Đăng Xuất</a>
            </div>
        </header>
        <div class="container">
            <div class="section-title">🔮 Săn Nhân Phẩm Túi Mù 🔮</div>
            {% if msg %}<div class="msg-box">{{ msg }}</div>{% endif %}
            <div class="css-gift-box" onclick="document.getElementById('open-form').submit();">
                <div class="gift-label">MỞ TÚI (75 XU)</div>
            </div>
            <div class="action-buttons">
                <form method="POST" style="display:inline;"><input type="hidden" name="action" value="claim"><button type="submit" class="game-btn claim-btn">🎁 Điểm Danh Nhận 200 Xu</button></form>
                <form id="open-form" method="POST" style="display:inline;"><input type="hidden" name="action" value="open"><button type="submit" class="game-btn">⚡ Mở Ngay (75 Xu)</button></form>
            </div>
            <div class="history-pod">
                <h3>📜 Lịch Sử Hoạt Động Chung</h3>
                <ul class="history-list">
                    {% for h in history %}
                    <li class="history-item"><span>{{ h.text }}</span><span class="history-time">{{ h.time }}</span></li>
                    {% endfor %}
                </ul>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_bag, username=username, user_info=user_info, history=data["history"], msg=msg)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('auth_page'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
