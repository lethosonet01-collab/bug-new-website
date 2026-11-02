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
* {
    box-sizing: border-box;
}

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

header h1 {
    margin: 0;
    font-size: 27px;
    font-weight: 900;
}

header p {
    margin-bottom: 0;
    color: #e0f2fe;
}

.container {
    max-width: 650px;
    margin: auto;
    padding: 20px 15px;
}

.intro {
    text-align: center;
    padding: 18px 5px;
}

.intro h2 {
    color: #38bdf8;
    font-size: 24px;
}

.intro p {
    color: #cbd5e1;
    line-height: 1.7;
}

.card {
    background: #131d30;
    border: 1px solid #1e3a8a;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 18px;
}

.card h2 {
    margin-top: 0;
    color: #38bdf8;
    font-size: 20px;
}

.price {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    padding: 15px 12px;
    margin: 10px 0;
    background: #1c2940;
    border-radius: 10px;
}

.likes {
    font-weight: bold;
}

.money {
    color: #4ade80;
    font-weight: bold;
    white-space: nowrap;
}

.payment {
    color: #e2e8f0;
    line-height: 2;
    padding-left: 5px;
}

.note-box {
    background: #0c4a6e;
    border: 1px solid #0284c7;
    color: #e0f2fe;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 18px;
    font-weight: bold;
    text-align: center;
    line-height: 1.6;
}

.nav-acc-btn {
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
}

.nav-acc-btn:hover {
    background: linear-gradient(135deg, #0ea5e9, #3b82f6);
}

/* HIỆU ỨNG ĐỘNG CHO KHUNG ACC & NÚT MUA */
.acc-item {
    background: #1c2940;
    border-radius: 12px;
    padding: 15px;
    margin-bottom: 20px;
    border: 1px solid #1e3a8a;
    transition: all 0.3s ease;
}

.acc-item:hover {
    transform: translateY(-4px);
    border-color: #38bdf8;
    box-shadow: 0 8px 20px rgba(56, 189, 248, 0.3);
}

@keyframes button-pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.02); }
    100% { transform: scale(1); }
}

.button {
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
}

.button:hover {
    background: #86efac;
}

