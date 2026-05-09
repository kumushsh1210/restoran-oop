import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO


class RestoranOnlineRasmlar:
    def __init__(self, root):
        self.root = root
        self.root.title("Gourmet Restoran v4.5")
        self.root.geometry("900x650")
        self.root.configure(bg="#f0f2f5")

        # Taomlar va ularning internetdagi rasmlari
        self.menu_data = [
            {"nomi": "Palov", "narxi": 35000, "link": "https://freepik.com"},
            {"nomi": "Manti", "narxi": 30000, "link": "https://freepik.com"},
            {"nomi": "Shashlik", "narxi": 18000, "link": "https://freepik.com"},
            {"nomi": "Choy", "narxi": 5000, "link": "https://freepik.com"}
        ]

        self.savat = []
        self.interfeys_qurish()

    def rasm_yuklash(self, url):
        try:
            response = requests.get(url)
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img = img.resize((180, 140))
            return ImageTk.PhotoImage(img)
        except:
            return None

    def interfeys_qurish(self):
        tk.Label(self.root, text="🇺🇿 MILLIY TAOMLAR MENYUSI", font=("Helvetica", 24, "bold"), bg="#f0f2f5").pack(
            pady=20)

        main_frame = tk.Frame(self.root, bg="#f0f2f5")
        main_frame.pack(pady=10)

        self.img_list = []  # Xotirada saqlash uchun

        for i, taom in enumerate(self.menu_data):
            card = tk.Frame(main_frame, bg="white", bd=1, relief="ridge", padx=10, pady=10)
            card.grid(row=0, column=i, padx=15)

            # Internetdan rasmni olish
            photo = self.rasm_yuklash(taom["link"])
            if photo:
                lbl = tk.Label(card, image=photo, bg="white")
                lbl.pack()
                self.img_list.append(photo)

            tk.Label(card, text=taom["nomi"], font=("Arial", 14, "bold"), bg="white").pack(pady=5)
            tk.Label(card, text=f"{taom['narxi']} so'm", fg="#2ecc71", font=("Arial", 12), bg="white").pack()

            tk.Button(card, text="Savatga qo'shish", bg="#3498db", fg="white", font=("Arial", 10, "bold"),
                      command=lambda t=taom: self.savatga_qosh(t)).pack(pady=10)

        self.btn_buyurtma = tk.Button(self.root, text="🛒 BUYURTMA BERISH (0 ta)", font=("Arial", 16, "bold"),
                                      bg="#e67e22", fg="white", width=30, height=2, command=self.yakunlash)
        self.btn_buyurtma.pack(pady=30)

    def savatga_qosh(self, taom):
        self.savat.append(taom)
        self.btn_buyurtma.config(text=f"🛒 BUYURTMA BERISH ({len(self.savat)} ta)")

    def yakunlash(self):
        if not self.savat:
            messagebox.showwarning("Bo'sh!", "Savatga hali hech narsa qo'shmadingiz.")
            return

        jami = sum(t["narxi"] for t in self.savat)
        messagebox.showinfo("Muvaffaqiyatli", f"Buyurtmangiz qabul qilindi!\nJami summa: {jami} so'm")
        self.savat = []
        self.btn_buyurtma.config(text="🛒 BUYURTMA BERISH (0 ta)")


if __name__ == "__main__":
    root = tk.Tk()
    app = RestoranOnlineRasmlar(root)
    root.mainloop()
