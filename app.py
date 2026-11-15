from datetime import datetime
import random
from flask import Flask, redirect, render_template_string, request, session, url_for

app = Flask(__name__)
app.secret_key = "bug_new_secret_key_secure"

users_db = {"BugNew": "bugnewff.01"}
user_coins = {"BugNew": 500}
global_history = [
    (
        "BugNew",
        f"[{datetime.now().strftime('%H:%M %d/%m')}] 🎁 Nhận 200 xu điểm danh",
    )
]
last_checkin = {}

# 1. GIAO DIỆN ĐĂNG NHẬP (Tông Xanh Dương Điện - Cyan Matrix)
LOGIN_STYLE = """
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #020617; color: #f3f4f6; overflow-x: hidden; }
header { padding: 35px 20px; text-align: center; background: linear-gradient(135deg, #0f172a, #1e3a8a, #0284c7); border-bottom: 3px solid #38bdf8; box-shadow: 0 10px 30px rgba(56, 189, 248, 0.3); }
header h1 { margin: 0; font-size: 30px; letter-spacing: 1px; color: #38bdf8; text-shadow: 0 0 20px rgba(56, 189, 248, 0.8); }
header p { margin: 8px 0 0 0; color: #7dd3fc; font-size: 13px; text-transform: uppercase; letter-spacing: 3px; font-weight: bold; }
.container { max-width: 480px; margin: auto; padding: 20px; position: relative; z-index: 10; }
.card { background: rgba(15, 23, 42, 0.95); border: 2px solid #0284c7; border-radius: 18px; padding: 26px; margin-bottom: 20px; box-shadow: 0 10px 40px rgba(2, 132, 199, 0.25); backdrop-filter: blur(12px); }
.card h2 { margin-top: 0; color: #38bdf8; font-size: 20px; text-align: center; text-transform: uppercase; letter-spacing: 1px; }
.form-group { margin-bottom: 16px; }
.form-group label { display: block; margin-bottom: 6px; color: #38bdf8; font-weight: 600; font-size: 14px; }
.password-wrapper { position: relative; }
.form-control { width: 100%; padding: 13px; padding-right: 45px; background: #020617; border: 1px solid #1e293b; border-radius: 10px; color: white; font-size: 15px; transition: all 0.3s ease; }
.form-control:focus { outline: none; border-color: #38bdf8; box-shadow: 0 0 15px rgba(56, 189, 248, 0.4); }
.toggle-password { position: absolute; right: 12px; top: 50%; transform: translateY(-50%); background: none; border: none; cursor: pointer; font-size: 16px; color: #38bdf8; }
.btn { display: block; width: 100%; padding: 14px; background: linear-gradient(135deg, #0284c7, #2563eb); color: white; border: none; border-radius: 10px; font-size: 16px; font-weight: bold; cursor: pointer; text-transform: uppercase; letter-spacing: 1px; box-shadow: 0 4px 20px rgba(37, 99, 235, 0.5); transition: transform 0.2s; }
.btn:active { transform: scale(0.98); }
.error-msg { background: rgba(153, 27, 27, 0.5); border: 1px solid #ef4444; color: #fca5a5; padding: 12px; border-radius: 10px; margin-bottom: 15px; text-align: center; font-weight: bold; font-size: 14px; }
.success-msg { background: rgba(6, 78, 59, 0.5); border: 1px solid #10b981; color: #6ee7b7; padding: 12px; border-radius: 10px; margin-bottom: 15px; text-align: center; font-weight: bold; font-size: 14px; }
.switch-link { text-align: center; margin-top: 15px; font-size: 14px; color: #94a3b8; }
.switch-link a { color: #38bdf8; text-decoration: none; font-weight: bold; }
#matrix-canvas { position: fixed; inset: 0; pointer-events: none; z-index: 1; opacity: 0.18; }
</style>
<script>
window.addEventListener('DOMContentLoaded', () => {
    const canvas = document.createElement('canvas'); canvas.id = 'matrix-canvas'; document.body.prepend(canvas);
    const ctx = canvas.getContext('2d'); let w = canvas.width = window.innerWidth, h = canvas.height = window.innerHeight;
    const letters = '01BUGNEW⚡'; const size = 14; const cols = w / size; const drops = Array.from({length: cols}, () => 1);
    setInterval(() => {
        ctx.fillStyle = 'rgba(2, 6, 23, 0.08)'; ctx.fillRect(0, 0, w, h);
        ctx.fillStyle = '#38bdf8'; ctx.font = size + 'px monospace';
        drops.forEach((y, i) => { ctx.fillText(letters.charAt(Math.floor(Math.random()*letters.length)), i*size, y*size); if(y*size > h && Math.random() > 0.975) drops[i]=0; drops[i]++; });
    }, 30);
});
function togglePassword(id, btn) {
    const input = document.getElementById(id);
    input.type = input.type === "password" ? "text" : "password";
    btn.textContent = input.type === "password" ? "👁️" : "👁️‍🗨️";
}
</script>
"""

