import cv2

face_referensi = cv2.CascadeClassifier("face_referensi.xml")
camera = cv2.VideoCapture(0)

def deteksi_wajah(frame):
    alat_pengoptimal = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    wajah = face_referensi.detectMultiScale(alat_pengoptimal, scaleFactor=1.1)
    return wajah

def menggambar_kotak_wajah(frame):
    for x, y, lebar, tinggi in deteksi_wajah(frame):
        cv2.rectangle(frame, (x, y), (x + lebar, y + tinggi), (255, 0, 0), thickness=4)

def menggambar_kotak_nama(frame, nama):
    for x, y, lebar, tinggi in deteksi_wajah(frame):
        # Hitung ukuran teks
        teks_size = cv2.getTextSize(nama, cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, thickness=4)[0]
        
        # Koordinat untuk sudut kanan bawah kotak
        x2 = x + teks_size[0] + 10  # Tambah padding di kanan
        y2 = y - teks_size[1] - 10   # Tambah padding di atas
        
        # Gambar kotak untuk nama


def keluar_program():
    camera.release()
    cv2.destroyAllWindows()
    exit()

def main():
    while True:
        nama = "HALLOO CANTTIIK"
        _, frame = camera.read()
        menggambar_kotak_wajah(frame)
        menggambar_kotak_nama(frame, nama)
        cv2.imshow("program face_detection", frame)
        if cv2.waitKey(1) & 0xFF == ord("l"):
            keluar_program()

if __name__ == "__main__":
    main()