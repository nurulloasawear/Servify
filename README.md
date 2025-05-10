
---

````markdown
# Servify 🛠️

**Servify** — bu mijozlar va mutaxassislarni bog‘lovchi xizmatlar platformasi. Loyihada foydalanuvchilar xizmatlarga buyurtma berishi, ixtisoslashgan mutaxassislar bilan muloqot qilishi va to‘lovlarni amalga oshirishi mumkin.

---

## 🧩 Asosiy imkoniyatlar

- 🔐 Foydalanuvchi ro‘yxatdan o‘tishi va login bo‘lishi
- 🧑‍🔧 Mijozlar va mutaxassislar uchun alohida rollar
- 📍 Joylashuv bo‘yicha mutaxassis qidirish
- 💬 Xabarlar orqali aloqa (chat)
- 📅 Xizmatlar uchun jadval tuzish va bron qilish
- 🛒 Savatcha orqali xizmat tanlash
- 💳 To‘lov funksiyasi
- 📝 Fikr va reytinglar qoldirish
- 📈 Admin panel orqali monitoring

---

## ⚙️ Texnologiyalar

- Python / Django REST Framework
- PostgreSQL
- Redis (optional)
- JWT Authentication
- Swagger (drf-yasg)

---

## 🚀 O‘rnatish

1. Loyihani klon qiling:
   ```bash
   git clone https://github.com/nurulloasawear/Servify.git
   cd Servify
````

2. Virtual muhit yarating va faollashtiring:

   ```bash
   python -m venv env
   source env/bin/activate  # Windows uchun: env\Scripts\activate
   ```

3. Kerakli kutubxonalarni o‘rnating:

   ```bash
   pip install -r requirements.txt
   ```

4. Ma'lumotlar bazasini sozlang:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Superuser yarating:

   ```bash
   python manage.py createsuperuser
   ```

6. Serverni ishga tushuring:

   ```bash
   python manage.py runserver
   ```

---

## 📂 Loyihaning tarkibi

```
Servify/
├── api/
│   ├── users/
│   ├── services/
│   ├── location/
│   ├── ...
│   ├── permissions.py
│   └── urls.py
├── media/
├── myenv/
├── manage.py
├── requirements.txt
└── README.md
```

---

## 👥 Muallif

* [@nurulloasawear](https://github.com/nurulloasawear)

---

## 📜 Litsenziya

Ushbu loyiha [MIT License](LICENSE) ostida tarqatiladi.

---

