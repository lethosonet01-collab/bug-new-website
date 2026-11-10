from datetime import datetime
from flask import Flask, redirect, render_template_string, request, session, url_for

app = Flask(__name__)
app.secret_key = "bug_new_secret_key_secure"

users_db = {"BugNew": "bugnewff.01"}
user_coins = {"BugNew": 500}
user_history = {
    "BugNew": [
        "🎁 [Điểm danh] Nhận 200 xu miễn phí",
        "🛍️ [Mở túi] Trúng: ❤️ 50 Likes",
    ]
}
last_checkin = {}

LOGIN_REGISTER_STYLE = """
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { box-sizing: border-box; }
body { margin: 0; font-family: Arial, sans-serif; background: #050814; color: white; overflow-x: hidden; }
header { padding: 25px 15px; text-align: center; background: linear-gradient(135deg, #1d4ed8, #0284c7); }
header h1 { margin: 0; font-size: 25px; text-shadow: 0 0 10px #38bdf8; }
.container { max-width: 650px; margin: auto; padding: 15px; position: relative; z-index: 10; }
.card { background: rgba(19, 29, 48, 0.9); border: 1px solid #38bdf8; border-radius: 14px; padding: 18px; margin-bottom: 15px; }
.card h2 { margin-top: 0; color: #38bdf8; font-size: 18px; text-align: center; }
.form-group { margin-bottom: 12px; }
.form-group label { display: block; margin-bottom: 4px; color: #38bdf8; font-weight: bold; }
.password-wrapper { position: relative; }
.form-control { width: 100%; padding: 11px; padding-right: 40px; background: #0b1326; border: 1px solid #1e3a8a; border-radius: 8px; color: white; font-size: 15px; }
.toggle-password { position: absolute; right: 10px; top: 50%; transform: translateY(-50%); background: none; border: none; cursor: pointer; font-size: 16px; color: #38bdf8; }
.btn { display: block; width: 100%; padding: 12px; background: linear-gradient(135deg, #0284c7, #2563eb); color: white; border: none; border-radius: 8px; font-size: 16px; font-weight: bold; cursor: pointer; }
.error-msg { background: #450a0a; border: 1px solid #ef4444; color: #fca5a5; padding: 10px; border-radius: 8px; margin-bottom: 12px; text-align: center; font-weight: bold; }
.success-msg { background: #064e3b; border: 1px solid #10b981; color: #6ee7b7; padding: 10px; border-radius: 8px; margin-bottom: 12px; text-align: center; font-weight: bold; }
.switch-link { text-align: center; margin-top: 12px; font-size: 13px; color: #94a3b8; }
.switch-link a { color: #38bdf8; text-decoration: none; font-weight: bold; }
#matrix-canvas { position: fixed; inset: 0; pointer-events: none; z-index: 1; opacity: 0.2; }
</style>
<script>
window.addEventListener('DOMContentLoaded', () => {
    const canvas = document.createElement('canvas'); canvas.id = 'matrix-canvas'; document.body.prepend(canvas);
    const ctx = canvas.getContext('2d'); let w = canvas.width = window.innerWidth, h = canvas.height = window.innerHeight;
    const letters = '01BUGNEW'; const size = 14; const cols = w / size; const drops = Array.from({length: cols}, () => 1);
    setInterval(() => {
        ctx.fillStyle = 'rgba(5, 8, 20, 0.05)'; ctx.fillRect(0, 0, w, h);
        ctx.fillStyle = '#38bdf8'; ctx.font = size + 'px monospace';
        drops.forEach((y, i) => { ctx.fillText(letters.charAt(Math.floor(Math.random()*letters.length)), i*size, y*size); if(y*size > h && Math.random() > 0.975) drops[i]=0; drops[i]++; });
    }, 33);
});
function togglePassword(id, btn) {
    const input = document.getElementById(id);
    input.type = input.type === "password" ? "text" : "password";
    btn.textContent = input.type === "password" ? "👁️" : "👁️‍🗨️";
}
</script>
"""

