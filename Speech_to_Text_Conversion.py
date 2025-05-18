import os
import speech_recognition as sr
from pydub import AudioSegment

r = sr.Recognizer()

wav_dosyasi = next((f for f in os.listdir() if f.endswith('.wav')), None)
mp3_dosyasi = next((f for f in os.listdir() if f.endswith('.mp3')), None)

ses_dosyasi = None
kullanicidan_al = True

if wav_dosyasi or mp3_dosyasi:
    print("\n🎧 Ses dosyası bulundu:")
    if wav_dosyasi:
        print(f"• WAV: {wav_dosyasi}")
    if mp3_dosyasi:
        print(f"• MP3: {mp3_dosyasi}")

    cevap = input("🎤 Konuşmak mı istiyorsun (K), yoksa ses dosyasını mı kullanmak (D)? [K/D]: ").strip().upper()
    if cevap == 'D':
        kullanicidan_al = False
        ses_dosyasi = wav_dosyasi if wav_dosyasi else mp3_dosyasi
else:
    print("\n⚠️ Ses dosyası bulunamadı, konuşmanı bekliyorum...")

if kullanicidan_al:
    with sr.Microphone() as source:
        print("🎙️ Konuş bakalım:")
        audio = r.listen(source)
else:
    if ses_dosyasi.endswith('.mp3'):
        sound = AudioSegment.from_mp3(ses_dosyasi)
        ses_dosyasi_wav = "ses.wav"
        sound.export(ses_dosyasi_wav, format="wav")
        ses_dosyasi = ses_dosyasi_wav
    
    with sr.AudioFile(ses_dosyasi) as source:
        audio = r.record(source)

try:
    sonuc = r.recognize_google(audio, language="tr-TR")
    print("\n🗣️ Dediniz: " + sonuc)
    
    # Metni dosyaya kaydet
    with open("ses.txt", "w", encoding="utf-8") as dosya:
        dosya.write(sonuc)
        print("📄 ses.txt dosyasına yazıldı.")

except sr.UnknownValueError:
    print("😕 Ne dediğini anlayamadım.")
except sr.RequestError as e:
    print(f"🔌 Google servisine ulaşılamadı: {e}")
