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
}

header {
    padding: 28px 15px;
    text-align: center;
    background: linear-gradient(135deg, #6d28d9, #0891b2);
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
    color: #67e8f9;
    font-size: 24px;
}

.intro p {
    color: #cbd5e1;
    line-height: 1.7;
}

.card {
    background: #131d30;
    border: 1px solid #26354e;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 18px;
}

.card h2 {
    margin-top: 0;
    color: #67e8f9;
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
    background: #1e1b4b;
    border: 1px solid #7c3aed;
    color: #f3e8ff;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 18px;
    font-weight: bold;
    text-align: center;
    line-height: 1.6;
}

.contact {
    text-align: center;
    padding: 25px 15px;
    background: linear-gradient(135deg, #172554, #164e63);
    border-radius: 16px;
}

.contact h2 {
    color: #67e8f9;
}

.button {
    display: inline-block;
    margin-top: 10px;
    padding: 13px 24px;
    background: #22c55e;
    color: #052e16;
    text-decoration: none;
    border-radius: 10px;
    font-weight: bold;
}

.button:hover {
    background: #86efac;
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
    <h1>⚡ BUG NEW ⚡</h1>
    <p>🎮 DỊCH VỤ CỦA BUG NEW 🎮</p>
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

    <!-- KHUNG LƯU Ý QUAN TRỌNG -->
    <div class="note-box">
        ❗ LƯU Ý: Mỗi ngày chỉ nhận tối đa 220 likes / ngày!
    </div>

    <!-- KHUNG TIÊU ĐỀ CHUNG -->
    <section class="card" style="text-align: center;">
        <h2 style="margin: 0; color: #67e8f9;">📋 BẢNG GIÁ BUFF LIKES</h2>
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
            <span class="likes">👍 4.000 Likes</span>
            <span class="money">20.000đ</span>
        </div>
        <div class="price">
            <span class="likes">👍 10.000 Likes</span>
            <span class="money">50.000đ</span>
        </div>
    </section>

    <!-- 3. GIÁ ĐỒ TRONG GAME -->
    <section class="card">
        <h2>🎮 GIÁ ĐỒ TRONG GAME</h2>
        <div class="price">
            <span class="likes">👍 2.000 Likes</span>
            <span class="money">💎 &lt; 100</span>
        </div>
        <div class="price">
            <span class="likes">👍 5.000 Likes</span>
            <span class="money">💎 &lt; 200</span>
        </div>
        <div class="price">
            <span class="likes">👍 10.000 Likes</span>
            <span class="money">💎 &lt; 300</span>
        </div>
    </section>

    <!-- 4. GIÁ NẠP KIM CƯƠNG -->
    <section class="card">
        <h2>💎 GIÁ NẠP KIM CƯƠNG</h2>
        <div class="price">
            <span class="likes">👍 1.000 Likes</span>
            <span class="money">💎 25</span>
        </div>
        <div class="price">
            <span class="likes">👍 2.000 Likes</span>
            <span class="money">💎 51</span>
        </div>
        <div class="price">
            <span class="likes">👍 5.000 Likes</span>
            <span class="money">💎 113</span>
        </div>
        <div class="price">
            <span class="likes">👍 12.000 Likes</span>
            <span class="money">💎 283</span>
        </div>
    </section>

    <section class="card">
        <h2>💸 PHƯƠNG THỨC THANH TOÁN</h2>
        <div class="payment">
            🏦 Chuyển khoản<br>
            💳 Thẻ điện thoại (card)<br>
            💵 Tiền mặt<br>
            🎮 Đồ trong game<br>
            💎 Kim cương
        </div>
    </section>

    <section class="contact">
        <h2>📩 MUA LIKES IB NHA!</h2>
        <p>👤 Facebook: <strong>Bug New</strong></p>

        <a class="button"
           href="https://www.facebook.com/"
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
    ⚡ © 2026 BUG NEW | DỊCH VỤ CỦA BUG NEW ⚡
</footer>

<!-- 🎃 BUG NEW HALLOWEEN EFFECTS -->
<div id="halloween-effects" aria-hidden="true">
    <div class="spider-web web-left">🕸️</div>
    <div class="spider-web web-right">🕸️</div>
    <div class="floating-pumpkin">🎃</div>
    <div class="floating-ghost ghost-one">👻</div>
    <div class="floating-ghost ghost-two">👻</div>
    <div class="flying-bat bat-one">🦇</div>
    <div class="flying-bat bat-two">🦇</div>
    <div class="halloween-fog"></div>
    <canvas id="halloween-particles"></canvas>
</div>

<style>
#halloween-effects {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 9998;
    overflow: hidden;
}

.spider-web {
    position: absolute;
    top: 0;
    font-size: 65px;
    opacity: .5;
    filter: drop-shadow(0 0 8px #a855f7);
    animation: web-glow 3s ease-in-out infinite alternate;
}

.web-left { left: 0; }
.web-right { right: 0; transform: scaleX(-1); }

.floating-pumpkin {
    position: absolute;
    right: 24px;
    bottom: 100px;
    font-size: 42px;
    animation: pumpkin-float 3s ease-in-out infinite;
    filter: drop-shadow(0 0 12px #ff7300);
}

.floating-ghost {
    position: absolute;
    font-size: 32px;
    opacity: .8;
    filter: drop-shadow(0 0 10px #c084fc);
    animation: ghost-float 7s ease-in-out infinite;
}

.ghost-one {
    top: 28%;
    left: -50px;
    animation-name: ghost-cross;
    animation-duration: 22s;
}

.ghost-two {
    top: 65%;
    right: -50px;
    animation-name: ghost-cross-reverse;
    animation-duration: 27s;
}

.flying-bat {
    position: absolute;
    font-size: 27px;
    filter: drop-shadow(0 0 6px #a855f7);
}

.bat-one {
    top: 18%;
    left: -50px;
    animation: bat-fly 16s linear infinite;
}

.bat-two {
    top: 45%;
    left: -50px;
    animation: bat-fly 23s linear infinite 5s;
}

.halloween-fog {
    position: absolute;
    bottom: 0;
    left: -20%;
    width: 140%;
    height: 75px;
    opacity: .3;
    background: linear-gradient(
        0deg,
        rgba(124, 58, 237, .35),
        rgba(249, 115, 22, .12),
        transparent
    );
    animation: fog-move 8s ease-in-out infinite alternate;
}

#halloween-particles {
    width: 100%;
    height: 100%;
    display: block;
}

@keyframes pumpkin-float {
    0%, 100% { transform: translateY(0) rotate(-8deg); }
    50% { transform: translateY(-18px) rotate(8deg); }
}

@keyframes ghost-float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-25px); }
}

@keyframes ghost-cross {
    0% { left: -60px; transform: translateY(0) rotate(-8deg); }
    50% { transform: translateY(-35px) rotate(8deg); }
    100% { left: calc(100% + 60px); transform: translateY(0); }
}

@keyframes ghost-cross-reverse {
    0% { right: -60px; transform: translateY(0) rotate(8deg); }
    50% { transform: translateY(25px) rotate(-8deg); }
    100% { right: calc(100% + 60px); transform: translateY(0); }
}

@keyframes bat-fly {
    0% { left: -50px; transform: translateY(0) scale(1); }
    25% { transform: translateY(-35px) scale(.8); }
    50% { transform: translateY(15px) scale(1.1); }
    75% { transform: translateY(-25px) scale(.9); }
    100% { left: calc(100% + 50px); transform: translateY(0) scale(1); }
}

@keyframes web-glow {
    from { opacity: .3; }
    to { opacity: .7; }
}

@keyframes fog-move {
    from { transform: translateX(-5%); }
    to { transform: translateX(5%); }
}

@media (prefers-reduced-motion: reduce) {
    #halloween-effects *,
    #halloween-effects {
        animation: none !important;
    }
}
</style>

<script>
(() => {
    const canvas = document.getElementById("halloween-particles");
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

        const count = width < 600 ? 22 : 45;

        particles = Array.from({ length: count }, () => ({
            x: Math.random() * width,
            y: Math.random() * height,
            size: Math.random() * 3 + 1,
            speed: Math.random() * .7 + .2,
            drift: Math.random() * .6 - .3,
            phase: Math.random() * Math.PI * 2,
            color: Math.random() > .5 ? "#fb923c" : "#c084fc"
        }));
    }

    function draw() {
        if (!running) return;

        ctx.clearRect(0, 0, width, height);

        for (const p of particles) {
            p.phase += .025;
            p.y -= p.speed;
            p.x += p.drift + Math.sin(p.phase) * .35;

            if (p.y < -10) {
                p.y = height + 10;
                p.x = Math.random() * width;
            }

            if (p.x < 0) p.x = width;
            if (p.x > width) p.x = 0;

            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            ctx.fillStyle = p.color;
            ctx.globalAlpha = .65;
            ctx.shadowBlur = 12;
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
  
