
from PyQt6.QtWidgets import *

class GirisEkrani(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Uygulama Giriş Ekranı')
        self.setFixedSize(250,200)

        di_cerceve = QVBoxLayout()
        yi1 = QHBoxLayout()

        yi1_di1 = QVBoxLayout()
        yi1_di1.addWidget(QLabel("Kullanıcı adı"))
        yi1_di1.addWidget(QLabel("Şifresi"))

        yi1_di2 = QVBoxLayout()
        self.kullanici_adi = QLineEdit()
        # self.kullanici_adi.textChanged.connect(self.kontrol1) 
        yi1_di2.addWidget(self.kullanici_adi)

        self.sifre = QLineEdit()
        yi1_di2.addWidget(self.sifre)
       
        yi2 = QHBoxLayout()
        dugme1 = QPushButton("Giriş yap")
        yi2.addWidget(dugme1)
        dugme1.clicked.connect(self.giris_kontrol)  # düğme 1 e bastığında bu sınıftaki (self dediğimizde bu sınıfın fonksiyonu diyoruz) giris_kontrol fonksiyonu çalışsın.
        
        dugme2 = QPushButton("Vazgeç")
        yi2.addWidget(dugme2)
        dugme2.clicked.connect(self.vazgec)

        yi1.addLayout(yi1_di1)
        yi1.addLayout(yi1_di2)

        yi3 = QHBoxLayout()
        self.function_menu = QComboBox()
        self.function_menu.addItems(["Uygulama Seçiniz:", "İnç/Cm Dönüştürme Uygulaması", "VKİ Uygulaması"])
        self.function_menu.currentIndexChanged.connect(self.fonksiyon_sec)
        yi3.addWidget(self.function_menu)
        
        di_cerceve.addLayout(yi1)
        di_cerceve.addLayout(yi2)
        di_cerceve.addLayout(yi3)

        pencere = QWidget()
        pencere.setLayout(di_cerceve)
        self.setCentralWidget(pencere)
       
    def giris_kontrol(self):
        
        dka = "admin"
        dsf = "1234"

        ka = self.kullanici_adi.text().strip()
        sf = self.sifre.text().strip()
      
        if dka != ka and dsf != sf :
            print("Kullanıcı adı ve şifre hatalı.")     
        elif dka != ka and dsf == sf :
            print("Kullanıcı adı hatalı.")          
        elif dka == ka and dsf != sf :
            print("Şifre hatalı.")
        else:
           # print("Yetki var, giriş başarılı.")
            a = QMessageBox(self)
            a.setWindowTitle("Giriş Başarılı")
            a.setText("Sisteme başarıyla giriş yapıldı.")
            a.exec()
                            
        # giris_hakki = 5
        # while giris_hakki > 0:

        #     ka = self.kullanici_adi.text().strip()
        #     sf = self.sifre.text().strip()

        #     if dka == ka and dsf == sf :
        #         # print("Yetki var, giriş başarılı.")
        #         a = QMessageBox(self)
        #         a.setWindowTitle("Giriş Başarılı")
        #         a.setText("Sisteme başarıyla giriş yapıldı.")
        #         a.exec()
        #         break
            
        #     else:

        #         if dka != ka and dsf != sf :
        #             print(f"Kullanıcı adı ve şifre hatalı. Kalan giriş hakkınız: {giris_hakki}")
        #             giris_hakki -= 1
        #         elif dka != ka and dsf == sf :
        #             print(f"Kullanıcı adı hatalı.Kalan giriş hakkınız: {giris_hakki}")
        #             giris_hakki -= 1
        #         elif dka == ka and dsf != sf :
        #             print(f"Şifre hatalı.Kalan giriş hakkınız: {giris_hakki}")
        #             giris_hakki -= 1
        #         if (giris_hakki == 0):
        #             print("Giriş hakkınız bitmiştir.")
        #             break     
           
            
    def vazgec(self):
        print("vazgeç düğmesine tıklandı.")
        aaa = QMessageBox(self)
        # aaa.setWindowTitle("Aman Dikkat")
        aaa.setText("Vazgeç düğmesine tıkladınız.")
        aaa.exec()
    
    def fonksiyon_indeksAta(self):
        self.setWindowTitle('Uygulama Giriş Ekranı')
        self.password_label.setText('Kullanıcı adı:')
        self.password_label.setText('Şifresi:')
        self.login_button.setText('Giriş Yap')
        self.function_menu.setItemText(0, "Fonksiyon Seçin")
        self.function_menu.setItemText(1, "İnç/Cm Dönüştürme Uygulaması")
        self.function_menu.setItemText(2, "VKİ Uygulaması")

    def fonksiyon_sec(self, index):
        if index == 1:
            self.inc_donusturme_uyg()
        elif index == 2:
            self.vki_uyg()
        self.function_menu.setCurrentIndex(0)
    
    def inc_donusturme_uyg(self):
        self.birim_donusturme_penceresi = birim_donusturme()
        self.birim_donusturme_penceresi.show()
        self.close()
          
    def vki_uyg(self):
        self.vki_uygulama_penceresi =VKIUygulamasi()
        self.vki_uygulama_penceresi.show()
        self.close()

class birim_donusturme(QWidget):
    def __init__(self):
        super().__init__()
        self.birim_donustur()

    def birim_donustur(self):
        self.setWindowTitle("İnç - Cm Dönüştürme Uygulaması")
        inc_cm_di1 = QVBoxLayout()

        inc_etiket = QLabel("Dönüştürme Tipi:")
        inc_cm_di1.addWidget(inc_etiket)

        self.donusumTipi = QComboBox()
        self.donusumTipi.addItems(["İnçten CM'ye","CM'den İnçe"])
        # self.donusumTipi.addItem("CM'den İnçe" )
        inc_cm_di1.addWidget(self.donusumTipi)
       
        inc_cm_di1.addWidget(QLabel("Değer girin:"))
        self.deger = QLineEdit()
        inc_cm_di1.addWidget(self.deger)
        
        self.donustur_dugmesi = QPushButton('Dönüştür')
        self.donustur_dugmesi.clicked.connect(self.inc_cm_donustur)
        inc_cm_di1.addWidget(self.donustur_dugmesi)
        
        self.inc_bilgi = QLabel()
        inc_cm_di1.addWidget(self.inc_bilgi)

        self.inc_sonuc = QLabel()
        inc_cm_di1.addWidget(self.inc_sonuc)

        self.setLayout(inc_cm_di1)
        self.inc_bilgi_guncelle()

        self.donusumTipi.currentIndexChanged.connect(self.inc_bilgi_guncelle)

    def inc_cm_donustur(self):
        try:
            deger = float(self.deger.text())
            if self.donusumTipi.currentText() == ("İnçten CM'ye"):
                sonuc = deger * 2.54
                self.inc_sonuc.setText(f"Sonuç:\n{deger} inç {sonuc:.2f} cm'dir.")
            else:
                sonuc = deger / 2.54
                self.inc_sonuc.setText(f"Sonuç:\n{deger} cm {sonuc:.2f} inçtir.")
        except ValueError:
            QMessageBox.warning(self, '', 'Lütfen geçerli bir sayı girin.')
        
        self.deger.clear()

        # self.name_input.clear()
        # self.phone_input.clear()

    def inc_bilgi_guncelle(self):
        if self.donusumTipi.currentText() == ("İnçten CM'ye"):
            self.inc_bilgi.setText("1 inç 2.54 cm'dir.\n")
        else:
            self.inc_bilgi.setText("1 cm 0.3937 inçtir.\n")

    # def inc_bilgi_guncelle(self):
    #     self.inc_bilgi.setText("Bilgi:\n1 inç 2.54 cm'dir.\n1 cm 0.3937 inçtir.\n")
       
       
class VKIUygulamasi(QWidget):
    
    def __init__(self):
        super().__init__()
        self.vki_hesapla()

    def vki_hesapla(self):
        self.setWindowTitle("VKİ Uygulaması")
        vki_di1 = QVBoxLayout()
       
        vki_etiket = QLabel("VÜCUT KİTLE İNDEKSİ HESAPLAMA")
        vki_etiket.setStyleSheet("border: 1px double black; color: black; font-size:20px; background: white")
        vki_di1.addWidget(vki_etiket)
        vki_di1.addWidget(QLabel("Kilonuz(kg):"))
        self.kilo = QLineEdit()
        vki_di1.addWidget(self.kilo)
        
        vki_di1.addWidget(QLabel("Boyunuz(cm):"))
        self.boy = QLineEdit()
        vki_di1.addWidget(self.boy)

        self.hesaplaDugmesi = QPushButton('Hesapla')
        self.hesaplaDugmesi.clicked.connect(self.vki_hesaplama)
        vki_di1.addWidget(self.hesaplaDugmesi)
        
        self.vki_bilgi = QLabel()
        vki_di1.addWidget(self.vki_bilgi)

        self.vki_sonuc = QLabel()
        vki_di1.addWidget(self.vki_sonuc)

        self.setLayout(vki_di1)
        self.vki_bilgi_guncelle()

        # self.converter_type.currentIndexChanged.connect(self.update_info_label)

    def vki_hesaplama(self):
        try:
            vki = float(self.kilo.text()) / (float(self.boy.text())/100)**2
            if vki < 18.5:
                self.vki_sonuc.setText(f"VKi: {vki:.2f} kg/m², Zayıf")
            elif vki >= 18.5 and vki <= 24.9:
                self.vki_sonuc.setText(f"VKİ: {vki:.2f} kg/m², Sağlıklı")
            elif vki <= 25 and vki <= 29.9:
                self.vki_sonuc.setText(f"VKi: {vki:.2f} kg/m², Şişman")
            elif vki >= 30 and vki <= 39.9:
                self.vki_sonuc.setText(f"VKi: {vki:.2f} kg/m², Obez")
            else:
                self.vki_sonuc.setText(f"VKİ: {vki:.2f} kg/m², Aşırı Obez")
        except ValueError:
            QMessageBox.warning(self, '', 'Lütfen geçerli bir sayı girin.')
        
        self.kilo.clear()
        self.boy.clear()

    def vki_bilgi_guncelle(self):
       self.vki_bilgi.setText("18, 5 kg/m² ‘nin altındaki sonuçlar: Zayıf\n18, 5 kg/m² ile 24, 9 kg/m² arasındaki sonuçlar: Sağlıklı\n25 kg/m² ile 29, 9 kg/m² arasındaki sonuçlar: Şişman\n30 kg/m² ile 39, 9 kg/m² arasındaki sonuçlar: Obez\n40 kg/m² üzerindeki sonuçlar: Aşırı obez.")




















aa = QApplication([])
pencere = GirisEkrani()
pencere.show()

aa.exec()