from datetime import datetime
import random
from flask import Flask, redirect, render_template_string, request, session, url_for

app = Flask(__name__)
app.secret_key = "bug_new_secret_key_secure_3d"

users_db = {"BugNew": {"pass": "bugnewff.01", "gmail": "bugnew@gmail.com"}}
user_coins = {"BugNew": 500}
global_history = [
    (
        "BugNew",
        f"[{datetime.now().strftime('%H:%M %d/%m')}] 🎁 Nhận 200 xu điểm danh",
    )
]
last_checkin = {}

# GIAO DIỆN 1: ĐĂNG NHẬP / ĐĂNG KÝ (Hiệu ứng Network Cyber 3D - Không trùng lặp)
AUTH_STYLE = """
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #020617; color: #f3f4f6; overflow-x: hidden; }
header { padding: 40px 20px; text-align: center; background: radial-gradient(circle, #1e1b4b 0%, #020617 100%); border-bottom: 3px solid #6366f1; box-shadow: 0 15px 35px rgba(99, 102, 241, 0.4); }
header h1 { margin: 0; font-size: 32px; letter-spacing: 2px; color: #818cf8; text-shadow: 0 0 25px rgba(129, 140, 248, 0.9); }
header p { margin: 8px 0 0 0; color: #c7d2fe; font-size: 13px; text-transform: uppercase; letter-spacing: 4px; font-weight: bold; }
.container { max-width: 480px; margin: auto; padding: 20px; position: relative; z-index: 10; }
.card { background: rgba(15, 23, 42, 0.88); border: 2px solid #6366f1; border-radius: 20px; padding: 28px; margin-bottom: 20px; box-shadow: 0 15px 50px rgba(99, 102, 241, 0.3); backdrop-filter: blur(15px); }
.card h2 { margin-top: 0; color: #818cf8; font-size: 22px; text-align: center; text-transform: uppercase; letter-spacing: 2px; }
.form-group { margin-bottom: 16px; }
.form-group label { display: block; margin-bottom: 6px; color: #a5b4fc; font-weight: 600; font-size: 14px; }
.password-wrapper { position: relative; }
.form-control { width: 100%; padding: 14px; padding-right: 45px; background: #090d16; border: 1px solid #3730a3; border-radius: 12px; color: white; font-size: 15px; transition: all 0.3s ease; }
.form-control:focus { outline: none; border-color: #818cf8; box-shadow: 0 0 20px rgba(129, 140, 248, 0.5); }
.toggle-password { position: absolute; right: 12px; top: 50%; transform: translateY(-50%); background: none; border: none; cursor: pointer; font-size: 16px; color: #818cf8; }
.btn { display: block; width: 100%; padding: 15px; background: linear-gradient(135deg, #4f46e5, #9333ea); color: white; border: none; border-radius: 12px; font-size: 16px; font-weight: bold; cursor: pointer; text-transform: uppercase; letter-spacing: 2px; box-shadow: 0 6px 25px rgba(147, 51, 234, 0.6); transition: transform 0.2s; }
.btn:active { transform: scale(0.98); }
.error-msg { background: rgba(153, 27, 27, 0.6); border: 1px solid #ef4444; color: #fca5a5; padding: 12px; border-radius: 12px; margin-bottom: 15px; text-align: center; font-weight: bold; font-size: 14px; }
.success-msg { background: rgba(6, 78, 59, 0.6); border: 1px solid #10b981; color: #6ee7b7; padding: 12px; border-radius: 12px; margin-bottom: 15px; text-align: center; font-weight: bold; font-size: 14px; }
.switch-link { text-align: center; margin-top: 15px; font-size: 14px; color: #94a3b8; }
.switch-link a { color: #818cf8; text-decoration: none; font-weight: bold; }
#network-canvas { position: fixed; inset: 0; pointer-events: none; z-index: 1; }
</style>
<script>
window.addEventListener('DOMContentLoaded', () => {
    const canvas = document.createElement('canvas'); canvas.id = 'network-canvas'; document.body.prepend(canvas);
    const ctx = canvas.getContext('2d'); let w = canvas.width = window.innerWidth, h = canvas.height = window.innerHeight;
    window.addEventListener('resize', () => { w = canvas.width = window.innerWidth; h = canvas.height = window.innerHeight; });
    const particles = Array.from({length: 50}, () => ({
        x: Math.random() * w, y: Math.random() * h,
        vx: (Math.random() - 0.5) * 1.5, vy: (Math.random() - 0.5) * 1.5,
        radius: Math.random() * 2.5 + 1
    }));
    function animate() {
        ctx.fillStyle = 'rgba(2, 6, 23, 0.25)'; ctx.fillRect(0, 0, w, h);
        ctx.strokeStyle = 'rgba(99, 102, 241, 0.15)'; ctx.lineWidth = 1;
        for (let i = 0; i < particles.length; i++) {
            let p1 = particles[i];
            p1.x += p1.vx; p1.y += p1.vy;
            if (p1.x < 0 || p1.x > w) p1.vx *= -1;
            if (p1.y < 0 || p1.y > h) p1.vy *= -1;
            ctx.fillStyle = '#818cf8'; ctx.beginPath(); ctx.arc(p1.x, p1.y, p1.radius, 0, Math.PI * 2); ctx.fill();
            for (let j = i + 1; j < particles.length; j++) {
                let p2 = particles[j];
                let dist = Math.hypot(p1.x - p2.x, p1.y - p2.y);
                if (dist < 120) {
                    ctx.beginPath(); ctx.moveTo(p1.x, p1.y); ctx.lineTo(p2.x, p2.y); ctx.stroke();
                }
            }
        }
        requestAnimationFrame(animate);
    }
    animate();
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
        if u in users_db and users_db[u]["pass"] == p:
            session["user"] = u
            if u not in user_coins: user_coins[u] = 0
            return redirect(url_for("home"))
        error = "Tài khoản hoặc mật khẩu không chính xác!"
    return render_template_string("""
    <!DOCTYPE html><html lang="vi"><head><title>ĐĂNG NHẬP - HỆ THỐNG SAO LƯU GMAIL</title>{{ style | safe }}</head>
    <body>
    <header><h1>🔐 SHOP BUG NEW</h1><p>CỔNG ĐĂNG NHẬP BẢO MẬT</p></header>
    <div class="container" style="margin-top: 30px;">
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
                <button type="submit" class="btn">🚀 TRUY CẬP HỆ THỐNG</button>
            </form>
            <div class="switch-link">Chưa có tài khoản? <a href="/register">Đăng ký sao lưu ngay</a></div>
        </div>
    </div></body></html>""", style=AUTH_STYLE, success=success, error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        u = request.form.get("username", "").strip()
        p = request.form.get("password", "").strip()
        gmail = request.form.get("gmail", "").strip()
        if not u.isalpha(): error = "Tài khoản chỉ được chứa chữ cái, không số/ký tự đặc biệt!"
        elif u in users_db: error = "Tài khoản đã tồn tại trên hệ thống!"
        elif len(p) < 6: error = "Mật khẩu phải từ 6 ký tự trở lên!"
        elif "@gmail.com" not in gmail: error = "Vui lòng nhập đúng định dạng Gmail để sao lưu tài khoản!"
        else:
            users_db[u] = {"pass": p, "gmail": gmail}
            user_coins[u] = 0
            return redirect(url_for("login", success="Đăng ký & Sao lưu Gmail thành công! Hãy đăng nhập."))
    return render_template_string("""
    <!DOCTYPE html><html lang="vi"><head><title>ĐĂNG KÝ & SAO LƯU GMAIL</title>{{ style | safe }}</head>
    <body>
    <header><h1>🛡️ SHOP BUG NEW</h1><p>ĐĂNG KÝ & SAO LƯU GMAIL</p></header>
    <div class="container" style="margin-top: 20px;">
        <div class="card">
            <h2>➕ TẠO TÀI KHOẢN MỚI</h2>
            {% if error %}<div class="error-msg">{{ error }}</div>{% endif %}
            <form method="POST">
                <div class="form-group"><label>Tài khoản (Chỉ chữ cái):</label><input type="text" name="username" class="form-control" placeholder="Ví dụ: BugNew" required></div>
                <div class="form-group"><label>Gmail sao lưu (Tránh mất acc):</label><input type="email" name="gmail" class="form-control" placeholder="vd: email@gmail.com" required></div>
                <div class="form-group"><label>Mật khẩu:</label>
                    <div class="password-wrapper">
                        <input type="password" name="password" id="p2" class="form-control" placeholder="Ít nhất 6 ký tự..." required>
                        <button type="button" class="toggle-password" onclick="togglePassword('p2', this)">👁️</button>
                    </div>
                </div>
                <button type="submit" class="btn">✨ XÁC NHẬN ĐĂNG KÝ</button>
            </form>
            <div class="switch-link">Đã có tài khoản? <a href="/login">Đăng nhập ngay</a></div>
        </div>
    </div></body></html>""", style=AUTH_STYLE, error=error)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# GIAO DIỆN 2: TRANG CHỦ / SẢNH CHÍNH (Hiệu ứng 3D Rực Lửa phong cách Free Fire)
HOME_STYLE = """
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0c0502; color: #f3f4f6; scroll-behavior: smooth; overflow-x: hidden; }
header { padding: 35px 15px; text-align: center; background: linear-gradient(135deg, #450a0a, #991b1b, #ea580c); position: relative; z-index: 10; border-bottom: 3px solid #fb923c; box-shadow: 0 15px 40px rgba(234, 88, 12, 0.4); }
header h1 { margin: 0; font-size: 28px; color: #ffedd5; text-shadow: 0 0 25px rgba(255, 237, 213, 0.9); }
header p { margin: 6px 0 0 0; color: #fed7aa; font-size: 13px; letter-spacing: 2px; font-weight: bold; text-transform: uppercase; }
.user-badge { position: absolute; top: 12px; right: 15px; background: rgba(69, 10, 10, 0.9); border: 1px solid #fb923c; padding: 6px 12px; border-radius: 20px; font-size: 12px; backdrop-filter: blur(5px); }
.user-badge a { color: #fca5a5; text-decoration: none; margin-left: 6px; font-weight: bold; }
.blind-bag-btn-top { position: absolute; top: 12px; left: 15px; background: linear-gradient(135deg, #7c2d12, #c2410c); border: 1px solid #fdba74; padding: 6px 12px; border-radius: 20px; font-size: 12px; color: white; text-decoration: none; font-weight: bold; box-shadow: 0 0 15px rgba(194, 65, 12, 0.6); }
.container { max-width: 650px; margin: auto; padding: 15px; position: relative; z-index: 10; }
.card { background: rgba(69, 10, 10, 0.35); border: 2px solid #ea580c; border-radius: 18px; padding: 22px; margin-bottom: 20px; box-shadow: 0 10px 35px rgba(0, 0, 0, 0.6); backdrop-filter: blur(12px); }
.card h2 { margin-top: 0; color: #fb923c; font-size: 19px; border-bottom: 1px solid #7c2d12; padding-bottom: 10px; text-transform: uppercase; letter-spacing: 1px; }
.price { display: flex; justify-content: space-between; align-items: center; padding: 13px 16px; margin: 11px 0; background: #180805; border-radius: 12px; border: 1px solid #7c2d12; transition: all 0.2s; }
.price:hover { border-color: #fb923c; box-shadow: 0 0 15px rgba(251, 146, 60, 0.4); }
.money { color: #facc15; font-weight: bold; font-size: 15px; text-shadow: 0 0 8px rgba(250, 204, 21, 0.5); }
.nav-acc-btn { display: block; text-align: center; background: linear-gradient(135deg, #c2410c, #ea580c); color: white; padding: 16px; border-radius: 14px; font-size: 16px; font-weight: bold; text-decoration: none; margin-bottom: 22px; box-shadow: 0 8px 25px rgba(234, 88, 12, 0.5); text-transform: uppercase; letter-spacing: 1px; }
.acc-item { background: #180805; border-radius: 14px; padding: 16px; margin-bottom: 20px; border: 2px solid #9a3412; transition: transform 0.2s; }
.acc-item:hover { transform: translateY(-2px); border-color: #fb923c; box-shadow: 0 0 20px rgba(251, 146, 60, 0.3); }
.acc-item img { width: 100%; border-radius: 12px; margin-bottom: 12px; border: 1px solid #7c2d12; }
.button { display: block; text-align: center; margin-top: 12px; padding: 13px; background: linear-gradient(135deg, #16a34a, #22c55e); color: #052e16; text-decoration: none; border-radius: 12px; font-weight: bold; box-shadow: 0 4px 15px rgba(34, 197, 94, 0.4); text-transform: uppercase; font-size: 14px; }
.contact { text-align: center; padding: 25px 20px; background: linear-gradient(135deg, #7c2d12, #9a3412); border-radius: 18px; border: 2px solid #fb923c; box-shadow: 0 10px 30px rgba(154, 52, 18, 0.4); }
footer { text-align: center; padding: 25px; color: #78716c; font-size: 13px; letter-spacing: 1px; }
#fire-canvas { position: fixed; inset: 0; pointer-events: none; z-index: 1; opacity: 0.25; }
</style>
<script>
window.addEventListener('DOMContentLoaded', () => {
    const canvas = document.createElement('canvas'); canvas.id = 'fire-canvas'; document.body.prepend(canvas);
    const ctx = canvas.getContext('2d'); let w = canvas.width = window.innerWidth, h = canvas.height = window.innerHeight;
    window.addEventListener('resize', () => { w = canvas.width = window.innerWidth; h = canvas.height = window.innerHeight; });
    const flames = Array.from({length: 60}, () => ({
        x: Math.random() * w, y: h + Math.random() * 100,
        vx: (Math.random() - 0.5) * 1.2, vy: -Math.random() * 3 - 1.5,
        radius: Math.random() * 6 + 2, life: Math.random() * 80 + 20
    }));
    function animateFire() {
        ctx.fillStyle = 'rgba(12, 5, 2, 0.2)'; ctx.fillRect(0, 0, w, h);
        flames.forEach(f => {
            f.x += f.vx; f.y += f.vy; f.life--;
            ctx.fillStyle = f.life > 50 ? '#f97316' : (f.life > 20 ? '#ef4444' : '#facc15');
            ctx.beginPath(); ctx.arc(f.x, f.y, f.radius, 0, Math.PI * 2); ctx.fill();
            if (f.life <= 0 || f.y < 0) {
                f.x = Math.random() * w; f.y = h + 20; f.life = Math.random() * 80 + 20;
            }
        });
        requestAnimationFrame(animateFire);
    }
    animateFire();
});
</script>
"""
@app.route("/")
def home():
    if "user" not in session: return redirect(url_for("login"))
    u = session["user"]
    return render_template_string("""
    <!DOCTYPE html><html lang="vi"><head><title>TRANG CHỦ - KHO ACC & BẢNG GIÁ FF</title>{{ style | safe }}</head>
    <body>
    <header>
        <a href="/blind-bag" class="blind-bag-btn-top">🎁 Túi Mù 3D</a>
        <div class="user-badge">👤 <b>{{ u }}</b> | <a href="/logout">Đăng xuất</a></div>
        <h1>🔥 SHOP BUG NEW</h1><p>🎮 KHO 10 ACC FREE FIRE & DỊCH VỤ LIKES</p>
    </header>
    <div class="container" style="margin-top: 15px;">
        <div class="card" style="text-align:center;">
            <h2>🔥 BẢNG GIÁ BUFF LIKES</h2>
            <p style="color:#fed7aa; font-size:13px; margin:5px 0 0 0;">Mỗi ngày tối đa 220 likes / ngày!</p>
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
                <h3 style="color:#fb923c; margin:5px 0; font-size:16px;">🎮 Acc #1</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 34<br>🔐 <b>Login:</b> Facebook<br>💰 <b>Giá:</b> <strong style="color:#facc15;">35.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            <div class="acc-item">
                <img src="https://i.postimg.cc/3R7RwWS6/Screenshot-20261102-174720-com-dts-freefireth.jpg" alt="Acc 2">
                <h3 style="color:#fb923c; margin:5px 0; font-size:16px;">🎮 Acc #2</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 21<br>🔐 <b>Login:</b> Facebook<br>💰 <b>Giá:</b> <strong style="color:#facc15;">20.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            <div class="acc-item">
                <img src="https://i.postimg.cc/3NxxgVHC/Screenshot-20261031-191554-com-dts-freefireth.jpg" alt="Acc 3">
                <h3 style="color:#fb923c; margin:5px 0; font-size:16px;">🎮 Acc #3</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 18<br>🔐 <b>Login:</b> Facebook<br>💰 <b>Giá:</b> <strong style="color:#facc15;">15.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            <div class="acc-item">
                <img src="https://i.postimg.cc/rwfKhsvC/Screenshot-20261031-191554-com-dts-freefireth.jpg" alt="Acc 4">
                <h3 style="color:#fb923c; margin:5px 0; font-size:16px;">🎮 Acc #4</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 26<br>🔐 <b>Login:</b> Google<br>💰 <b>Giá:</b> <strong style="color:#facc15;">15.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            <div class="acc-item">
                <img src="https://i.postimg.cc/28cDMWSj/Screenshot-20261031-191815-com-dts-freefireth.jpg" alt="Acc 5">
                <h3 style="color:#fb923c; margin:5px 0; font-size:16px;">🎮 Acc #5</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 9<br>🔐 <b>Login:</b> Google<br>💰 <b>Giá:</b> <strong style="color:#facc15;">36.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            <div class="acc-item">
                <img src="https://i.postimg.cc/XqjRDNM8/Screenshot-20261031-191924-com-dts-freefireth.jpg" alt="Acc 6">
                <h3 style="color:#fb923c; margin:5px 0; font-size:16px;">🎮 Acc #6</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 13<br>🔐 <b>Login:</b> Google<br>💰 <b>Giá:</b> <strong style="color:#facc15;">5.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            <div class="acc-item">
                <img src="https://i.postimg.cc/ncwy0t3T/Screenshot-20261031-192021-com-dts-freefireth.jpg" alt="Acc 7">
                <h3 style="color:#fb923c; margin:5px 0; font-size:16px;">🎮 Acc #7</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 22<br>🔐 <b>Login:</b> Google<br>💰 <b>Giá:</b> <strong style="color:#facc15;">20.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            <div class="acc-item">
                <img src="https://i.postimg.cc/3w2z80YD/Screenshot-20261031-192143-com-dts-freefireth.jpg" alt="Acc 8">
                <h3 style="color:#fb923c; margin:5px 0; font-size:16px;">🎮 Acc #8</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 2<br>🔐 <b>Login:</b> Google<br>💰 <b>Giá:</b> <strong style="color:#facc15;">25.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            <div class="acc-item">
                <img src="https://i.postimg.cc/J4tgy2RD/Screenshot-20261031-192412-com-dts-freefireth.jpg" alt="Acc 9">
                <h3 style="color:#fb923c; margin:5px 0; font-size:16px;">🎮 Acc #9</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 28<br>🔐 <b>Login:</b> Facebook<br>💰 <b>Giá:</b> <strong style="color:#facc15;">30.000đ</strong></p>
                <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
            </div>
            <div class="acc-item">
                <img src="https://i.postimg.cc/JhCd27ZP/Screenshot-20261031-192920-com-dts-freefireth.jpg" alt="Acc 10">
                <h3 style="color:#fb923c; margin:5px 0; font-size:16px;">🎮 Acc #10</h3>
                <p style="color:#cbd5e1; font-size:13px; margin:5px 0; line-height:1.5;">⭐ <b>Level:</b> 14<br>🔐 <b>Login:</b> Facebook<br>💰 <b>Giá:</b> <strong style="color:#facc15;">10.000đ</strong></p>
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
    # GIAO DIỆN 3: TÚI MÙ (Hiệu ứng 3D Diamond / Box Particle, Hộp quà không gian 3D)
BLIND_STYLE = """
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0c021a; color: #f3f4f6; scroll-behavior: smooth; overflow-x: hidden; }
header { padding: 35px 15px; text-align: center; background: linear-gradient(135deg, #3b0764, #7e22ce, #c026d3); position: relative; z-index: 10; border-bottom: 3px solid #f0abfc; box-shadow: 0 15px 40px rgba(192, 38, 211, 0.4); }
header h1 { margin: 0; font-size: 28px; color: #fdf4ff; text-shadow: 0 0 25px rgba(253, 244, 255, 0.9); }
header p { margin: 6px 0 0 0; color: #fae8ff; font-size: 13px; letter-spacing: 2px; font-weight: bold; text-transform: uppercase; }
.back-btn { position: absolute; top: 12px; left: 15px; background: rgba(59, 7, 100, 0.9); border: 1px solid #f0abfc; padding: 6px 12px; border-radius: 20px; font-size: 12px; color: #f0abfc; text-decoration: none; font-weight: bold; }
.user-badge { position: absolute; top: 12px; right: 15px; background: rgba(59, 7, 100, 0.9); border: 1px solid #f0abfc; padding: 6px 12px; border-radius: 20px; font-size: 12px; backdrop-filter: blur(5px); color: #fae8ff; }
.container { max-width: 650px; margin: auto; padding: 15px; position: relative; z-index: 10; }
.coin-box { background: linear-gradient(135deg, #713f12, #ca8a04); border: 2px solid #fde047; padding: 16px; border-radius: 16px; text-align: center; font-size: 17px; font-weight: bold; color: #fef08a; margin-bottom: 20px; box-shadow: 0 8px 25px rgba(202, 138, 4, 0.4); }
.card { background: rgba(76, 29, 149, 0.25); border: 2px solid #9333ea; border-radius: 18px; padding: 22px; margin-bottom: 20px; box-shadow: 0 10px 35px rgba(0, 0, 0, 0.6); backdrop-filter: blur(12px); }
.card h2 { margin-top: 0; color: #f0abfc; font-size: 19px; border-bottom: 1px solid #581c87; padding-bottom: 10px; text-transform: uppercase; letter-spacing: 1px; }
.btn-action { display: block; width: 100%; padding: 15px; background: linear-gradient(135deg, #059669, #10b981); color: white; border: none; border-radius: 14px; font-size: 15px; font-weight: bold; cursor: pointer; text-decoration: none; margin-top: 10px; box-shadow: 0 6px 20px rgba(16, 185, 129, 0.4); text-transform: uppercase; letter-spacing: 1px; }
.bags-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; margin: 15px 0; }
.bag-item { background: #090d16; border: 2px solid #c026d3; border-radius: 16px; padding: 25px 10px; text-align: center; cursor: pointer; width: 100%; transition: all 0.25s; box-shadow: 0 5px 20px rgba(192, 38, 211, 0.25); }
.bag-item:hover { background: #1e1b4b; border-color: #f43f5e; transform: translateY(-4px) scale(1.02); box-shadow: 0 0 25px rgba(244, 63, 94, 0.6); }
.history-box { background: #090d16; border: 1px solid #581c87; border-radius: 12px; padding: 14px; max-height: 240px; overflow-y: auto; font-size: 13px; color: #e2e8f0; }
.history-item { padding: 9px 0; border-bottom: 1px solid #3b0764; }
.opening-modal { display: none; position: fixed; inset: 0; background: rgba(12, 2, 26, 0.94); backdrop-filter: blur(10px); z-index: 100; justify-content: center; align-items: center; flex-direction: column; text-align: center; padding: 25px; }
@keyframes boxShake { 0% { transform: translate(1px, 1px) rotate(0deg) scale(1); } 20% { transform: translate(-4px, 2px) rotate(-8deg) scale(1.05); } 40% { transform: translate(4px, -2px) rotate(8deg) scale(1.05); } 60% { transform: translate(-2px, 2px) rotate(-4deg) scale(1.02); } 100% { transform: translate(0, 0) rotate(0deg) scale(1); } }
.shaking { animation: boxShake 0.35s infinite; }
.box-3d { width: 90px; height: 90px; margin: 0 auto 20px auto; background: linear-gradient(135deg, #e11d48, #9333ea); border-radius: 20px; box-shadow: 0 0 35px rgba(225, 29, 72, 0.8), inset 0 0 15px rgba(255,255,255,0.4); display: flex; align-items: center; justify-content: center; font-size: 42px; border: 2px solid #f0abfc; }
.button { display: block; text-align: center; margin-top: 12px; padding: 13px; background: linear-gradient(135deg, #e11d48, #db2777); color: white; text-decoration: none; border-radius: 12px; font-weight: bold; box-shadow: 0 6px 20px rgba(225, 29, 72, 0.5); text-transform: uppercase; font-size: 14px; letter-spacing: 1px; }
footer { text-align: center; padding: 25px; color: #a855f7; font-size: 13px; letter-spacing: 1px; }
#diamond-canvas { position: fixed; inset: 0; pointer-events: none; z-index: 1; opacity: 0.25; }
</style>
<script>
window.addEventListener('DOMContentLoaded', () => {
    const canvas = document.createElement('canvas'); canvas.id = 'diamond-canvas'; document.body.prepend(canvas);
    const ctx = canvas.getContext('2d'); let w = canvas.width = window.innerWidth, h = canvas.height = window.innerHeight;
    window.addEventListener('resize', () => { w = canvas.width = window.innerWidth; h = canvas.height = window.innerHeight; });
    const stars = Array.from({length: 50}, () => ({
        x: Math.random() * w, y: Math.random() * h,
        size: Math.random() * 2.5 + 1, speed: Math.random() * 0.8 + 0.2
    }));
    function animateStars() {
        ctx.fillStyle = 'rgba(12, 2, 26, 0.25)'; ctx.fillRect(0, 0, w, h);
        ctx.fillStyle = '#f0abfc';
        stars.forEach(s => {
            s.y -= s.speed;
            if (s.y < 0) s.y = h;
            ctx.beginPath(); ctx.arc(s.x, s.y, s.size, 0, Math.PI * 2); ctx.fill();
        });
        requestAnimationFrame(animateStars);
    }
    animateStars();
});

function openBagAnimation(bagNum) {
    const modal = document.getElementById('openingModal');
    const boxImg = document.getElementById('boxImg');
    const rewardText = document.getElementById('rewardText');
    const actionBtn = document.getElementById('actionBtn');
    
    modal.style.display = 'flex';
    boxImg.classList.add('shaking');
    rewardText.textContent = "🎁 Đang giải mã hộp quà 3D #" + bagNum + "...";
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
                rewardText.innerHTML = "🎉 Trúng thưởng: <b style='color:#fde047'>" + data.reward + "</b>";
            } else {
                rewardText.innerHTML = "<b style='color:#f87171'>" + data.msg + "</b>";
            }
            actionBtn.style.display = "block";
        });
    }, 1600);
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
    <!DOCTYPE html><html lang="vi"><head><title>TÚI MÙ 3D - SHOP BUG NEW</title>{{ style | safe }}</head>
    <body>
    <header>
        <a href="/" class="back-btn">🏠 Trang Chủ</a>
        <div class="user-badge">👤 <b>{{ u }}</b></div>
        <h1>🎁 TÚI MÙ LIKES FF 3D</h1><p>SĂN QUÀ KHÔNG GIAN ẢO</p>
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
            <h2>💎 CHỌN 1 TRONG 4 HỘP QUÀ 3D (75 XU)</h2>
            <div class="bags-grid">
                <div class="bag-item" onclick="openBagAnimation(1)">
                    <div style="font-size:30px; margin-bottom:8px;">💎</div>
                    <h3 style="margin:5px 0; color:#f0abfc; font-size:15px;">Hộp #1</h3>
                    <span style="font-size:12px; color:#cbd5e1;">Phí: 75 xu</span>
                </div>
                <div class="bag-item" onclick="openBagAnimation(2)">
                    <div style="font-size:30px; margin-bottom:8px;">💎</div>
                    <h3 style="margin:5px 0; color:#f0abfc; font-size:15px;">Hộp #2</h3>
                    <span style="font-size:12px; color:#cbd5e1;">Phí: 75 xu</span>
                </div>
                <div class="bag-item" onclick="openBagAnimation(3)">
                    <div style="font-size:30px; margin-bottom:8px;">💎</div>
                    <h3 style="margin:5px 0; color:#f0abfc; font-size:15px;">Hộp #3</h3>
                    <span style="font-size:12px; color:#cbd5e1;">Phí: 75 xu</span>
                </div>
                <div class="bag-item" onclick="openBagAnimation(4)">
                    <div style="font-size:30px; margin-bottom:8px;">💎</div>
                    <h3 style="margin:5px 0; color:#f0abfc; font-size:15px;">Hộp #4</h3>
                    <span style="font-size:12px; color:#cbd5e1;">Phí: 75 xu</span>
                </div>
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
        <div class="box-3d" id="boxImg">💎</div>
        <h2 id="rewardText" style="color:#f0abfc; margin-bottom:20px; font-size:20px;">Đang giải mã hộp quà 3D...</h2>
        <div id="actionBtn" style="display:none; width:100%; max-width:320px;">
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank" style="margin-bottom:12px;">💬 GỬI ẢNH CHO ADMIN QUA FACEBOOK</a>
            <button onclick="location.reload()" style="background:#3b0764; color:white; border:2px solid #f0abfc; padding:12px; width:100%; border-radius:12px; cursor:pointer; font-weight:bold; text-transform:uppercase;">TIẾP TỤC CHƠI</button>
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
    
    global_history.insert(0, (u, f"[{datetime.now().strftime('%H:%M %d/%m')}] 💎 Mở hộp 3D (-75 xu) - Trúng: {won}"))
    return {"status": "success", "reward": won}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