# 2. GIAO DIỆN ĐĂNG KÝ (Tông Tím Huyền Bí)
REGISTER_STYLE = """
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0f0728; color: #f3f4f6; overflow-x: hidden; }
header { padding: 35px 20px; text-align: center; background: linear-gradient(135deg, #3b0764, #7e22ce, #c026d3); border-bottom: 3px solid #e879f9; box-shadow: 0 10px 30px rgba(232, 121, 249, 0.3); }
header h1 { margin: 0; font-size: 30px; letter-spacing: 1px; color: #f0abfc; text-shadow: 0 0 20px rgba(240, 171, 252, 0.8); }
header p { margin: 8px 0 0 0; color: #f5d0fe; font-size: 13px; text-transform: uppercase; letter-spacing: 3px; font-weight: bold; }
.container { max-width: 480px; margin: auto; padding: 20px; position: relative; z-index: 10; }
.card { background: rgba(24, 15, 48, 0.95); border: 2px solid #a855f7; border-radius: 18px; padding: 26px; margin-bottom: 20px; box-shadow: 0 10px 40px rgba(168, 85, 247, 0.25); backdrop-filter: blur(12px); }
.card h2 { margin-top: 0; color: #e879f9; font-size: 20px; text-align: center; text-transform: uppercase; letter-spacing: 1px; }
.form-group { margin-bottom: 16px; }
.form-group label { display: block; margin-bottom: 6px; color: #e879f9; font-weight: 600; font-size: 14px; }
.password-wrapper { position: relative; }
.form-control { width: 100%; padding: 13px; padding-right: 45px; background: #0f0728; border: 1px solid #4c1d95; border-radius: 10px; color: white; font-size: 15px; transition: all 0.3s ease; }
.form-control:focus { outline: none; border-color: #e879f9; box-shadow: 0 0 15px rgba(232, 121, 249, 0.4); }
.toggle-password { position: absolute; right: 12px; top: 50%; transform: translateY(-50%); background: none; border: none; cursor: pointer; font-size: 16px; color: #e879f9; }
.btn { display: block; width: 100%; padding: 14px; background: linear-gradient(135deg, #9333ea, #c026d3); color: white; border: none; border-radius: 10px; font-size: 16px; font-weight: bold; cursor: pointer; text-transform: uppercase; letter-spacing: 1px; box-shadow: 0 4px 20px rgba(192, 38, 211, 0.5); transition: transform 0.2s; }
.btn:active { transform: scale(0.98); }
.error-msg { background: rgba(153, 27, 27, 0.5); border: 1px solid #ef4444; color: #fca5a5; padding: 12px; border-radius: 10px; margin-bottom: 15px; text-align: center; font-weight: bold; font-size: 14px; }
.switch-link { text-align: center; margin-top: 15px; font-size: 14px; color: #cbd5e1; }
.switch-link a { color: #e879f9; text-decoration: none; font-weight: bold; }
#violet-canvas { position: fixed; inset: 0; pointer-events: none; z-index: 1; opacity: 0.18; }
</style>
<script>
window.addEventListener('DOMContentLoaded', () => {
    const canvas = document.createElement('canvas'); canvas.id = 'violet-canvas'; document.body.prepend(canvas);
    const ctx = canvas.getContext('2d'); let w = canvas.width = window.innerWidth, h = canvas.height = window.innerHeight;
    const letters = '✨💜BUGNEW'; const size = 14; const cols = w / size; const drops = Array.from({length: cols}, () => 1);
    setInterval(() => {
        ctx.fillStyle = 'rgba(15, 7, 40, 0.08)'; ctx.fillRect(0, 0, w, h);
        ctx.fillStyle = '#e879f9'; ctx.font = size + 'px monospace';
        drops.forEach((y, i) => { ctx.fillText(letters.charAt(Math.floor(Math.random()*letters.length)), i*size, y*size); if(y*size > h && Math.random() > 0.975) drops[i]=0; drops[i]++; });
    }, 30);
});
function togglePassword(id, btn) {
    const input = document.getElementById(id);
    input.type = input.type === "password" ? "text" : "password";
    btn.textContent = input.type === "password" ? "👁️" : "👁️‍🗨️";
}
</script>
"""

