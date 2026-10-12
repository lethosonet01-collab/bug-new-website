from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
  return """
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DỊCH VỤ LIKES CỦA BUG NEW</title>
<style>
* { box-sizing: border-box; }
body { margin: 0; font-family: Arial, sans-serif; background: #080d19; color: white; }
header { padding: 28px 15px; text-align: center; background: linear-gradient(135deg, #6d28d9, #0891b2); }
header h1 { margin: 0; font-size: 27px; font-weight: 900; }
header p { margin-bottom: 0; color: #e0f2fe; }
.container { max-width: 650px; margin: auto; padding: 20px 15px; }
.intro { text-align: center; padding: 18px 5px; }
.intro h2 { color: #67e8f9; font-size: 24px; }
.intro p { color: #cbd5e1; line-height: 1.7; }
.card { background: #131d30; border: 1px solid #26354e; border-radius: 16px; padding: 20px; margin-bottom: 18px; }
.card h2 { margin-top: 0; color: #67e8f9; font-size: 20px; }
.price { display: flex; justify-content: space-between; align-items: center; gap: 10px; padding: 15px 12px; margin: 10px 0; background: #1c2940; border-radius: 10px; }
.likes { font-weight: bold; }
.money { color: #4ade80; font-weight: bold; white-space: nowrap; }
.payment { color: #e2e8f0; line-height: 2; padding-left: 5px; }
.contact { text-align: center; padding: 25px 15px; background: linear-gradient(135deg, #172554, #164e63); border-radius: 16px; }
.contact h2 { color: #67e8f9; }
.button { display: inline-block; margin-top: 10px; padding: 13px 24px; background: #22c55e; color: #052e16; text-decoration: none; border-radius: 10px; font-weight: bold; }
.note { color: #cbd5e1; font-size: 13px; line-height: 1.6; }
footer { text-align: center; padding: 25px 12px; color: #94a3b8; font-size: 13px; }
</style>
</head>
<body>
<header>
    <h1>⚡ BUG NEW ⚡</h1>
    <p>🎮 DỊCH VỤ CỦA BUG NEW 🎮</p>
</header>
<div class="container">
    <section class="intro">
        <h2>🔥 DỊCH VỤ BUFF LIKES 🔥</h2>
        <p>💎 Bảng giá dịch vụ của BUG NEW<br>🛒 Chọn gói phù hợp với bạn<br>💬 Liên hệ Facebook để trao đổi và đặt dịch vụ!</p>
    </section>
    <section class="card">
        <h2>📋 BẢNG GIÁ BUFF LIKES</h2>
        <div class="price"><span class="likes">👍 220 Likes</span><span class="money">2.000đ</span></div>
        <div class="price"><span class="likes">👍 1.100 Likes</span><span class="money">5.000đ</span></div>
        <div class="price"><span class="likes">👍 3.300 Likes</span><span class="money">10.000đ</span></div>
        <div class="price"><span class="likes">👍 8.800 Likes</span><span class="money">20.000đ</span></div>
    </section>
    <section class="card">
        <h2>💳 PHƯƠNG THỨC THANH TOÁN</h2>
        <div class="payment">🏦 Chuyển khoản<br>💳 Thẻ điện thoại (card)<br>💵 Tiền mặt<br>🎮 Đồ trong game<br>💎 Kim cương</div>
    </section>
    <section class="contact">
        <h2>📩 MUA LIKES IB NHA!</h2>
        <p>👤 Facebook: <strong>Bug New</strong></p>
        <a class="button" href="https://www.facebook.com/" target="_blank" rel="noopener noreferrer">💬 LIÊN HỆ FACEBOOK</a>
        <p class="note">Nhấn nút để mở Facebook, sau đó tìm tài khoản Bug New.</p>
    </section>
</div>
<footer>
    ⚡ © 2026 BUG NEW | DỊCH VỤ CỦA BUG NEW ⚡
</footer>
</body>
</html>
"""


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
  
