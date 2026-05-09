import datetime


# 1. Taomlar klassi
class Taom:
    def __init__(self, nomi, narxi):
        self.nomi = nomi
        self.narxi = narxi

    def __str__(self):
        return f"{self.nomi:15} | {self.narxi} so'm"


# 2. Buyurtma va To'lov klassi
class Buyurtma:
    def __init__(self, id):
        self.id = id
        self.savat = []
        self.vaqt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def qoshish(self, taom):
        self.savat.append(taom)
        print(f"✅ {taom.nomi} savatga qo'shildi.")

    def jami(self):
        return sum(t.narxi for t in self.savat)


# 3. Asosiy Restoran tizimi
class RestoranTizimi:
    def __init__(self):
        # Menyu (Buni o'zgartirishingiz mumkin)
        self.menyu = [
            Taom("Osh", 35000),
            Taom("Shashlik", 15000),
            Taom("Manti", 30000),
            Taom("Choy", 5000)
        ]
        self.tarix_fayli = "tarix.txt"

    def menyuni_korsat(self):
        print("\n--- RESTORAN MENYUSI ---")
        for i, taom in enumerate(self.menyu, 1):
            print(f"{i}. {taom}")

    def tarixga_yozish(self, buyurtma):
        with open(self.tarix_fayli, "a", encoding="utf-8") as f:
            f.write(f"ID: {buyurtma.id} | Vaqt: {buyurtma.vaqt} | Jami: {buyurtma.jami()} so'm\n")

    def ishga_tushirish(self):
        buyurtma_id = 1
        while True:
            print("\n1. Menyu | 2. Buyurtma berish | 3. Tarixni ko'rish | 4. Chiqish")
            tanlov = input("Amalni tanlang: ")

            if tanlov == "1":
                self.menyuni_korsat()

            elif tanlov == "2":
                yangi_buyurtma = Buyurtma(buyurtma_id)
                self.menyuni_korsat()
                while True:
                    t_raqam = input("Taom raqamini kiriting (Tugatish uchun '0'): ")
                    if t_raqam == "0": break
                    try:
                        tanlangan = self.menyu[int(t_raqam) - 1]
                        yangi_buyurtma.qoshish(tanlangan)
                    except:
                        print("❌ Xato raqam kiritdingiz!")

                if yangi_buyurtma.savat:
                    print(f"\nJami hisob: {yangi_buyurtma.jami()} so'm")
                    self.tarixga_yozish(yangi_buyurtma)
                    buyurtma_id += 1
                    print("💰 To'lov saqlandi va tarixga yozildi.")

            elif tanlov == "3":
                print("\n--- SOTUVLAR TARIXI ---")
                try:
                    with open(self.tarix_fayli, "r", encoding="utf-8") as f:
                        print(f.read())
                except:
                    print("Tarix hali bo'sh.")

            elif tanlov == "4":
                print("Dastur yopildi. Xayr!")
                break


# Dasturni yurgizish
if __name__ == "__main__":
    app = RestoranTizimi()
    app.ishga_tushirish()
