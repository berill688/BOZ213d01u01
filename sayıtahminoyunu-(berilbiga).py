import os
import random
import webbrowser

# Bilgisayar 1-50 arası sayı seçer
gizli_sayi = random.randint(1, 50)

# Tarayıcıda açılacak web sayfası tasarımı ve oyun mantığı (JavaScript)
html_icerik = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Sayı Avcısı Web Oyunu</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f6f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }}
        .kutu {{
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            text-align: center;
            max-width: 400px;
            width: 100%;
        }}
        h2 {{ color: #2c3e50; }}
        input {{
            font-size: 18px;
            padding: 8px;
            width: 80px;
            text-align: center;
            margin: 10px 0;
        }}
        button {{
            padding: 10px 20px;
            font-size: 16px;
            background-color: #27ae60;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }}
        button:hover {{ background-color: #219150; }}
        #mesaj {{ font-size: 16px; font-weight: bold; margin-top: 15px; }}
        .hak {{ color: #7f8c8d; font-size: 14px; margin-top: 5px; }}
    </style>
</head>
<body>

<div class="kutu">
    <h2>🎯 Sayı Avcısı</h2>
    <p>1 ile 50 arasında bir sayı tuttum!</p>
    
    <input type="number" id="tahminInput" min="1" max="50" placeholder="Sayı">
    <br>
    <button onclick="tahminEt()">Tahmin Et</button>
    
    <div id="mesaj"></div>
    <div class="hak" id="hakYazisi">Kalan Hak: 5</div>
</div>

<script>
    let gizliSayi = {gizli_sayi};
    let hak = 5;

    function tahminEt() {{
        let girdi = document.getElementById("tahminInput").value;
        let mesajAlani = document.getElementById("mesaj");
        let hakAlani = document.getElementById("hakYazisi");

        if (!girdi) {{
            mesajAlani.innerHTML = "<span style='color:orange;'>Lütfen bir sayı girin!</span>";
            return;
        }}

        let tahmin = parseInt(girdi);
        hak--;

        if (tahmin === gizliSayi) {{
            mesajAlani.innerHTML = "<span style='color:green;'>🎉 Tebrikler! Doğru bildin!</span>";
            bitir();
        }} else if (hak === 0) {{
            mesajAlani.innerHTML = "<span style='color:red;'>💥 Hakkın bitti! Sayı: " + gizliSayi + " idi.</span>";
            bitir();
        }} else if (tahmin < gizliSayi) {{
            mesajAlani.innerHTML = "<span style='color:#2980b9;'>⬆️️ Daha BÜYÜK bir sayı gir!</span>";
        }} else {{
            mesajAlani.innerHTML = "<span style='color:#d35400;'>⬇️ Daha KÜÇÜK bir sayı gir!</span>";
        }}

        hakAlani.innerText = "Kalan Hak: " + hak;
        document.getElementById("tahminInput").value = "";
    }}

    function bitir() {{
        document.getElementById("tahminInput").disabled = true;
        document.querySelector("button").disabled = true;
    }}
</script>

</body>
</html>
"""

# HTML dosyasını oluştur ve tarayıcıda otomatik aç
dosya_adi = "oyun.html"
with open(dosya_adi, "w", encoding="utf-8") as f:
    f.write(html_icerik)

webbrowser.open("file://" + os.path.realpath(dosya_adi))
