from flask import Flask, redirect, render_template_string, request, session, url_for

app = Flask(__name__)
app.secret_key = "bug_new_secret_key_secure"

# Cơ sở dữ liệu giả lập tài khoản
users_db = {"bugnew": "bugnewff.01"}

# Giao diện CSS chung cho trang Đăng nhập / Đăng ký
COMMON_STYLE = """
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* { box-sizing: border-box; }
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #080d19;
    color: white;
    scroll-behavior: smooth;
}
header {
    padding: 28px 15px;
    text-align: center;
    background: linear-gradient(135deg, #1d4ed8, #0284c7);
}
header h1 { margin: 0; font-size: 27px; font-weight: 900; }
header p { margin-bottom: 0; color: #e0f2fe; }
.container { max-width: 650px; margin: auto; padding: 20px 15px; }
.card {
    background: #131d30;
    border: 1px solid #1e3a8a;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 18px;
}
.card h2 { margin-top: 0; color: #38bdf8; font-size: 20px; text-align: center; }
.form-group { margin-bottom: 15px; }
.form-group label { display: block; margin-bottom: 5px; color: #38bdf8; font-weight: bold; }
.form-control {
    width: 100%;
    padding: 12px;
    background: #1c2940;
    border: 1px solid #1e3a8a;
    border-radius: 10px;
    color: white;
    font-size: 16px;
}
.form-control:focus { outline: none; border-color: #38bdf8; }
.btn {
    display: block;
    width: 100%;
    text-align: center;
    padding: 14px;
    background: linear-gradient(135deg, #0284c7, #2563eb);
    color: white;
    border: none;
    border-radius: 10px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    text-decoration: none;
    transition: 0.3s;
}
.btn:hover { background: linear-gradient(135deg, #0ea5e9, #3b82f6); }
.error-msg { background: #450a0a; border: 1px solid #ef4444; color: #fca5a5; padding: 12px; border-radius: 10px; margin-bottom: 15px; text-align: center; font-weight: bold; }
.success-msg { background: #064e3b; border: 1px solid #10b981; color: #6ee7b7; padding: 12px; border-radius: 10px; margin-bottom: 15px; text-align: center; font-weight: bold; }
.switch-link { text-align: center; margin-top: 15px; color: #94a3b8; font-size: 14px; }
.switch-link a { color: #38bdf8; text-decoration: none; font-weight: bold; }
.switch-link a:hover { text-decoration: underline; }
</style>
"""


@app.route("/login", methods=["GET", "POST"])
def login():
  error = None
  success = request.args.get("success")

  if request.method == "POST":
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()

    if username in users_db and users_db[username] == password:
      session["user"] = username
      return redirect(url_for("home"))
    else:
      error = "Tên tài khoản hoặc mật khẩu không chính xác!"

  return (
      """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
    <title>ĐĂNG NHẬP - BUG NEW</title>
    """
      + COMMON_STYLE
      + """
    </head>
    <body>
    <header>
        <h1>🛍️ SHOP BUG NEW 🛍️</h1>
        <p>🔐 CỔNG ĐĂNG NHẬP HỆ THỐNG</p>
    </header>
    <div class="container" style="margin-top: 40px;">
        <div class="card">
            <h2>🔑 ĐĂNG NHẬP TÀI KHOẢN</h2>
            """
      + (f'<div class="success-msg">{success}</div>' if success else "")
      + """
            """
      + (f'<div class="error-msg">{error}</div>' if error else "")
      + """
            <form method="POST">
                <div class="form-group">
                    <label>Tên tài khoản:</label>
                    <input type="text" name="username" class="form-control" placeholder="Ví dụ: bugnew" required>
                </div>
                <div class="form-group">
                    <label>Mật khẩu:</label>
                    <input type="password" name="password" class="form-control" placeholder="Nhập mật khẩu..." required>
                </div>
                <button type="submit" class="btn">🚀 ĐĂNG NHẬP</button>
            </form>
            <div class="switch-link">
                Chưa có tài khoản? <a href="/register">Đăng ký ngay</a>
            </div>
        </div>
    </div>
    </body>
    </html>
    """
  )


