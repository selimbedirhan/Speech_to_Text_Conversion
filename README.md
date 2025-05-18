### 📄 `README.md`

````markdown
# 🎤 Speech to Text (Ses Tanıma ve Metne Dönüştürme)

Bu Python projesi, **mikrofondan konuşmayı** veya **.mp3/.wav ses dosyalarını** tanıyarak **Türkçe metne dönüştürür** ve sonucu bir dosyaya (`ses.txt`) kaydeder.

## 🚀 Özellikler

- 🎙️ Mikrofonla ses kaydı yapabilir
- 🎧 Var olan `.mp3` veya `.wav` dosyasını metne dönüştürebilir
- 📝 Çıktıyı `ses.txt` dosyasına kaydeder
- 🇹🇷 Türkçe dil desteği ile Google Speech Recognition kullanır

## 🧰 Gereksinimler

Aşağıdaki kütüphanelerin kurulu olması gerekir:

```bash
pip install SpeechRecognition
pip install pydub
pip install pyaudio
````

Ayrıca `.mp3` dosyalarını `.wav` formatına çevirmek için `ffmpeg` kurulu olmalıdır:

**Mac:**

```bash
brew install ffmpeg
```

**Windows:**

FFmpeg'i indirip sistem PATH'ine ekleyin: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

## 📂 Kullanım

1. `Speech_to_Text_Conversion.py` dosyasını çalıştır:

```bash
python Speech_to_Text_Conversion.py
```

2. Eğer klasörde `.mp3` veya `.wav` dosyası varsa, sana şu soruyu sorar:

```
🎤 Konuşmak mı istiyorsun (K), yoksa ses dosyasını mı kullanmak (D)? [K/D]:
```

3. Mikrofonla konuşmak istersen `K`, dosyayı kullanmak istersen `D` yaz.

4. İşlem bittikten sonra, tanınan metin ekrana yazdırılır ve `ses.txt` dosyasına kaydedilir.

## 📁 Örnek Dosya Yapısı

```
Speech_to_Text_Conversion/
├── ses.mp3
├── Speech_to_Text_Conversion.py
└── ses.txt
```

## 🔐 Notlar

* Çevrimde Google’ın ücretsiz Speech API’si kullanılır. Aktif internet bağlantısı gerekir.
* Çok büyük ses dosyalarında Google API sınırlamalarına dikkat edilmelidir.

## 👨‍💻 Geliştirici

Selim Bedirhan Öztürk
💼 Ankara Üniversitesi – Bilgisayar Mühendisliği