HOME_STYLE = """
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { box-sizing: border-box; }
body { margin: 0; font-family: Arial, sans-serif; background: #050814; color: white; scroll-behavior: smooth; overflow-x: hidden; }
header { padding: 25px 15px; text-align: center; background: linear-gradient(135deg, #1d4ed8, #0284c7); position: relative; z-index: 10; }
header h1 { margin: 0; font-size: 25px; text-shadow: 0 0 10px #fff; }
.user-badge { position: absolute; top: 10px; right: 15px; background: rgba(0,0,0,0.4); padding: 5px 10px; border-radius: 15px; font-size: 12px; border: 1px solid rgba(56,189,248,0.4); }
.user-badge a { color: #f87171; text-decoration: none; margin-left: 5px; font-weight: bold; }
.blind-bag-btn-top { position: absolute; top: 10px; left: 15px; background: rgba(220,38,38,0.8); padding: 5px 10px; border-radius: 15px; font-size: 12px; border: 1px solid #f87171; color: white; text-decoration: none; font-weight: bold; }
.container { max-width: 650px; margin: auto; padding: 15px; position: relative; z-index: 10; }
.card { background: rgba(19, 29, 48, 0.9); border: 1px solid #1e3a8a; border-radius: 14px; padding: 18px; margin-bottom: 15px; }
.card h2 { margin-top: 0; color: #38bdf8; font-size: 18px; }
.price { display: flex; justify-content: space-between; padding: 12px; margin: 8px 0; background: #0b1326; border-radius: 8px; border: 1px solid #172554; }
.money { color: #4ade80; font-weight: bold; }
.nav-acc-btn { display: block; text-align: center; background: linear-gradient(135deg, #0284c7, #2563eb); color: white; padding: 14px; border-radius: 12px; font-size: 16px; font-weight: bold; text-decoration: none; margin-bottom: 20px; }
.acc-item { background: #0b1326; border-radius: 10px; padding: 12px; margin-bottom: 15px; border: 1px solid #1e3a8a; }
.button { display: block; text-align: center; margin-top: 10px; padding: 10px; background: #22c55e; color: #052e16; text-decoration: none; border-radius: 8px; font-weight: bold; }
.contact { text-align: center; padding: 20px; background: linear-gradient(135deg, #082f49, #0369a1); border-radius: 14px; border: 1px solid #38bdf8; }
footer { text-align: center; padding: 20px; color: #94a3b8; font-size: 12px; }
#cyber-stream-canvas { position: fixed; inset: 0; pointer-events: none; z-index: 1; opacity: 0.2; }
</style>
<script>
window.addEventListener('DOMContentLoaded', () => {
    const canvas = document.createElement('canvas'); canvas.id = 'cyber-stream-canvas'; document.body.prepend(canvas);
    const ctx = canvas.getContext('2d'); let w = canvas.width = window.innerWidth, h = canvas.height = window.innerHeight;
    const symbols = '⚡💎BUGNEW01'; const size = 16; const cols = w / size; const drops = Array.from({length: cols}, () => Math.floor(Math.random() * h));
    setInterval(() => {
        ctx.fillStyle = 'rgba(5, 8, 20, 0.1)'; ctx.fillRect(0, 0, w, h);
        ctx.fillStyle = '#0ea5e9'; ctx.font = size + 'px monospace';
        drops.forEach((y, i) => { ctx.fillText(symbols.charAt(Math.floor(Math.random()*symbols.length)), i*size, y*size); if(y*size > h && Math.random() > 0.95) drops[i]=0; drops[i]++; });
    }, 30);
});
</script>
"""