@app.route("/register", methods=["GET", "POST"])
def register():
  error = None

  if request.method == "POST":
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()

    if not username.islower() or not username.isalnum():
      error = (
          "Tên tài khoản chỉ được phép viết chữ thường, không dấu, không khoảng"
          " trắng và không chứa ký tự đặc biệt (Ví dụ: bugnew)!"
      )
    elif username in users_db:
      error = "Tên tài khoản này đã tồn tại, vui lòng chọn tên khác!"
    elif len(password) < 6:
      error = "Mật khẩu phải có ít nhất 6 ký tự!"
    else:
      users_db[username] = password
      return redirect(
          url_for("login", success="Đăng ký thành công! Hãy đăng nhập ngay.")
      )

  return (
      """
    <!DOCTYPE html>
    <html lang="vi">
    <head>
    <title>ĐĂNG KÝ - BUG NEW</title>
    """
      + COMMON_STYLE
      + """
    </head>
    <body>
    <header>
        <h1>🛍️ SHOP BUG NEW 🛍️</h1>
        <p>📝 TẠO TÀI KHOẢN MỚI</p>
    </header>
    <div class="container" style="margin-top: 30px;">
        <div class="card">
            <h2>➕ ĐĂNG KÝ TÀI KHOẢN</h2>
            """
      + (f'<div class="error-msg">{error}</div>' if error else "")
      + """
            <form method="POST">
                <div class="form-group">
                    <label>Tên tài khoản (Chỉ viết thường, không dấu, không cách):</label>
                    <input type="text" name="username" class="form-control" placeholder="Ví dụ: bugnew" required>
                </div>
                <div class="form-group">
                    <label>Mật khẩu:</label>
                    <input type="password" name="password" class="form-control" placeholder="Ví dụ: bugnewff.01" required>
                </div>
                <button type="submit" class="btn">✨ ĐĂNG KÝ NGAY</button>
            </form>
            <div class="switch-link">
                Đã có tài khoản? <a href="/login">Đăng nhập ngay</a>
            </div>
        </div>
    </div>
    </body>
    </html>
    """
  )


@app.route("/logout")
def logout():
  session.pop("user", None)
  return redirect(url_for("login"))


@app.route("/")
def home():
  if "user" not in session:
    return redirect(url_for("login"))

  current_user = session["user"]

  return f"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DỊCH VỤ LIKES CỦA BUG NEW</title>