@app.route("/login", methods=["GET", "POST"])
def login():
    error, success = None, request.args.get("success")
    if request.method == "POST":
        u, p = request.form.get("username", "").strip(), request.form.get("password", "").strip()
        if u in users_db and users_db[u] == p:
            session["user"] = u
            if u not in user_coins: user_coins[u] = 0
            return redirect(url_for("home"))
        error = "Tài khoản hoặc mật khẩu không chính xác!"
    return render_template_string("""
    <!DOCTYPE html><html lang="vi"><head><title>ĐĂNG NHẬP - SHOP BUG NEW</title>{{ style | safe }}</head>
    <body>
    <header><h1>🛍️ SHOP BUG NEW</h1><p>CỔNG ĐĂNG NHẬP HỆ THỐNG</p></header>
    <div class="container" style="margin-top: 40px;">
        <div class="card">
            <h2>🔑 ĐĂNG NHẬP</h2>
            {% if success %}<div class="success-msg">{{ success }}</div>{% endif %}
            {% if error %}<div class="error-msg">{{ error }}</div>{% endif %}
            <form method="POST">
                <div class="form-group"><label>Tài khoản:</label><input type="text" name="username" class="form-control" placeholder="Nhập tên tài khoản..." required></div>
                <div class="form-group"><label>Mật khẩu:</label>
                    <div class="password-wrapper">
                        <input type="password" name="password" id="p1" class="form-control" placeholder="Nhập mật khẩu..." required>
                        <button type="button" class="toggle-password" onclick="togglePassword('p1', this)">👁️</button>
                    </div>
                </div>
                <button type="submit" class="btn">🚀 ĐĂNG NHẬP NGAY</button>
            </form>
            <div class="switch-link">Chưa có tài khoản? <a href="/register">Đăng ký ngay</a></div>
        </div>
    </div></body></html>""", style=LOGIN_STYLE, success=success, error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        u, p = request.form.get("username", "").strip(), request.form.get("password", "").strip()
        if not u.isalpha(): error = "Tài khoản chỉ được chứa chữ cái, không số/ký tự đặc biệt!"
        elif u in users_db: error = "Tài khoản đã tồn tại!"
        elif len(p) < 6: error = "Mật khẩu phải từ 6 ký tự trở lên!"
        else:
            users_db[u], user_coins[u] = p, 0
            return redirect(url_for("login", success="Đăng ký thành công! Hãy đăng nhập."))
    return render_template_string("""
    <!DOCTYPE html><html lang="vi"><head><title>ĐĂNG KÝ - SHOP BUG NEW</title>{{ style | safe }}</head>
    <body>
    <header><h1>🛍️ SHOP BUG NEW</h1><p>TẠO TÀI KHOẢN MỚI</p></header>
    <div class="container" style="margin-top: 30px;">
        <div class="card">
            <h2>➕ ĐĂNG KÝ</h2>
            {% if error %}<div class="error-msg">{{ error }}</div>{% endif %}
            <form method="POST">
                <div class="form-group"><label>Tài khoản (Chỉ chữ cái):</label><input type="text" name="username" class="form-control" placeholder="Ví dụ: BugNew" required></div>
                <div class="form-group"><label>Mật khẩu:</label>
                    <div class="password-wrapper">
                        <input type="password" name="password" id="p2" class="form-control" placeholder="Ít nhất 6 ký tự..." required>
                        <button type="button" class="toggle-password" onclick="togglePassword('p2', this)">👁️</button>
                    </div>
                </div>
                <button type="submit" class="btn">✨ TẠO TÀI KHOẢN</button>
            </form>
            <div class="switch-link">Đã có tài khoản? <a href="/login">Đăng nhập ngay</a></div>
        </div>
    </div></body></html>""", style=REGISTER_STYLE, error=error)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
    # 3. GIAO DIỆN TRANG CHỦ & KHO ACC
HOME_STYLE = """
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #030712; color: #f3f4f6; scroll-behavior: smooth; overflow-x: hidden; }
header { padding: 30px 15px; text-align: center; background: linear-gradient(135deg, #022c22, #047857, #0284c7); position: relative; z-index: 10; border-bottom: 3px solid #34d399; box-shadow: 0 10px 30px rgba(52, 211, 153, 0.3); }
header h1 { margin: 0; font-size: 27px; color: #34d399; text-shadow: 0 0 20px rgba(52, 211, 153, 0.7); }
header p { margin: 6px 0 0 0; color: #a7f3d0; font-size: 13px; letter-spacing: 1px; font-weight: bold; }
.user-badge { position: absolute; top: 12px; right: 15px; background: rgba(2, 44, 34, 0.9); border: 1px solid #34d399; padding: 6px 12px; border-radius: 20px; font-size: 12px; backdrop-filter: blur(5px); }
.user-badge a { color: #f87171; text-decoration: none; margin-left: 6px; font-weight: bold; }
.blind-bag-btn-top { position: absolute; top: 12px; left: 15px; background: linear-gradient(135deg, #e11d48, #be185d); border: 1px solid #fb7185; padding: 6px 12px; border-radius: 20px; font-size: 12px; color: white; text-decoration: none; font-weight: bold; box-shadow: 0 0 15px rgba(225, 29, 72, 0.6); }
.container { max-width: 650px; margin: auto; padding: 15px; position: relative; z-index: 10; }
.card { background: rgba(6, 78, 59, 0.25); border: 2px solid #059669; border-radius: 16px; padding: 20px; margin-bottom: 18px; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5); backdrop-filter: blur(10px); }
.card h2 { margin-top: 0; color: #34d399; font-size: 18px; border-bottom: 1px solid #065f46; padding-bottom: 10px; text-transform: uppercase; letter-spacing: 1px; }
.price { display: flex; justify-content: space-between; align-items: center; padding: 12px 15px; margin: 10px 0; background: #020617; border-radius: 10px; border: 1px solid #064e3b; transition: all 0.2s; }
.price:hover { border-color: #34d399; box-shadow: 0 0 12px rgba(52, 211, 153, 0.3); }
.money { color: #4ade80; font-weight: bold; font-size: 15px; text-shadow: 0 0 8px rgba(74, 222, 128, 0.4); }
.nav-acc-btn { display: block; text-align: center; background: linear-gradient(135deg, #059669, #0284c7); color: white; padding: 16px; border-radius: 14px; font-size: 16px; font-weight: bold; text-decoration: none; margin-bottom: 22px; box-shadow: 0 6px 20px rgba(5, 150, 105, 0.5); text-transform: uppercase; letter-spacing: 1px; }
.acc-item { background: #020617; border-radius: 12px; padding: 15px; margin-bottom: 18px; border: 2px solid #047857; transition: transform 0.2s; }
.acc-item:hover { transform: translateY(-2px); border-color: #34d399; box-shadow: 0 0 15px rgba(52, 211, 153, 0.25); }
.acc-item img { width: 100%; border-radius: 10px; margin-bottom: 10px; border: 1px solid #065f46; }
.button { display: block; text-align: center; margin-top: 12px; padding: 12px; background: linear-gradient(135deg, #16a34a, #22c55e); color: #052e16; text-decoration: none; border-radius: 10px; font-weight: bold; box-shadow: 0 4px 15px rgba(34, 197, 94, 0.4); text-transform: uppercase; font-size: 14px; }
.contact { text-align: center; padding: 25px 20px; background: linear-gradient(135deg, #064e3b, #0369a1); border-radius: 16px; border: 2px solid #34d399; box-shadow: 0 8px 25px rgba(3, 105, 161, 0.4); }
footer { text-align: center; padding: 25px; color: #64748b; font-size: 13px; letter-spacing: 1px; }
#green-canvas { position: fixed; inset: 0; pointer-events: none; z-index: 1; opacity: 0.15; }
</style>
<script>
window.addEventListener('DOMContentLoaded', () => {
    const canvas = document.createElement('canvas'); canvas.id = 'green-canvas'; document.body.prepend(canvas);
    const ctx = canvas.getContext('2d'); let w = canvas.width = window.innerWidth, h = canvas.height = window.innerHeight;
    const symbols = '🔥👍💎BUGNEW'; const size = 16; const cols = w / size; const drops = Array.from({length: cols}, () => Math.floor(Math.random() * h));
    setInterval(() => {
        ctx.fillStyle = 'rgba(3, 7, 18, 0.1)'; ctx.fillRect(0, 0, w, h);
        ctx.fillStyle = '#34d399'; ctx.font = size + 'px monospace';
        drops.forEach((y, i) => { ctx.fillText(symbols.charAt(Math.floor(Math.random()*symbols.length)), i*size, y*size); if(y*size > h && Math.random() > 0.95) drops[i]=0; drops[i]++; });
    }, 30);
});
</script>
"""

@app.route("/")
def home():
    if "user" not in session: return redirect(url_for("login"))
    u = session["user"]
    return render_template_string("""
    <!DOCTYPE html><html lang="vi"><head><title>SHOP LIKES & KHO ACC FF - BUG NEW</title>{{ style | safe }}</head>
    <body>
    <header>
        <a href="/blind-bag" class="blind-bag-btn-top">🎁 Túi Mù</a>
        <div class="user-badge">👤 <b>{{ u }}</b> | <a href="/logout">Đăng xuất</a></div>
        <h1>🛍️ SHOP BUG NEW</h1><p>🎮 DỊCH VỤ LIKES & KHO 10 ACC FREE FIRE</p>
    </header>
    <div class="container" style="margin-top: 15px;">
        <div class="card" style="text-align:center;">
            <h2>🔥 BẢNG GIÁ BUFF LIKES</h2>
            <p style="color:#a7f3d0; font-size:13px; margin:5px 0 0 0;">Mỗi ngày tối đa 220 likes / ngày!</p>
        </div>
        <div class="card">
            <h2>🏦 GIÁ CHUYỂN KHOẢN</h2>
            <div class="price"><span>👍 220 Likes</span><span class="money">2.000đ</span></div>
            <div class="price"><span>👍 1.100 Likes</span><span class="money">5.000đ</span></div>
            <div class="price"><span>👍 3.300 Likes</span><span class="money">10.000đ</span></div>
            <div class="price"><span>👍 8.800 Likes</span><span class="money">20.000đ</span></div>
        </div>
        <div class="card">
            <h2>💳 GIÁ THẺ ĐIỆN THOẠI (CARD)</h2>
            <div class="price"><span>👍 4.400 Likes</span><span class="money">20.000đ</span></div>
            <div class="price"><span>👍 11.000 Likes</span><span class="money">50.000đ</span></div>
        </div>
        <div class="card">
            <h2>🎮 GIÁ ĐỒ TRONG GAME</h2>
            <div class="price"><span>👍 2.200 Likes</span><span class="money">💎 &lt; 100</span></div>
            <div class="price"><span>👍 5.500 Likes</span><span class="money">💎 &lt; 200</span></div>
            <div class="price"><span>👍 11.000 Likes</span><span class="money">💎 &lt; 300</span></div>
        </div>
        <div class="card">
            <h2>💎 GIÁ NẠP KIM CƯƠNG</h2>
            <div class="price"><span>👍 1.100 Likes</span><span class="money">💎 25</span></div>
            <div class="price"><span>👍 2.200 Likes</span><span class="money">💎 51</span></div>
            <div class="price"><span>👍 5.500 Likes</span><span class="money">💎 113</span></div>
            <div class="price"><span>👍 12.100 Likes</span><span class="money">💎 283</span></div>
        </div>

        <a href="#kho-acc" class="nav-acc-btn">📦 XEM KHO ACC FREE FIRE (10 ACC)</a>
        
        <div class="card" id="kho-acc">
            <h2 style="text-align:center;">🔥 KHO ACC FREE FIRE (10 ACC) 🔥</h2>
            
            <div class="acc-item">
                <img src="https://i.postimg.cc/rwBsvfSm/Screenshot-20261102-174419-com-dts-freefireth.jpg" alt="Acc 1">
                <h3 style="color:#34d399; margin:5px 0; font-size:16px;">🎮 Acc #1</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 34<br>🔐 <b>Login:</b> Facebook<br>💰 <b>Giá:</b> <strong style="color:#4ade80;">35.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            <div class="acc-item">
                <img src="https://i.postimg.cc/3R7RwWS6/Screenshot-20261102-174720-com-dts-freefireth.jpg" alt="Acc 2">
                <h3 style="color:#34d399; margin:5px 0; font-size:16px;">🎮 Acc #2</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 21<br>🔐 <b>Login:</b> Facebook<br>💰 <b>Giá:</b> <strong style="color:#4ade80;">20.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            <div class="acc-item">
                <img src="https://i.postimg.cc/3NxxgVHC/Screenshot-20261031-191554-com-dts-freefireth.jpg" alt="Acc 3">
                <h3 style="color:#34d399; margin:5px 0; font-size:16px;">🎮 Acc #3</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 18<br>🔐 <b>Login:</b> Facebook<br>💰 <b>Giá:</b> <strong style="color:#4ade80;">15.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            <div class="acc-item">
                <img src="https://i.postimg.cc/rwfKhsvC/Screenshot-20261031-191554-com-dts-freefireth.jpg" alt="Acc 4">
                <h3 style="color:#34d399; margin:5px 0; font-size:16px;">🎮 Acc #4</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 26<br>🔐 <b>Login:</b> Google<br>💰 <b>Giá:</b> <strong style="color:#4ade80;">15.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            <div class="acc-item">
                <img src="https://i.postimg.cc/28cDMWSj/Screenshot-20261031-191815-com-dts-freefireth.jpg" alt="Acc 5">
                <h3 style="color:#34d399; margin:5px 0; font-size:16px;">🎮 Acc #5</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 9<br>🔐 <b>Login:</b> Google<br>💰 <b>Giá:</b> <strong style="color:#4ade80;">36.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            <div class="acc-item">
                <img src="https://i.postimg.cc/XqjRDNM8/Screenshot-20261031-191924-com-dts-freefireth.jpg" alt="Acc 6">
                <h3 style="color:#34d399; margin:5px 0; font-size:16px;">🎮 Acc #6</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 13<br>🔐 <b>Login:</b> Google<br>💰 <b>Giá:</b> <strong style="color:#4ade80;">5.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            <div class="acc-item">
                <img src="https://i.postimg.cc/ncwy0t3T/Screenshot-20261031-192021-com-dts-freefireth.jpg" alt="Acc 7">
                <h3 style="color:#34d399; margin:5px 0; font-size:16px;">🎮 Acc #7</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 22<br>🔐 <b>Login:</b> Google<br>💰 <b>Giá:</b> <strong style="color:#4ade80;">20.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            <div class="acc-item">
                <img src="https://i.postimg.cc/3w2z80YD/Screenshot-20261031-192143-com-dts-freefireth.jpg" alt="Acc 8">
                <h3 style="color:#34d399; margin:5px 0; font-size:16px;">🎮 Acc #8</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 2<br>🔐 <b>Login:</b> Google<br>💰 <b>Giá:</b> <strong style="color:#4ade80;">25.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            <div class="acc-item">
                <img src="https://i.postimg.cc/J4tgy2RD/Screenshot-20261031-192412-com-dts-freefireth.jpg" alt="Acc 9">
                <h3 style="color:#34d399; margin:5px 0; font-size:16px;">🎮 Acc #9</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 28<br>🔐 <b>Login:</b> Facebook<br>💰 <b>Giá:</b> <strong style="color:#4ade80;">30.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            <div class="acc-item">
                <img src="https://i.postimg.cc/JhCd27ZP/Screenshot-20261031-192920-com-dts-freefireth.jpg" alt="Acc 10">
                <h3 style="color:#34d399; margin:5px 0; font-size:16px;">🎮 Acc #10</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 14<br>🔐 <b>Login:</b> Facebook<br>💰 <b>Giá:</b> <strong style="color:#4ade80;">10.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
        </div>

        <div class="contact">
            <h2>📩 MUA LIKES IB NHA!</h2>
            <p style="margin:8px 0 15px 0;">Facebook chính chủ: <b>Bug New</b></p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank" style="margin:0 auto; max-width:250px;">💬 LIÊN HỆ FACEBOOK</a>
        </div>
    </div>
    <footer>⚡ © 2026 BUG NEW ⚡</footer>
    </body></html>""", style=HOME_STYLE, u=u)
    # 4. GIAO DIỆN TÚI MÙ
BLIND_STYLE = """
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #1a050f; color: #f3f4f6; scroll-behavior: smooth; overflow-x: hidden; }
header { padding: 30px 15px; text-align: center; background: linear-gradient(135deg, #4c0519, #be123c, #e11d48); position: relative; z-index: 10; border-bottom: 3px solid #fb7185; box-shadow: 0 10px 30px rgba(251, 113, 133, 0.4); }
header h1 { margin: 0; font-size: 27px; color: #ffe4e6; text-shadow: 0 0 20px rgba(255, 228, 230, 0.8); }
header p { margin: 6px 0 0 0; color: #fecdd3; font-size: 13px; letter-spacing: 1px; font-weight: bold; }
.back-btn { position: absolute; top: 12px; left: 15px; background: rgba(76, 5, 25, 0.9); border: 1px solid #fb7185; padding: 6px 12px; border-radius: 20px; font-size: 12px; color: #fb7185; text-decoration: none; font-weight: bold; }
.user-badge { position: absolute; top: 12px; right: 15px; background: rgba(76, 5, 25, 0.9); border: 1px solid #fb7185; padding: 6px 12px; border-radius: 20px; font-size: 12px; backdrop-filter: blur(5px); color: #fecdd3; }
.container { max-width: 650px; margin: auto; padding: 15px; position: relative; z-index: 10; }
.coin-box { background: linear-gradient(135deg, #78350f, #d97706); border: 2px solid #facc15; padding: 15px; border-radius: 14px; text-align: center; font-size: 17px; font-weight: bold; color: #fef08a; margin-bottom: 18px; box-shadow: 0 6px 20px rgba(217, 119, 6, 0.4); }
.card { background: rgba(136, 19, 55, 0.2); border: 2px solid #e11d48; border-radius: 16px; padding: 20px; margin-bottom: 18px; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5); backdrop-filter: blur(10px); }
.card h2 { margin-top: 0; color: #fb7185; font-size: 18px; border-bottom: 1px solid #881337; padding-bottom: 10px; text-transform: uppercase; letter-spacing: 1px; }
.btn-action { display: block; width: 100%; padding: 14px; background: linear-gradient(135deg, #059669, #10b981); color: white; border: none; border-radius: 12px; font-size: 15px; font-weight: bold; cursor: pointer; text-decoration: none; margin-top: 10px; box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4); text-transform: uppercase; }
.bags-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; margin: 15px 0; }
.bag-item { background: #020617; border: 2px dashed #fb7185; border-radius: 14px; padding: 22px 10px; text-align: center; cursor: pointer; width: 100%; transition: all 0.2s; }
.bag-item:hover { background: #380414; border-color: #f43f5e; transform: scale(1.02); box-shadow: 0 0 20px rgba(244, 63, 94, 0.4); }
.history-box { background: #020617; border: 1px solid #881337; border-radius: 10px; padding: 12px; max-height: 240px; overflow-y: auto; font-size: 13px; color: #cbd5e1; }
.history-item { padding: 8px 0; border-bottom: 1px solid #4c0519; }
.opening-modal { display: none; position: fixed; inset: 0; background: rgba(26, 5, 15, 0.92); backdrop-filter: blur(8px); z-index: 100; justify-content: center; align-items: center; flex-direction: column; text-align: center; padding: 25px; }
@keyframes shake { 0% { transform: translate(1px, 1px) rotate(0deg); } 20% { transform: translate(-3px, 0px) rotate(-5deg); } 40% { transform: translate(3px, 2px) rotate(5deg); } 60% { transform: translate(-1px, -1px) rotate(0deg); } 100% { transform: translate(0, 0) rotate(0deg); } }
.shaking { animation: shake 0.4s infinite; }
.button { display: block; text-align: center; margin-top: 12px; padding: 12px; background: linear-gradient(135deg, #e11d48, #f43f5e); color: white; text-decoration: none; border-radius: 10px; font-weight: bold; box-shadow: 0 4px 15px rgba(225, 29, 72, 0.5); text-transform: uppercase; font-size: 14px; }
footer { text-align: center; padding: 25px; color: #64748b; font-size: 13px; letter-spacing: 1px; }
#pink-canvas { position: fixed; inset: 0; pointer-events: none; z-index: 1; opacity: 0.15; }
</style>
<script>
window.addEventListener('DOMContentLoaded', () => {
    const canvas = document.createElement('canvas'); canvas.id = 'pink-canvas'; document.body.prepend(canvas);
    const ctx = canvas.getContext('2d'); let w = canvas.width = window.innerWidth, h = canvas.height = window.innerHeight;
    const symbols = '🎁📦🪙BUGNEW'; const size = 16; const cols = w / size; const drops = Array.from({length: cols}, () => Math.floor(Math.random() * h));
    setInterval(() => {
        ctx.fillStyle = 'rgba(26, 5, 15, 0.1)'; ctx.fillRect(0, 0, w, h);
        ctx.fillStyle = '#fb7185'; ctx.font = size + 'px monospace';
        drops.forEach((y, i) => { ctx.fillText(symbols.charAt(Math.floor(Math.random()*symbols.length)), i*size, y*size); if(y*size > h && Math.random() > 0.95) drops[i]=0; drops[i]++; });
    }, 30);
});

function openBagAnimation(bagNum) {
    const modal = document.getElementById('openingModal');
    const boxImg = document.getElementById('boxImg');
    const rewardText = document.getElementById('rewardText');
    const actionBtn = document.getElementById('actionBtn');
    
    modal.style.display = 'flex';
    boxImg.classList.add('shaking');
    rewardText.textContent = "🎁 Đang mở túi mù #" + bagNum + "...";
    actionBtn.style.display = "none";
    
    setTimeout(() => {
        boxImg.classList.remove('shaking');
        fetch('/open-bag-api', {
            method: 'POST',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}
        })
        .then(res => res.json())
        .then(data => {
            if(data.status === 'success') {
                rewardText.innerHTML = "🎉 Trúng thưởng: <b style='color:#facc15'>" + data.reward + "</b>";
            } else {
                rewardText.innerHTML = "<b style='color:#f87171'>" + data.msg + "</b>";
            }
            actionBtn.style.display = "block";
        });
    }, 1500);
}
</script>
"""

@app.route("/blind-bag", methods=["GET", "POST"])
def blind_bag():
    if "user" not in session: return redirect(url_for("login"))
    u = session["user"]
    msg, msg_type = None, None
    if u not in user_coins: user_coins[u] = 0
    today = datetime.now().strftime("%Y-%m-%d")

    if request.method == "POST" and request.form.get("action") == "checkin":
        if last_checkin.get(u) == today:
            msg, msg_type = "❌ Bạn đã điểm danh hôm nay rồi!", "error"
        else:
            last_checkin[u] = today
            user_coins[u] += 200
            global_history.insert(0, (u, f"[{datetime.now().strftime('%H:%M %d/%m')}] 🎁 Nhận 200 xu điểm danh"))
            msg, msg_type = "🎉 Nhận thành công +200 xu!", "success"

    return render_template_string("""
    <!DOCTYPE html><html lang="vi"><head><title>TÚI MÙ LIKES - BUG NEW</title>{{ style | safe }}</head>
    <body>
    <header>
        <a href="/" class="back-btn">🏠 Trang Chủ</a>
        <div class="user-badge">👤 <b>{{ u }}</b></div>
        <h1>🎁 TÚI MÙ LIKES FF</h1><p>SĂN NHÂN PHẨM MỖI NGÀY</p>
    </header>
    <div class="container" style="margin-top: 15px;">
        <div class="coin-box">💰 Tài khoản: <b>{{ u }}</b> | 🪙 Xu hiện có: <span style="color:#fef08a;">{{ coins }}</span> xu</div>
        {% if msg %}
            <div class="card" style="border-color:{{ '#10b981' if msg_type=='success' else '#ef4444' }}; text-align:center;">
                <h3 style="margin:0; color:{{ '#6ee7b7' if msg_type=='success' else '#fca5a5' }};">{{ msg }}</h3>
            </div>
        {% endif %}
        <div class="card">
            <h2>📅 ĐIỂM DANH HẰNG NGÀY</h2>
            <form method="POST"><input type="hidden" name="action" value="checkin">
                <button type="submit" class="btn-action">🎁 NHẬN 200 XU</button>
            </form>
        </div>
        <div class="card">
            <h2>🛍️ CHỌN 1 TRONG 4 TÚI MÙ (75 XU)</h2>
            <div class="bags-grid">
                <button type="button" class="bag-item" onclick="openBagAnimation(1)"><span style="font-size:32px;">📦</span><h3 style="margin:8px 0 4px 0; color:#fb7185; font-size:15px;">Túi #1</h3><span style="font-size:12px; color:#cbd5e1;">Phí: 75 xu</span></button>
                <button type="button" class="bag-item" onclick="openBagAnimation(2)"><span style="font-size:32px;">📦</span><h3 style="margin:8px 0 4px 0; color:#fb7185; font-size:15px;">Túi #2</h3><span style="font-size:12px; color:#cbd5e1;">Phí: 75 xu</span></button>
                <button type="button" class="bag-item" onclick="openBagAnimation(3)"><span style="font-size:32px;">📦</span><h3 style="margin:8px 0 4px 0; color:#fb7185; font-size:15px;">Túi #3</h3><span style="font-size:12px; color:#cbd5e1;">Phí: 75 xu</span></button>
                <button type="button" class="bag-item" onclick="openBagAnimation(4)"><span style="font-size:32px;">📦</span><h3 style="margin:8px 0 4px 0; color:#fb7185; font-size:15px;">Túi #4</h3><span style="font-size:12px; color:#cbd5e1;">Phí: 75 xu</span></button>
            </div>
        </div>
        <div class="card">
            <h2>📜 LỊCH SỬ HOẠT ĐỘNG CHUNG</h2>
            <div class="history-box">
                {% if history %}{% for user_name, item in history %}<div class="history-item"><b>[{{ user_name }}]</b> {{ item }}</div>{% endfor %}
                {% else %}<div style="text-align:center; color:#64748b; padding:10px;">Chưa có lịch sử.</div>{% endif %}
            </div>
        </div>
    </div>

    <div id="openingModal" class="opening-modal">
        <div id="boxImg" style="font-size:80px; margin-bottom:15px;">📦</div>
        <h2 id="rewardText" style="color:#fb7185; margin-bottom:20px; font-size:20px;">Đang mở túi mù...</h2>
        <div id="actionBtn" style="display:none; width:100%; max-width:320px;">
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank" style="margin-bottom:12px;">💬 GỬI ẢNH CHO ADMIN QUA FACEBOOK</a>
            <button onclick="location.reload()" style="background:#334155; color:white; border:none; padding:12px; width:100%; border-radius:10px; cursor:pointer; font-weight:bold; text-transform:uppercase;">TIẾP TỤC CHƠI</button>
        </div>
    </div>

    <footer>⚡ © 2026 BUG NEW ⚡</footer>
    </body></html>""", style=BLIND_STYLE, u=u, coins=user_coins[u], history=global_history, msg=msg, msg_type=msg_type)

@app.route("/open-bag-api", methods=["POST"])
def open_bag_api():
    if "user" not in session: return {"status": "error", "msg": "Chưa đăng nhập!"}
    u = session["user"]
    if user_coins.get(u, 0) < 75:
        return {"status": "error", "msg": f"Không đủ xu! Cần 75 xu (Bạn đang có {user_coins.get(u, 0)} xu)."}
    
    user_coins[u] -= 75
    rewards = ["💔 Chúc bạn may mắn lần sau", "❤️ 20 like", "❤️ 50 like", "❤️ 100 like", "❤️ 150 like", "❤️ 200 like", "❤️ 220 like", "🔥 1100 like"]
    weights = [25, 24, 17, 13, 9, 6, 4, 2]
    won = random.choices(rewards, weights=weights, k=1)[0]
    
    global_history.insert(0, (u, f"[{datetime.now().strftime('%H:%M %d/%m')}] 🛍️ Mở túi (-75 xu) - Trúng: {won}"))
    return {"status": "success", "reward": won}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
