import random
import tkinter as tk
from tkinter import messagebox, simpledialog

# Arkadaki gereksiz boş pencereyi gizliyoruz (sadece kutucuklar görünsün diye)
pencere = tk.Tk()
pencere.withdraw()

# 1. Bilgisayar rastgele bir sayı seçer ve hak tanımlanır
gizli_sayi = random.randint(1, 50)
hak = 5

messagebox.showinfo(
    "Oyun Başladı", "1 ile 50 arasında bir sayı tuttum. 5 hakkın var!"
)

# 2. Oyun döngüsü (Kullanıcı hakkı bitene kadar döner)
while hak > 0:
    # Kullanıcıdan ekranda açılan kutuyla girdi alıyoruz (input yerine)
    tahmin = simpledialog.askinteger(
        "Tahmin", f"Kalan Hak: {hak}\nTahminini yaz:"
    )

    # Kullanıcı çarpıya basarsa veya boş bırakırsa oyundan çıkar
    if tahmin is None:
        break

    # Girdiye göre farklı sonuçlar üretme kısmı
    if tahmin == gizli_sayi:
        messagebox.showinfo("Kazandın!", "Tebrikler, doğru sayıyı buldun! 🎉")
        break
    elif tahmin < gizli_sayi:
        messagebox.showwarning(
            "İpucu", "Daha BÜYÜK bir sayı söyle! (Yukarı ⬆)"
        )
    else:
        messagebox.showwarning(
            "İpucu", "Daha KÜÇÜK bir sayı söyle! (Aşağı ⬇)"
        )

    hak -= 1

# Hak bittiğinde doğru bilinmediyse
if hak == 0:
    messagebox.showerror(
        "Kaybettin", f"Hakkın bitti! Tuttuğum sayı: {gizli_sayi}"
    )