<style>
* {{ box-sizing: border-box; }}
body {{
    margin: 0;
    font-family: Arial, sans-serif;
    background: #080d19;
    color: white;
    scroll-behavior: smooth;
}}
header {{
    padding: 28px 15px;
    text-align: center;
    background: linear-gradient(135deg, #1d4ed8, #0284c7);
    position: relative;
}}
header h1 {{ margin: 0; font-size: 27px; font-weight: 900; }}
header p {{ margin-bottom: 0; color: #e0f2fe; }}
.user-badge {{
    position: absolute;
    top: 10px;
    right: 15px;
    background: rgba(0, 0, 0, 0.3);
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 13px;
    border: 1px solid rgba(255, 255, 255, 0.2);
}}
.user-badge a {{ color: #f87171; text-decoration: none; margin-left: 8px; font-weight: bold; }}
.container {{ max-width: 650px; margin: auto; padding: 20px 15px; }}
.intro {{ text-align: center; padding: 18px 5px; }}
.intro h2 {{ color: #38bdf8; font-size: 24px; }}
.intro p {{ color: #cbd5e1; line-height: 1.7; }}
.card {{
    background: #131d30;
    border: 1px solid #1e3a8a;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 18px;
}}
.card h2 {{ margin-top: 0; color: #38bdf8; font-size: 20px; }}
.price {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    padding: 15px 12px;
    margin: 10px 0;
    background: #1c2940;
    border-radius: 10px;
}}
.likes {{ font-weight: bold; }}
.money {{ color: #4ade80; font-weight: bold; white-space: nowrap; }}
.payment {{ color: #e2e8f0; line-height: 2; padding-left: 5px; }}
.note-box {{
    background: #0c4a6e;
    border: 1px solid #0284c7;
    color: #e0f2fe;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 18px;
    font-weight: bold;
    text-align: center;
    line-height: 1.6;
}}
.nav-acc-btn {{
    display: block;
    text-align: center;
    background: linear-gradient(135deg, #0284c7, #2563eb);
    color: white;
    padding: 15px;
    border-radius: 14px;
    font-size: 18px;
    font-weight: bold;
    text-decoration: none;
    margin-bottom: 25px;
    box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);
    transition: 0.3s;
}}
.nav-acc-btn:hover {{ background: linear-gradient(135deg, #0ea5e9, #3b82f6); }}
.acc-item {{
    background: #1c2940;
    border-radius: 12px;
    padding: 15px;
    margin-bottom: 20px;
    border: 1px solid #1e3a8a;
    transition: all 0.3s ease;
}}
.acc-item:hover {{
    transform: translateY(-4px);
    border-color: #38bdf8;
    box-shadow: 0 8px 20px rgba(56, 189, 248, 0.3);
}}
@keyframes button-pulse {{
    0% {{ transform: scale(1); }}
    50% {{ transform: scale(1.02); }}
    100% {{ transform: scale(1); }}
}}
.button {{
    display: block;
    text-align: center;
    margin-top: 12px;
    padding: 12px;
    background: #22c55e;
    color: #052e16;
    text-decoration: none;
    border-radius: 10px;
    font-weight: bold;
    animation: button-pulse 2s infinite ease-in-out;
    transition: background 0.3s;
}}
.button:hover {{ background: #86efac; }}
.contact {{
    text-align: center;
    padding: 25px 15px;
    background: linear-gradient(135deg, #082f49, #0369a1);
    border-radius: 16px;
}}
.contact h2 {{ color: #38bdf8; }}
.note {{ color: #cbd5e1; font-size: 13px; line-height: 1.6; }}
footer {{ text-align: center; padding: 25px 12px; color: #94a3b8; font-size: 13px; }}
</style>
</head>
<body>

<header>
    <div class="user-badge">
        👤 <b>{current_user}</b> | <a href="/logout">Đăng xuất</a>
    </div>
    <h1>🛍️ SHOP BUG NEW 🛍️</h1>
    <p>🎮 TẤT CẢ DỊCH VỤ GAME FF 🎮</p>
</header>

<div class="container">
    <section class="intro">
        <h2>🔥 DỊCH VỤ BUFF LIKES 🔥</h2>
        <p>
            💎 Bảng giá dịch vụ của BUG NEW<br>
            🛒 Chọn gói phù hợp với bạn<br>
            💬 Liên hệ Facebook để trao đổi và đặt dịch vụ!
        </p>
    </section>

    <div class="note-box">
        ❗ LƯU Ý: Mỗi ngày chỉ tối đa 220 likes / ngày!
    </div>

    <section class="card" style="text-align: center;">
        <h2 style="margin: 0; color: #38bdf8;">📋 BẢNG GIÁ BUFF LIKES</h2>
    </section>

    <section class="card">
        <h2>🏦 GIÁ CHUYỂN KHOẢN</h2>
        <div class="price"><span class="likes">👍 220 Likes</span><span class="money">2.000đ</span></div>
        <div class="price"><span class="likes">👍 1.100 Likes</span><span class="money">5.000đ</span></div>
        <div class="price"><span class="likes">👍 3.300 Likes</span><span class="money">10.000đ</span></div>
        <div class="price"><span class="likes">👍 8.800 Likes</span><span class="money">20.000đ</span></div>
    </section>

    <section class="card">
        <h2>💳 GIÁ THẺ ĐIỆN THOẠI (CARD)</h2>
        <div class="price"><span class="likes">👍 4.000 Likes</span><span class="money">20.000đ</span></div>
        <div class="price"><span class="likes">👍 10.000 Likes</span><span class="money">50.000đ</span></div>
    </section>

    <section class="card">
        <h2>🎮 GIÁ ĐỒ TRONG GAME</h2>
        <div class="price"><span class="likes">👍 2.000 Likes</span><span class="money">💎 &lt; 100</span></div>
        <div class="price"><span class="likes">👍 5.000 Likes</span><span class="money">💎 &lt; 200</span></div>
        <div class="price"><span class="likes">👍 10.000 Likes</span><span class="money">💎 &lt; 300</span></div>
    </section>

    <section class="card">
        <h2>💎 GIÁ NẠP KIM CƯƠNG</h2>
        <div class="price"><span class="likes">👍 1.000 Likes</span><span class="money">💎 25</span></div>
        <div class="price"><span class="likes">👍 2.000 Likes</span><span class="money">💎 51</span></div>
        <div class="price"><span class="likes">👍 5.000 Likes</span><span class="money">💎 113</span></div>
        <div class="price"><span class="likes">👍 12.000 Likes</span><span class="money">💎 283</span></div>
    </section>

    <a href="#kho-acc-section" class="nav-acc-btn">📦 XEM KHO ACC FREE FIRE (10 ACC)</a>

    <section class="card" id="kho-acc-section">
        <h2 style="text-align: center; font-size: 24px; color: #38bdf8;">🔥 KHO ACC FREE FIRE 🔥</h2>
        
        <div class="acc-item">
            <img src="https://i.postimg.cc/rwBsvfSm/Screenshot-20261102-174419-com-dts-freefireth.jpg" alt="Acc 1" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #1</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">⭐ <strong>Level:</strong> 34<br>🔐 <strong>Login:</strong> Facebook<br>💰 <strong>Giá:</strong> <strong style="color: #4ade80;">35.000đ</strong></p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <div class="acc-item">
            <img src="https://i.postimg.cc/3R7RwWS6/Screenshot-20261102-174720-com-dts-freefireth.jpg" alt="Acc 2" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #2</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">⭐ <strong>Level:</strong> 21<br>🔐 <strong>Login:</strong> Facebook<br>💰 <strong>Giá:</strong> <strong style="color: #4ade80;">20.000đ</strong></p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <div class="acc-item">
            <img src="https://i.postimg.cc/3NxxgVHC/Screenshot-20261102-174849-com-dts-freefireth.jpg" alt="Acc 3" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #3</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">⭐ <strong>Level:</strong> 18<br>🔐 <strong>Login:</strong> Facebook<br>💰 <strong>Giá:</strong> <strong style="color: #4ade80;">15.000đ</strong></p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <div class="acc-item">
            <img src="https://i.postimg.cc/rwfKhsvC/Screenshot-20261031-191554-com-dts-freefireth.jpg" alt="Acc 4" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #4</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">⭐ <strong>Level:</strong> 26<br>🔐 <strong>Login:</strong> Google<br>💰 <strong>Giá:</strong> <strong style="color: #4ade80;">15.000đ</strong></p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <div class="acc-item">
            <img src="https://i.postimg.cc/28cDMWSj/Screenshot-20261031-191815-com-dts-freefireth.jpg" alt="Acc 5" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #5</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">⭐ <strong>Level:</strong> 9<br>🔐 <strong>Login:</strong> Google<br>💰 <strong>Giá:</strong> <strong style="color: #4ade80;">36.000đ</strong></p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <div class="acc-item">
            <img src="https://i.postimg.cc/XqjRDNM8/Screenshot-20261031-191924-com-dts-freefireth.jpg" alt="Acc 6" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #6</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">⭐ <strong>Level:</strong> 13<br>🔐 <strong>Login:</strong> Google<br>💰 <strong>Giá:</strong> <strong style="color: #4ade80;">5.000đ</strong></p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <div class="acc-item">
            <img src="https://i.postimg.cc/ncwy0t3T/Screenshot-20261031-192021-com-dts-freefireth.jpg" alt="Acc 7" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #7</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">⭐ <strong>Level:</strong> 22<br>🔐 <strong>Login:</strong> Google<br>💰 <strong>Giá:</strong> <strong style="color: #4ade80;">20.000đ</strong></p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <div class="acc-item">
            <img src="https://i.postimg.cc/3w2z80YD/Screenshot-20261031-192143-com-dts-freefireth.jpg" alt="Acc 8" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #8</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">⭐ <strong>Level:</strong> 2<br>🔐 <strong>Login:</strong> Google<br>💰 <strong>Giá:</strong> <strong style="color: #4ade80;">25.000đ</strong></p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <div class="acc-item">
            <img src="https://i.postimg.cc/J4tgy2RD/Screenshot-20261031-192412-com-dts-freefireth.jpg" alt="Acc 9" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #9</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">⭐ <strong>Level:</strong> 28<br>🔐 <strong>Login:</strong> Facebook<br>💰 <strong>Giá:</strong> <strong style="color: #4ade80;">30.000đ</strong></p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <div class="acc-item">
            <img src="https://i.postimg.cc/JhCd27ZP/Screenshot-20261031-192920-com-dts-freefireth.jpg" alt="Acc 10" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #10</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">⭐ <strong>Level:</strong> 14<br>🔐 <strong>Login:</strong> Facebook<br>💰 <strong>Giá:</strong> <strong style="color: #4ade80;">10.000đ</strong></p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <div style="margin-top: 25px; padding-top: 15px; border-top: 1px dashed #1e3a8a;">
            <h3 style="color: #38bdf8; margin-bottom: 10px;">💳 Phương Thức Thanh Toán</h3>
            <div class="payment">🏦 Chuyển khoản<br>💳 Thẻ điện thoại (card)<br>💵 Tiền mặt<br>🎮 Đồ trong game<br>💎 Kim cương</div>
        </div>
    </section>

    <section class="contact">
        <h2>📩 MUA LIKES IB NHA!</h2>
        <p>👤 Facebook: <strong>Bug New</strong></p>
        <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank" rel="noopener noreferrer">💬 LIÊN HỆ FACEBOOK</a>
        <p class="note">Nhấn nút để mở Facebook, sau đó tìm tài khoản Bug New.</p>
    </sectio
