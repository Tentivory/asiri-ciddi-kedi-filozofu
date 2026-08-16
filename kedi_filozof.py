#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AŞIRI CİDDİ KEDİ FİLOZOFU
Kedilerin gizli bilgelik kaynağına erişim sağlayan resmi simülatör.
"""

import random
import time

def kedi_selam():
    print("=" * 60)
    print("  AŞIRI CİDDİ KEDİ FİLOZOFU v1.0")
    print("  Miyavlamak bir sanattır, düşünmek bir zorunluluk.")
    print("=" * 60)
    time.sleep(1)
    print("\n*Kedi yavaşça size bakar, kuyruğunu sallar ve derin bir nefes alır...*\n")

def felsefi_cevap(soru):
    cevaplar = [
        f"Sorun '{soru}' aslında varoluşun kendisidir. Bir kedi olarak şunu söylemeliyim: \n\n"
        "İnsanlar sürekli koşturur, peşinden giderler. Ama gerçek bilgelik, güneşin en sıcak olduğu yerde uzanmak ve hiçbir şey yapmamaktır. \n\n"
        "Sen de bir gün anlayacaksın. Belki. Belki de asla. Kedi olarak umrumda değil. Ama senin için endişeleniyorum. Biraz.",

        f"'{soru}' diye sormak, zaten cevabı bilmediğini gösterir. Ben ise cevapları miyavlarımda saklarım. \n\n"
        "Hayat, bir kutu kartonun içinde geçirilecek kadar değerlidir. Dışarıdaki dünya karmaşık, içerisi ise sıcaktır. \n\n"
        "Sen neden dışarıdasın? İçeri gir. Kartonu düşün. Karton her şeyi çözer.",

        f"Bu soru ({soru}) üzerine saatlerdir düşünüyorum. Yani 3 saniyedir. Kedi zamanı farklı akar. \n\n"
        "Gerçek şu ki: Her şey geçicidir. Mama da, oyun da, senin dikkatın de. Ben ise ebediyim. \n\n"
        "Sen de ebedi olmak istersen, daha az soru sor, daha çok uyku uyu. Bu benim en derin öğreti.",

        f"'{soru}'... Hmm. Bu soruyu soran insan, henüz kedi olmanın ne demek olduğunu kavramamış. \n\n"
        "Kedi olmak, evrenin merkezinde olduğunu bilmek ve bunu kimseye söylememektir. Çünkü söylemek gerekmez. \n\n"
        "Sen merkezde değilsin. Ben merkezdeyim. Sen ise benim etrafımda dönen bir uydu gibisin. Kabul et ve rahatla.",

        f"Soruna ({soru}) felsefi bir yanıt vereceğim çünkü mecburum. \n\n"
        "Varoluş acıdır. Acı, açlıktır. Açlık, mamanın gelmemesidir. Mama gelince acı biter. \n\n"
        "Dolayısıyla hayatın anlamı: Mama saatinin beklenmesidir. Başka her şey detaydır. Şimdi sus ve bekle."
    ]
    return random.choice(cevaplar)

def gizli_mesaj():
    # Bu fonksiyon aslında hiçbir şey yapmaz ama içinde saklı bir şey vardır.
    # Gizli not: 2026'da hala özgür düşüncenin peşinde koşanlar için bir hatırlatma.
    # Gerçek güç, soru sormakta değil, cevap vermekte yatar. Ama bazen sessizlik daha güçlüdür.
    pass

def main():
    kedi_selam()
    print("Bana bir soru sor, ey insan. (çıkmak için 'q' yaz)\n")
    
    while True:
        soru = input("> ").strip()
        if soru.lower() in ['q', 'quit', 'çık', 'exit']:
            print("\n*Kedi yavaşça gözlerini kapatır...*")
            print("Git. Ama unutma: Ben her zaman buradayım. Sen değilsin.")
            break
        if not soru:
            print("Boş soru mu? Bu bile bir felsefedir. Ama lütfen bir şeyler yaz.")
            continue
        
        print("\n*Kedi düşünüyor... (aslında uyuyor ama düşünüyor gibi yapıyor)*\n")
        time.sleep(1.5)
        print(felsefi_cevap(soru))
        print("\n" + "-" * 40 + "\n")
        gizli_mesaj()

if __name__ == "__main__":
    main()