.contact {
    text-align: center;
    padding: 25px 15px;
    background: linear-gradient(135deg, #082f49, #0369a1);
    border-radius: 16px;
}

.contact h2 {
    color: #38bdf8;
}

.note {
    color: #cbd5e1;
    font-size: 13px;
    line-height: 1.6;
}

footer {
    text-align: center;
    padding: 25px 12px;
    color: #94a3b8;
    font-size: 13px;
}
</style>
</head>

<body>

<header>
    <h1>🛍️ Shop BUG NEW 🛍️</h1>
    <p>🎮 DỊCH VỤ CỦA BUG NEW 🎮</p>
</header>

<div class="container">

    <section class="intro">
        <h2>📊 DỊCH VỤ BUFF LIKES ✅</h2>
        <p>
            💎 Bảng giá dịch vụ của BUG NEW<br>
            🛒 Chọn gói phù hợp với bạn<br>
            💬 Liên hệ Facebook để trao đổi và đặt dịch vụ!
        </p>
    </section>

    <!-- KHUNG LƯU Ý QUAN TRỌNG -->
    <div class="note-box">
        ❗ LƯU Ý: Chỉ nhận được 220 likes/ngày!
    </div>

    <!-- KHUNG TIÊU ĐỀ CHUNG -->
    <section class="card" style="text-align: center;">
        <h2 style="margin: 0; color: #38bdf8;">📋 BẢNG GIÁ BUFF LIKES</h2>
    </section>

    <!-- 1. GIÁ CHUYỂN KHOẢN -->
    <section class="card">
        <h2>🏦 GIÁ CHUYỂN KHOẢN</h2>
        <div class="price">
            <span class="likes">👍 220 Likes</span>
            <span class="money">2.000đ</span>
        </div>
        <div class="price">
            <span class="likes">👍 1.100 Likes</span>
            <span class="money">5.000đ</span>
        </div>
        <div class="price">
            <span class="likes">👍 3.300 Likes</span>
            <span class="money">10.000đ</span>
        </div>
        <div class="price">
            <span class="likes">👍 8.800 Likes</span>
            <span class="money">20.000đ</span>
        </div>
    </section>

    <!-- 2. GIÁ THẺ ĐIỆN THOẠI (CARD) -->
    <section class="card">
        <h2>💳 GIÁ THẺ ĐIỆN THOẠI (CARD)</h2>
        <div class="price">
            <span class="likes">👍 4.400 Likes</span>
            <span class="money">20.000đ</span>
        </div>
        <div class="price">
            <span class="likes">👍 11.000 Likes</span>
            <span class="money">50.000đ</span>
        </div>
    </section>

    <!-- 3. GIÁ ĐỒ TRONG GAME -->
    <section class="card">
        <h2>🎮 GIÁ ĐỒ TRONG GAME</h2>
        <div class="price">
            <span class="likes">👍 2.200 Likes</span>
            <span class="money">💎 &lt; 100</span>
        </div>
        <div class="price">
            <span class="likes">👍 5.500 Likes</span>
            <span class="money">💎 &lt; 200</span>
        </div>
        <div class="price">
            <span class="likes">👍 11.000 Likes</span>
            <span class="money">💎 &lt; 300</span>
        </div>
    </section>

    <!-- 4. GIÁ NẠP KIM CƯƠNG -->
    <section class="card">
        <h2>💎 GIÁ NẠP KIM CƯƠNG</h2>
        <div class="price">
            <span class="likes">👍 1.100 Likes</span>
            <span class="money">💎 25</span>
        </div>
        <div class="price">
            <span class="likes">👍 2.200 Likes</span>
            <span class="money">💎 51</span>
        </div>
        <div class="price">
            <span class="likes">👍 5.500 Likes</span>
            <span class="money">💎 113</span>
        </div>
        <div class="price">
            <span class="likes">👍 12.100 Likes</span>
            <span class="money">💎 283</span>
        </div>
    </section>

    <!-- NÚT BẤM ĐẾN KHO ACC FF -->
    <a href="#kho-acc-section" class="nav-acc-btn">📦 XEM KHO ACC FREE FIRE (10 ACC)</a>

    <!-- MỤC KHO ACC FREE FIRE (ĐỦ 10 ACC THỨ TỰ TỪ 1 ĐẾN 10) -->
    <section class="card" id="kho-acc-section">
        <h2 style="text-align: center; font-size: 24px; color: #38bdf8;">🔥 KHO ACC FREE FIRE 🔥</h2>
        
        <!-- ACC 1 -->
        <div class="acc-item">
            <img src="https://i.postimg.cc/rwBsvfSm/Screenshot-20261102-174419-com-dts-freefireth.jpg" alt="Acc FF 1" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #1</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">
                ⭐ <strong>Level:</strong> 34<br>
                🔐 <strong>Login:</strong> Facebook<br>
                💰 <strong>Giá:</strong> <strong style="color: #4ade80;">35.000đ</strong>
            </p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <!-- ACC 2 -->
        <div class="acc-item">
            <img src="https://i.postimg.cc/3R7RwWS6/Screenshot-20261102-174720-com-dts-freefireth.jpg" alt="Acc FF 2" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #2</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">
                ⭐ <strong>Level:</strong> 21<br>
                🔐 <strong>Login:</strong> Facebook<br>
                💰 <strong>Giá:</strong> <strong style="color: #4ade80;">20.000đ</strong>
            </p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <!-- ACC 3 -->
        <div class="acc-item">
            <img src="https://i.postimg.cc/3NxxgVHC/Screenshot-20261102-174849-com-dts-freefireth.jpg" alt="Acc FF 3" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #3</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">
                ⭐ <strong>Level:</strong> 18<br>
                🔐 <strong>Login:</strong> Facebook<br>
                💰 <strong>Giá:</strong> <strong style="color: #4ade80;">15.000đ</strong>
            </p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <!-- ACC 4 -->
        <div class="acc-item">
            <img src="https://i.postimg.cc/rwfKhsvC/Screenshot-20261031-191554-com-dts-freefireth.jpg" alt="Acc FF 4" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #4</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">
                ⭐ <strong>Level:</strong> 26<br>
                🔐 <strong>Login:</strong> Google<br>
                💰 <strong>Giá:</strong> <strong style="color: #4ade80;">15.000đ</strong>
            </p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <!-- ACC 5 -->
        <div class="acc-item">
            <img src="https://i.postimg.cc/28cDMWSj/Screenshot-20261031-191815-com-dts-freefireth.jpg" alt="Acc FF 5" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #5</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">
                ⭐ <strong>Level:</strong> 9<br>
                🔐 <strong>Login:</strong> Google<br>
                💰 <strong>Giá:</strong> <strong style="color: #4ade80;">36.000đ</strong>
            </p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <!-- ACC 6 -->
        <div class="acc-item">
            <img src="https://i.postimg.cc/XqjRDNM8/Screenshot-20261031-191924-com-dts-freefireth.jpg" alt="Acc FF 6" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #6</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">
                ⭐ <strong>Level:</strong> 13<br>
                🔐 <strong>Login:</strong> Google<br>
                💰 <strong>Giá:</strong> <strong style="color: #4ade80;">5.000đ</strong>
            </p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <!-- ACC 7 -->
        <div class="acc-item">
            <img src="https://i.postimg.cc/ncwy0t3T/Screenshot-20261031-192021-com-dts-freefireth.jpg" alt="Acc FF 7" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #7</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">
                ⭐ <strong>Level:</strong> 22<br>
                🔐 <strong>Login:</strong> Google<br>
                💰 <strong>Giá:</strong> <strong style="color: #4ade80;">20.000đ</strong>
            </p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <!-- ACC 8 -->
        <div class="acc-item">
            <img src="https://i.postimg.cc/3w2z80YD/Screenshot-20261031-192143-com-dts-freefireth.jpg" alt="Acc FF 8" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #8</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">
                ⭐ <strong>Level:</strong> 2<br>
                🔐 <strong>Login:</strong> Google<br>
                💰 <strong>Giá:</strong> <strong style="color: #4ade80;">25.000đ</strong>
            </p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <!-- ACC 9 -->
        <div class="acc-item">
            <img src="https://i.postimg.cc/J4tgy2RD/Screenshot-20261031-192412-com-dts-freefireth.jpg" alt="Acc FF 9" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #9</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">
                ⭐ <strong>Level:</strong> 28<br>
                🔐 <strong>Login:</strong> Facebook<br>
                💰 <strong>Giá:</strong> <strong style="color: #4ade80;">30.000đ</strong>
            </p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <!-- ACC 10 -->
        <div class="acc-item">
            <img src="https://i.postimg.cc/JhCd27ZP/Screenshot-20261031-192920-com-dts-freefireth.jpg" alt="Acc FF 10" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
            <h3 style="color: #38bdf8; margin: 5px 0;">🎮 Acc #10</h3>
            <p style="color: #cbd5e1; font-size: 14px; line-height: 1.6; margin: 5px 0;">
                ⭐ <strong>Level:</strong> 14<br>
                🔐 <strong>Login:</strong> Facebook<br>
                💰 <strong>Giá:</strong> <strong style="color: #4ade80;">10.000đ</strong>
            </p>
            <a class="button" href="https://www.facebook.com/share/1DWZpYDE4C/" target="_blank">🛒 MUA NGAY</a>
        </div>

        <!-- PHƯƠNG THỨC THANH TOÁN Ở DƯỚI CÙNG MỤC ACC -->
        <div style="margin-top: 25px; padding-top: 15px; border-top: 1px dashed #1e3a8a;">
            <h3 style="color: #38bdf8; margin-bottom: 10px;">💳 Phương Thức Thanh Toán</h3>
            <div class="payment">
                🏦 Chuyển khoản<br>
                💳 Thẻ điện thoại (card)<br>
                💵 Tiền mặt<br>
                🎮 Đồ trong game<br>
                💎 Kim cương
            </div>
        </div>
    </section>

    <section class="contact">
        <h2>📩 MUA LIKES IB FB NHA!</h2>
        <p>👤 Facebook: <strong>Bug New</strong></p>

        <a class="button"
           href="https://www.facebook.com/share/1DWZpYDE4C/"
           target="_blank"
           rel="noopener noreferrer">
           💬 LIÊN HỆ FACEBOOK
        </a>

        <p class="note">
            Nhấn nút để mở Facebook, sau đó tìm tài khoản Bug New.
        </p>
    </section>

</div>

<footer>
    🔰 © 2026 Bug New | DỊCH VỤ LIKES & ACC 🔰
</footer>

<!-- 🌟 BUG NEW BLUE CYBERPUNK EFFECTS -->
<div id="blue-effects" aria-hidden="true">
    <div class="floating-bubble bubble-one">💎</div>
    <div class="floating-bubble bubble-two">🔹</div>
    <div class="blue-glow"></div>
    <canvas id="blue-particles"></canvas>
</div>

<style>
#blue-effects {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 9998;
    overflow: hidden;
}