BLIND_BAG_STYLE = """
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { box-sizing: border-box; }
body { margin: 0; font-family: Arial, sans-serif; background: #050814; color: white; overflow-x: hidden; }
header { padding: 25px 15px; text-align: center; background: linear-gradient(135deg, #be185d, #e11d48); position: relative; }
header h1 { margin: 0; font-size: 25px; text-shadow: 0 0 10px #fff; }
.back-btn { position: absolute; top: 10px; left: 15px; background: rgba(0,0,0,0.4); padding: 5px 10px; border-radius: 15px; font-size: 12px; border: 1px solid rgba(255,255,255,0.4); color: white; text-decoration: none; font-weight: bold; }
.user-badge { position: absolute; top: 10px; right: 15px; background: rgba(0,0,0,0.4); padding: 5px 10px; border-radius: 15px; font-size: 12px; border: 1px solid rgba(255,255,255,0.4); }
.container { max-width: 650px; margin: auto; padding: 15px; position: relative; z-index: 10; }
.card { background: rgba(19, 29, 48, 0.9); border: 1px solid #f43f5e; border-radius: 14px; padding: 18px; margin-bottom: 15px; }
.card h2 { margin-top: 0; color: #fb7185; font-size: 18px; text-align: center; }
.coin-box { background: linear-gradient(135deg, #854d0e, #a16207); border: 1px solid #facc15; padding: 12px; border-radius: 10px; text-align: center; font-size: 17px; font-weight: bold; color: #fef08a; margin-bottom: 15px; }
.btn-action { display: block; width: 100%; padding: 12px; background: linear-gradient(135deg, #e11d48, #be185d); color: white; border: none; border-radius: 10px; font-size: 15px; font-weight: bold; cursor: pointer; text-decoration: none; margin-top: 8px; }
.bags-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; margin: 15px 0; }
.bag-item { background: #0b1326; border: 2px dashed #f43f5e; border-radius: 12px; padding: 20px 10px; text-align: center; cursor: pointer; }
.bag-item:hover { background: #1f1124; border-color: #fb7185; }
.history-box { background: #0b1326; border: 1px solid #1e3a8a; border-radius: 8px; padding: 10px; max-height: 200px; overflow-y: auto; font-size: 12px; color: #cbd5e1; }
.history-item { padding: 6px 0; border-bottom: 1px solid #172554; }
#radar-canvas { position: fixed; inset: 0; pointer-events: none; z-index: 1; opacity: 0.15; }
</style>
<script>
window.addEventListener('DOMContentLoaded', () => {
    const canvas = document.createElement('canvas'); canvas.id = 'radar-canvas'; document.body.prepend(canvas);
    const ctx = canvas.getContext('2d'); let w = canvas.width = window.innerWidth, h = canvas.height = window.innerHeight; let angle = 0;
    setInterval(() => {
        ctx.fillStyle = 'rgba(5, 8, 20, 0.08)'; ctx.fillRect(0, 0, w, h);
        ctx.strokeStyle = '#f43f5e'; ctx.lineWidth = 1; const cx = w/2, cy = h/2;
        ctx.beginPath(); ctx.arc(cx, cy, 100, 0, Math.PI*2); ctx.arc(cx, cy, 200, 0, Math.PI*2); ctx.stroke();
        ctx.save(); ctx.translate(cx, cy); ctx.rotate(angle); ctx.strokeStyle = '#fb7185'; ctx.lineWidth = 2;
        ctx.beginPath(); ctx.moveTo(0,0); ctx.lineTo(300,0); ctx.stroke(); ctx.restore(); angle += 0.03;
    }, 30);
});
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
            if u not in user_history: user_history[u] = []
            return redirect(url_for("home"))
        error = "Tài khoản hoặc mật khẩu không chính xác!"
    return render_template_string("""
    <!DOCTYPE html><html lang="vi"><head><title>ĐĂNG NHẬP</title>{{ style | safe }}</head>
    <body>
    <header><h1>🛍️ SHOP BUG NEW</h1><p>CỔNG ĐĂNG NHẬP</p></header>
    <div class="container" style="margin-top: 30px;">
        <div class="card">
            <h2>🔑 ĐĂNG NHẬP</h2>
            {% if success %}<div class="success-msg">{{ success }}</div>{% endif %}
            {% if error %}<div class="error-msg">{{ error }}</div>{% endif %}
            <form method="POST">
                <div class="form-group"><label>Tài khoản:</label><input type="text" name="username" class="form-control" required></div>
                <div class="form-group"><label>Mật khẩu:</label>
                    <div class="password-wrapper">
                        <input type="password" name="password" id="p1" class="form-control" required>
                        <button type="button" class="toggle-password" onclick="togglePassword('p1', this)">👁️</button>
                    </div>
                </div>
                <button type="submit" class="btn">🚀 ĐĂNG NHẬP</button>
            </form>
            <div class="switch-link">Chưa có tài khoản? <a href="/register">Đăng ký ngay</a></div>
        </div>
    </div></body></html>""", style=LOGIN_REGISTER_STYLE, success=success, error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        u, p = request.form.get("username", "").strip(), request.form.get("password", "").strip()
        if not u.isalpha(): error = "Tài khoản chỉ được chứa chữ cái, không số/ký tự đặc biệt!"
        elif u in users_db: error = "Tài khoản đã tồn tại!"
        elif len(p) < 6: error = "Mật khẩu phải từ 6 ký tự!"
        else:
            users_db[u], user_coins[u], user_history[u] = p, 0, []
            return redirect(url_for("login", success="Đăng ký thành công! Hãy đăng nhập."))
    return render_template_string("""
    <!DOCTYPE html><html lang="vi"><head><title>ĐĂNG KÝ</title>{{ style | safe }}</head>
    <body>
    <header><h1>🛍️ SHOP BUG NEW</h1><p>TẠO TÀI KHOẢN</p></header>
    <div class="container" style="margin-top: 20px;">
        <div class="card">
            <h2>➕ ĐĂNG KÝ</h2>
            {% if error %}<div class="error-msg">{{ error }}</div>{% endif %}
            <form method="POST">
                <div class="form-group"><label>Tài khoản (Chỉ chữ cái):</label><input type="text" name="username" class="form-control" required></div>
                <div class="form-group"><label>Mật khẩu:</label>
                    <div class="password-wrapper">
                        <input type="password" name="password" id="p2" class="form-control" required>
                        <button type="button" class="toggle-password" onclick="togglePassword('p2', this)">👁️</button>
                    </div>
                </div>
                <button type="submit" class="btn">✨ ĐĂNG KÝ NGAY</button>
            </form>
            <div class="switch-link">Đã có tài khoản? <a href="/login">Đăng nhập ngay</a></div>
        </div>
    </div></body></html>""", style=LOGIN_REGISTER_STYLE, error=error)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
    HOME_STYLE = """
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { box-sizing: border-box; }
body { margin: 0; font-family: Arial, sans-serif; background: #050814; color: white; scroll-behavior: smooth; overflow-x: hidden; }
header { padding: 25px 15px; text-align: center; background: linear-gradient(135deg, #1d4ed8, #0284c7); position: relative; z-index: 10; }
header h1 { margin: 0; font-size: 25px; }
.user-badge { position: absolute; top: 10px; right: 15px; background: rgba(0,0,0,0.4); padding: 5px 10px; border-radius: 15px; font-size: 12px; }
.user-badge a { color: #f87171; text-decoration: none; margin-left: 5px; font-weight: bold; }
.blind-bag-btn-top { position: absolute; top: 10px; left: 15px; background: rgba(220,38,38,0.8); padding: 5px 10px; border-radius: 15px; font-size: 12px; color: white; text-decoration: none; font-weight: bold; }
.container { max-width: 650px; margin: auto; padding: 15px; position: relative; z-index: 10; }
.card { background: rgba(19, 29, 48, 0.9); border: 1px solid #1e3a8a; border-radius: 14px; padding: 18px; margin-bottom: 15px; }
.card h2 { margin-top: 0; color: #38bdf8; font-size: 18px; }
.price { display: flex; justify-content: space-between; padding: 12px; margin: 8px 0; background: #0b1326; border-radius: 8px; border: 1px solid #172554; }
.money { color: #4ade80; font-weight: bold; }
.nav-acc-btn { display: block; text-align: center; background: linear-gradient(135deg, #0284c7, #2563eb); color: white; padding: 14px; border-radius: 12px; font-size: 16px; font-weight: bold; text-decoration: none; margin-bottom: 20px; }
.acc-item { background: #0b1326; border-radius: 10px; padding: 12px; margin-bottom: 15px; border: 1px solid #1e3a8a; }
.button { display: block; text-align: center; margin-top: 10px; padding: 10px; background: #22c55e; color: #052e16; text-decoration: none; border-radius: 8px; font-weight: bold; }
.contact { text-align: center; padding: 20px; background: linear-gradient(135deg, #082f49, #0369a1); border-radius: 14px; border: 1px solid #38bdf8; }
footer { text-align: center; padding: 20px; color: #94a3b8; font-size: 12px; }
#cyber-stream-canvas { position: fixed; inset: 0; pointer-events: none; z-index: 1; opacity: 0.2; }
</style>
<script>
window.addEventListener('DOMContentLoaded', () => {
    const canvas = document.createElement('canvas'); canvas.id = 'cyber-stream-canvas'; document.body.prepend(canvas);
    const ctx = canvas.getContext('2d'); let w = canvas.width = window.innerWidth, h = canvas.height = window.innerHeight;
    const symbols = '⚡💎BUGNEW'; const size = 16; const cols = w / size; const drops = Array.from({length: cols}, () => Math.floor(Math.random() * h));
    setInterval(() => {
        ctx.fillStyle = 'rgba(5, 8, 20, 0.1)'; ctx.fillRect(0, 0, w, h);
        ctx.fillStyle = '#0ea5e9'; ctx.font = size + 'px monospace';
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
    <!DOCTYPE html><html lang="vi"><head><title>SHOP LIKES</title>{{ style | safe }}</head>
    <body>
    <header>
        <a href="/blind-bag" class="blind-bag-btn-top">🎁 Túi Mù</a>
        <div class="user-badge">👤 <b>{{ u }}</b> | <a href="/logout">Đăng xuất</a></div>
        <h1>🛍️ SHOP BUG NEW</h1><p>🎮 DỊCH VỤ GAME FF</p>
    </header>
    <div class="container">
        <div class="card" style="text-align:center;">
            <h2>🔥 BẢNG GIÁ BUFF LIKES</h2>
            <p style="color:#cbd5e1; font-size:13px;">Mỗi ngày tối đa 220 likes / ngày!</p>
        </div>
        <div class="card">
            <h2>🏦 CHUYỂN KHOẢN</h2>
            <div class="price"><span>👍 220 Likes</span><span class="money">2.000đ</span></div>
            <div class="price"><span>👍 1.100 Likes</span><span class="money">5.000đ</span></div>
            <div class="price"><span>👍 3.300 Likes</span><span class="money">10.000đ</span></div>
            <div class="price"><span>👍 8.800 Likes</span><span class="money">20.000đ</span></div>
        </div>
        <div class="card">
            <h2>💳 THẺ CÀO & ĐỒ TRONG GAME</h2>
            <div class="price"><span>👍 4.400 Likes (Thẻ)</span><span class="money">20.000đ</span></div>
            <div class="price"><span>👍 2.200 Likes (Đồ)</span><span class="money">💎 < 100</span></div>
            <div class="price"><span>👍 5.500 Likes (Đồ)</span><span class="money">💎 < 200</span></div>
        </div>
        <a href="#kho-acc" class="nav-acc-btn">📦 XEM KHO ACC FREE FIRE (10 ACC)</a>
        <div class="card" id="kho-acc">
            <h2 style="text-align:center;">🔥 KHO ACC FREE FIRE 🔥</h2>
            {% for i in range(1, 11) %}
            <div class="acc-item">
                <h3 style="color:#38bdf8; margin:0 0 5px 0;">🎮 Acc #{{ i }}</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:0 0 8px 0;">Acc chọn lọc chất lượng cao cho anh em.</p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            {% endfor %}
        </div>
        <div class="contact">
            <h2>📩 MUA LIKES IB NHA!</h2>
            <p>Facebook: <b>Bug New</b></p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">💬 LIÊN HỆ FACEBOOK</a>
        </div>
    </div>
    <footer>🔰 © 2026 BUG NEW 🔰</footer>
    </body></html>""", style=HOME_STYLE, u=u)

@app.route("/blind-bag", methods=["GET", "POST"])
def blind_bag():
    import random
    if "user" not in session: return redirect(url_for("login"))
    u = session["user"]
    msg, msg_type = None, None
    if u not in user_coins: user_coins[u] = 0
    if u not in user_history: user_history[u] = []
    today = datetime.now().strftime("%Y-%m-%d")

    if request.method == "POST" and request.form.get("action") == "checkin":
        if last_checkin.get(u) == today:
            msg, msg_type = "❌ Bạn đã điểm danh hôm nay rồi!", "error"
        else:
            last_checkin[u] = today
            user_coins[u] += 200
            user_history[u].insert(0, f"[{datetime.now().strftime('%H:%M %d/%m')}] 🎁 Nhận 200 xu điểm danh")
            msg, msg_type = "🎉 Nhận thành công +200 xu!", "success"

    if request.method == "POST" and request.form.get("action") == "open_bag":
        if user_coins[u] < 75:
            msg, msg_type = f"❌ Không đủ xu! Cần 75 xu (Bạn có {user_coins[u]} xu).", "error"
        else:
            user_coins[u] -= 75
            # Xác suất chuẩn chỉnh y hệt hình ảnh bạn cung cấp
            rewards = [
                "💔 Chúc bạn may mắn lần sau", 
                "❤️ 20 like", 
                "❤️ 50 like", 
                "❤️ 100 like", 
                "❤️ 150 like", 
                "❤️ 200 like", 
                "❤️ 220 like", 
                "🔥 1100 like"
            ]
            weights = [25, 24, 17, 13, 9, 6, 4, 2]
            won = random.choices(rewards, weights=weights, k=1)[0]
            
            user_history[u].insert(0, f"[{datetime.now().strftime('%H:%M %d/%m')}] 🛍️ Mở túi (-75 xu) - Trúng: {won}")
            msg, msg_type = f"🎁 KẾT QUẢ: {won}", "reward"

    return render_template_string("""
    <!DOCTYPE html><html lang="vi"><head><title>TÚI MÙ LIKES</title>{{ style | safe }}</head>
    <body>
    <header>
        <a href="/" class="back-btn">🏠 Trang Chủ</a>
        <div class="user-badge">👤 <b>{{ u }}</b></div>
        <h1>🎁 TÚI MÙ LIKES FF</h1><p>SĂN NHÂN PHẨM</p>
    </header>
    <div class="container">
        <div class="coin-box">💰 Tài khoản: <b>{{ u }}</b> | 🪙 Xu hiện có: <span style="color:#facc15;">{{ coins }}</span> xu</div>
        {% if msg %}
            <div class="card" style="border-color:{{ '#10b981' if msg_type=='success' else ('#f43f5e' if msg_type=='reward' else '#ef4444') }}; text-align:center;">
                <h3 style="margin:0; color:{{ '#6ee7b7' if msg_type=='success' else ('#fb7185' if msg_type=='reward' else '#fca5a5') }};">{{ msg }}</h3>
                {% if msg_type == 'reward' %}
                    <p style="font-size:12px; color:#cbd5e1; margin:8px 0;">Chụp màn hình gửi Admin kèm FF ID để nhận thưởng!</p>
                    <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">💬 GỬI ẢNH CHO ADMIN</a>
                {% endif %}
            </div>
        {% endif %}
        <div class="card">
            <h2>📅 ĐIỂM DANH HẰNG NGÀY</h2>
            <form method="POST"><input type="hidden" name="action" value="checkin">
                <button type="submit" class="btn-action" style="background:linear-gradient(135deg, #059669, #10b981);">🎁 NHẬN 200 XU</button>
            </form>
        </div>
        <div class="card">
            <h2>🛍️ CHỌN 1 TRONG 4 TÚI MÙ (75 XU)</h2>
            <div class="bags-grid">
                {% for i in range(1, 5) %}
                <form method="POST"><input type="hidden" name="action" value="open_bag">
                    <button type="submit" class="bag-item" style="width:100%;">
                        <span style="font-size:30px;">📦</span><h3 style="margin:5px 0; color:#fb7185;">Túi #{{ i }}</h3><span style="font-size:11px; color:#cbd5e1;">Phí: 75 xu</span>
                    </button>
                </form>
                {% endfor %}
            </div>
        </div>
        <div class="card">
            <h2>📜 LỊCH SỬ HOẠT ĐỘNG ({{ u }})</h2>
            <div class="history-box">
                {% if history %}{% for item in history %}<div class="history-item">{{ item }}</div>{% endfor %}
                {% else %}<div style="text-align:center; color:#64748b; padding:10px;">Chưa có lịch sử.</div>{% endif %}
            </div>
        </div>
    </div>
    <footer>📈 © Mua Likes ib Bug New ☎️</footer>
    </body></html>""", style=BLIND_BAG_STYLE, u=u, coins=user_coins[u], history=user_history[u], msg=msg, msg_type=msg_type)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