.floating-bubble {
    position: absolute;
    font-size: 28px;
    animation: bubble-float 5s ease-in-out infinite;
    filter: drop-shadow(0 0 10px #38bdf8);
}

.bubble-one {
    bottom: 20px;
    left: 20px;
    animation-duration: 4s;
}

.bubble-two {
    bottom: 40px;
    right: 20px;
    animation-duration: 5.5s;
}

.blue-glow {
    position: absolute;
    bottom: 0;
    left: -10%;
    width: 120%;
    height: 60px;
    opacity: .25;
    background: linear-gradient(
        0deg,
        rgba(2, 132, 199, .4),
        rgba(56, 189, 248, .1),
        transparent
    );
    animation: blue-glow-pulse 3s ease-in-out infinite alternate;
}

#blue-particles {
    width: 100%;
    height: 100%;
    display: block;
}

@keyframes bubble-float {
    0%, 100% { transform: translateY(0) scale(1); }
    50% { transform: translateY(-15px) scale(1.1); }
}

@keyframes blue-glow-pulse {
    from { opacity: .15; }
    to { opacity: .35; }
}

@media (prefers-reduced-motion: reduce) {
    #blue-effects *,
    #blue-effects {
        animation: none !important;
    }
}
</style>

<script>
(() => {
    const canvas = document.getElementById("blue-particles");
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let width = 0;
    let height = 0;
    let particles = [];
    let frame = null;
    let running = false;

    const reducedMotion = window.matchMedia(
        "(prefers-reduced-motion: reduce)"
    );

    function resize() {
        const dpr = Math.min(window.devicePixelRatio || 1, 2);

        width = window.innerWidth;
        height = window.innerHeight;

        canvas.width = width * dpr;
        canvas.height = height * dpr;
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

        const count = width < 600 ? 20 : 40;

        particles = Array.from({ length: count }, () => ({
            x: Math.random() * width,
            y: Math.random() * height,
            size: Math.random() * 2.5 + 0.8,
            speed: Math.random() * 0.8 + 0.3,
            drift: Math.random() * 0.5 - 0.25,
            phase: Math.random() * Math.PI * 2,
            color: Math.random() > 0.4 ? "#38bdf8" : "#818cf8"
        }));
    }

    function draw() {
        if (!running) return;

        ctx.clearRect(0, 0, width, height);

        for (const p of particles) {
            p.phase += 0.03;
            p.y -= p.speed;
            p.x += p.drift + Math.sin(p.phase) * 0.4;

            if (p.y < -10) {
                p.y = height + 10;
                p.x = Math.random() * width;
            }

            if (p.x < 0) p.x = width;
            if (p.x > width) p.x = 0;

            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            ctx.fillStyle = p.color;
            ctx.globalAlpha = 0.7;
            ctx.shadowBlur = 10;
            ctx.shadowColor = p.color;
            ctx.fill();
        }

        ctx.globalAlpha = 1;
        ctx.shadowBlur = 0;
        frame = requestAnimationFrame(draw);
    }

    function start() {
        if (running || reducedMotion.matches || document.hidden) return;
        running = true;
        draw();
    }

    function stop() {
        running = false;
        if (frame !== null) cancelAnimationFrame(frame);
        frame = null;
    }

    resize();
    start();

    window.addEventListener("resize", resize);

    document.addEventListener("visibilitychange", () => {
        if (document.hidden) stop();
        else start();
    });

    reducedMotion.addEventListener("change", () => {
        if (reducedMotion.matches) stop();
        else start();
    });
})();
</script>

</body>
</html>
"""

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
  
