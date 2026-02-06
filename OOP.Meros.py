# class AVTO:
#     def __init__(self , rusumi , nomi , rangi , yili , narxi ,  yonilgi_sarfi):
#         self.rusumi = rusumi
#         self.nomi = nomi
#         self.color = rangi
#         self.data = yili
#         self.price = narxi
#         self.benzin = yonilgi_sarfi

#     def get_info(self):
#         return f"Mashina rusumi: {self.rusumi}\nMashina nomi {self.nomi}\nMashina rangi {self.color} \nMashina ishlab chiqarilgan sanasi {self.data} \nMashina narxi {self.price}"

# class Mersedes(AVTO) :
#     def __init__(self, rusumi, nomi, rangi, yili, narxi, mator_kuchi , clas , porshn ,):
#         super().__init__(rusumi, nomi, rangi, yili, narxi)

#         self.ot_kuchi = mator_kuchi
#         self.clas = clas
#         self.porshn = porshn
        
#     def get_car_info(self):
#         return f"Mashina rusumi: {self.rusumi}\nMashina nomi {self.nomi}\nMashina rangi {self.color} \nMashina ishlab chiqarilgan sanasi {self.data} \nMashina narxi {self.price} \nMashina {self.clas}classga mansub \nMashina {self.porshn}porshinli \nMashina {self.ot_kuchi}ta ot kuchiga ega \nMashina 100 km ga o'rtacha {self.benzin} litr sarflaydi "

# class Damas(AVTO):
#     def __init__(self, rusumi, nomi, rangi, yili, narxi, yonilgi_sarfi ,labo , van ):
#         super().__init__(rusumi, nomi, rangi, yili, narxi, yonilgi_sarfi)

#         self.labo = labo
#         self.van = van
        

#     def get_labo(self):
#         if self.labo :
#             return f"labo"

#         elif self.van :
#             return "van"
#         else:
#             return "damaz"

# car = Mersedes("Mercedes-AMG G63 " , "Gelik" , "qora" , 2025 , 130000 ,  585  , "G" , 4 , 13-15)
# damaz = Damas('Chevrolet' , "damaz" , "oq" , 2026 , 8000 , 7-8 , False  , False )
# print(car.get_car_info())
# print(damaz.get_labo())


# class Hayvon:
#     def __init__(self , zoti , narxi , rangi  , ismi):
        
#         self.zoti = zoti
#         self.narxi  = narxi
#         self.rangi = rangi
#         self.ismi = ismi

#     def get_info(self):
#         return f"Zoti :{self.zoti} \nRangi :{self.rangi} \nIsmi :{self.ismi} \nNarxi :{self.narxi}"
# class Mushuk(Hayvon):
#     def __init__(self, zoti, narxi, rangi, ismi , ov_qobilyati):
#         super().__init__(zoti, narxi, rangi, ismi)
    
#         self.ovchi = ov_qobilyati

#     def cat_info(self):
#         return f"Ovqilish qobilyati {self.ovchi} \n{self.get_info()}"

# class It(Hayvon):
#     def __init__(self, zoti, narxi, rangi, ismi , harbiy_it):
#         super().__init__(zoti, narxi, rangi, ismi)
#         self.harbiy = harbiy_it

#     def get_data(self):
#         return f"Harbiy it bo'lishga munosiblik darajasi {self.harbiy}\n{self.get_info()}"

# kuchuk = It("Alabai" , 400 , "oq" , "simba" , "To'g'ri kelmaydi")
# pishak = Mushuk("Nebelung" , 1200 , "To'q kulrang" , "Bezbet" , "yaxshi rivojlanmagan")

# print(kuchuk.get_data())
# print(pishak.cat_info())


# class Avto:
#     def __init__(self , rusumi , nomi , narxi , rangi  ):
#         self.rusumi = rusumi
#         self.nomi = nomi
#         self.narxi = narxi
#         self.color = rangi

#     def get_info(self) :
#         return f"Mashina rusumi {self.rusumi}\nMashina nomi {self.nomi} \nMashina narxi {self.narxi} \nMashina rangi {self.color}"

# class bola(Avto) :
#     def __init__(self, rusumi, nomi, narxi, rangi):
#         super().__init__(rusumi, nomi, narxi, rangi)
#     def get_data(self) :
#         return self.get_info()

# mashina = bola("Chevrolet" , "Captiva" , 20000 , "qora")
# print(mashina.get_data())


# class Talaba:
#     def __init__(self , universitet_nomi , diplom_darajasi  ,   talaba_ismi , talaba_id ):
#         self.name = universitet_nomi
#         self.level = diplom_darajasi
#         self.talaba_name = talaba_ismi
#         self.id = talaba_id

#     def get_info(self):
#         return f"Universitet nomi {self.name} \nDiplom darajasi {self.level} \nTalaba ismi {self.talaba_name} \nTalabani id raqami {self.id}"
    

# class Bakalavr(Talaba):
#     def __init__(self, universitet_nomi, diplom_darajasi, talaba_ismi, talaba_id , oqish_davri , kurs , yonalishi):
#         super().__init__(universitet_nomi, diplom_darajasi, talaba_ismi, talaba_id)
#         self.yil = oqish_davri
#         self.kurs = kurs 
#         self.yonalishi = yonalishi
#     def get_bakalavr_info(self):
#         return f"{self.get_info()}\nO'qish muddati {self.yil}\nTalaba {self.kurs} da o'qiydi\nTalabani yo'nalishi {self.yonalishi}da "



# class Magistir(Talaba):
#     def __init__(self, universitet_nomi, diplom_darajasi, talaba_ismi, talaba_id , mutaxasisligi):
#         super().__init__(universitet_nomi, diplom_darajasi, talaba_ismi, talaba_id)
#         self.mutaxasis = mutaxasisligi
#     def get_magistir_info(self):
#         return f"{self.get_info()}\nTalabani mutaxasisligi {self.mutaxasis}" 

# talaba1= Bakalavr("Renesans" , "Oliy" , 'Yoqubboy' , 1564516855 , 4  , 3 ," suniy intelyekt")
# talaba2 = Magistir("TATU" , "Oliy" , "Ulug'bek" , 1525562235 ," Back-end developer")
# print(talaba1.get_bakalavr_info())


# class Ustoz:
#     def __init__(self , toifa , fan , sinif_rahbari  ):
#         self.toifa = toifa
#         self.fan = fan 
#         self.sinf = sinif_rahbari

#     def get_info(self):
#         return f"Toifa {self.toifa} \n O'qtuvchi dars beradigan fani {self.fan} \nO'qtuvchi sinf rahbari {self.sinf} \n"
    
# class Informatika_ustoz(Ustoz):
#     def __init__(self, toifa, fan, sinif_rahbari , dars_oluvchi_sinflar  ):
#         super().__init__(toifa, fan, sinif_rahbari)
#         self.sinflar = dars_oluvchi_sinflar
    
#     def get_ustoz(self):
#         return f"{self.get_info()} Faqatgina {self.sinflar} dars oladi"

# sarvar_ustoz = Informatika_ustoz("orta" , "informatika" , "sinf rahbari" , "5 dan 11 gacha")

# print(sarvar_ustoz.get_ustoz())


# class Texnika:
#     def __init__(self , materiali , sifati , kafolati , narxi ):
#         self.materiali = materiali
#         self.sifati = sifati
#         self.garantiya = kafolati
#         self.narxi = narxi

#     def get_info(self):
#         return f"Mahsulot materiali {self.materiali} \nSifati {self.sifati} \nKafolat mudati {self.garantiya} \nMahsulot narxi {self.narxi} $\n"
    
# class Kampiyuter(Texnika):
#     def __init__(self, materiali, sifati, kafolati, narxi , ekrani , prosessori , yangilanish_tezligi):
#         super().__init__(materiali, sifati, kafolati, narxi)

#         self.ekrani  = ekrani
#         self.prosessori = prosessori
#         self.tezligi  = yangilanish_tezligi

#     def get_kampiyuter(self):
#         return f"{self.get_info()}Ekrani {self.ekrani}  \nProsesori {self.prosessori} \nYangilanish tezligi {self.tezligi}Gerz"

# laptoop = Kampiyuter("Silver metalic" , "a'lo" , "3 yil" , 480 , 15.6 , "intel core I7 " , 144  )
# print(laptoop.get_kampiyuter())

# class Shaxs:
#     def __init__(self , ismi , familiyasi , yoshi ):
#         self.ismi = ismi
#         self.familyasi = familiyasi
#         self.yoshi = yoshi

    
#     def info(self):
#         return f"Ismi {self.ismi} \nFamilyasi {self.familyasi} \nYoshi {self.yoshi} "

# class Ustoz(Shaxs):
#     def __init__(self, ismi, familiyasi, yoshi,  fani , darslar_soati , toifasi ):
#         super().__init__(ismi, familiyasi, yoshi, )
#         self.fan = fani
#         self.daslari = darslar_soati
#         self.toifa = toifasi

#     def get_info(self):
#         return f"{self.info()}\nO'qituvchi dars beradigan fani {self.fan} \nDarslar soati {self.daslari} soat \nO'qituvchi darajasi {self.toifa}"

# teacher = Ustoz("Ulug'bek" , "Yarashboyev" , 36 , "jismoniy tarbiya" ,  25  , "o'rta")

# print(teacher.get_info())


# class Mashina:
#     def __init__(self , yuk_sigimi , odam_sigimi , baq_sigimi , zaxira_shinalari ,  ot_kuchi):
#         self.yuk = yuk_sigimi
#         self.odam = odam_sigimi
#         self.baq = baq_sigimi
#         self.zaxira_balon = zaxira_shinalari
#         self.mator = ot_kuchi

#     def info(self):
#         return f"Yuk ko'tarish sig'imi {self.yuk} tonna \nMashinaga {self.odam} ta odam sig'adi\nMashinani baqiga {self.baq} Litr yonilg'i sig'adi\nMashinada zaxira balonlari {self.zaxira_balon} ta\nMashina matori {self.mator} ot kuchiga ega"
    
# class Yukmashina(Mashina):
#     def __init__(self, yuk_sigimi, odam_sigimi, baq_sigimi, zaxira_shinalari, ot_kuchi , butilishi_darajasi ):
#         super().__init__(yuk_sigimi, odam_sigimi, baq_sigimi, zaxira_shinalari, ot_kuchi)
#         self.burilish = butilishi_darajasi

#     def get_info(self):
#         return f"{self.info()}\nYuk mashinasi builish darajasi {self.burilish} gradus"
    
# fura = Yukmashina(25 , 2 , 200 , 3 , 400 , 45 )
# print(fura.get_info())



# class Uchuvchi:
#     def __init__(self , ismi , yoshi , biladigan_tillari):
#         self.ismi = ismi
#         self.yoshi = yoshi
#         self.tili = biladigan_tillari

#     def info(self):
#         return f"uchuvchi ismi {self.ismi} \nYoshi {self.yoshi} \nMuloqot qilaoladigan tillari {self.tili}"
# class harbiy_uchuvchi(Uchuvchi):
#     def __init__(self, ismi, yoshi, biladigan_tillari , nishinga_olish_qobilyati , toponcha_ishlatabilish , ishlata_oladigna_qurollar_soni):
#         super().__init__(ismi, yoshi, biladigan_tillari)
#         self.nishon = nishinga_olish_qobilyati
#         self.toponcha = toponcha_ishlatabilish
#         self.qurol_ishlatish = ishlata_oladigna_qurollar_soni
#     def get(self):
#         return f"{self.info()}\nUchuvchi havoda o'qqa tutish qobilyati {self.nishon} \nUchuvchi topponchadan foydalanishni {self.toponcha} \nUchuvchi {self.qurol_ishlatish} ta quroldan foydalanishni biladi"

# pro = harbiy_uchuvchi("Ulug'bek" , 27 , "Ingiliz , rus , O'zbek " , "aniq" , "kuchli" , 9)
# print(pro.get())


# class Hayvon:
#     def __init__(self , nomi ):
#         self.nomi = nomi
   
#     def info(self):
#         print(f"Unig nomi {self.nomi} \n")

# class It(Hayvon):
#     def __init__(self, nomi , it):
#         super().__init__( nomi, )
#         self.it = it

#     def Dog_info(self):
#         print(f"{self.info()} It bunday ovoz chiqaradi{self.it}")     

# class Mushuk(Hayvon):
#     def __init__(self,  nomi, mushuk ):
#         super().__init__( nomi, )
#         self.mushuk = mushuk

#     def Cat_info(self):
#         return f"{self.info} mushuk bunday ovoz chiqaradi {self.mushuk}"

# bobik = It('bobik' , 'vov')
# bezbet = Mushuk("bezbet" , 'miau')

# print(bezbet.Cat_info())



# class Texnika :
#     def __init__(self ,nomi ,  xotira , batareya , prosesori ):
#         self.nomi = nomi 
#         self.xotira = xotira
#         self.batareya = batareya
#         self.prosesor = prosesori

#     def get_info(self):
#         return f"Bu {self.nomi } \nXotirasi {self.xotira}GB\nBatareyasi {self.batareya}\nProsesori {self.prosesor}\n"


# class Telefon(Texnika):
#     def __init__(self, nomi, xotira, batareya, prosesori , kamerasi ):
#         super().__init__(nomi, xotira, batareya, prosesori)
#         self.kamera = kamerasi

#     def phone_info(self):
#         return f"{self.get_info()}Telefonni kamerasi {self.kamera} MP"

# class Noutbuk(Texnika):
#     def __init__(self, nomi, xotira, batareya, prosesori , ekran_dyumi):
#         super().__init__(nomi, xotira, batareya, prosesori)
#         self.ekran = ekran_dyumi

#     def notebook_info(self):
#         return f"{self.get_info()}Notebookni ekrani o'lchami {self.ekran}"
    
# redmi = Telefon("Xiomi 17 pro max" , 256 , 6500 , "Snapdregon 8 Elite gen 5" , 108  )
# lenovo = Noutbuk("Lenovo Ipad slim " , 512 , "4 soatga yetadi" , "Intel Core I7 " , 15.8)
# print(lenovo.notebook_info())


class Kompaniya:
    def __init__(self , ish_vaqti , ishlab_chiqariluvchi_mahsulot , daromad):
        self.ishvaqti = ish_vaqti
        self.mahsulot = ishlab_chiqariluvchi_mahsulot
        self.daromad = daromad

    def get_Kampaniya(self):
        return f"Kampaniya {self.ishvaqti} gacha ishlaydi.\nishlab chiqariluvchi mahsulot {self.mahsulot}\nKampaniya daromadi {self.daromad}\n"

class Ishchi(Kompaniya):
    def __init__(self, ish_vaqti, ishlab_chiqariluvchi_mahsulot, daromad , ish_bolimi , smena):
        super().__init__(ish_vaqti, ishlab_chiqariluvchi_mahsulot, daromad)
        self.ishbolimi = ish_bolimi
        self.smena  = smena

    def 








class Shaxs:
#     def __init__(self, ismi , yoshi , ishlashjoyi):
#         self.name = ismi
#         self.age = yoshi
#         self.work = ishlashjoyi

#     def get_info(self):
#         return f"Ismi {self.name} \nYoshi {self.age}\nIsh joyi {self.work}"
    
# class Talaba(Shaxs):
#     def __init__(self, ismi, yoshi, ishlashjoyi , oqish_vaqti ):
#         super().__init__(ismi, yoshi, ishlashjoyi)
#         self.vaqti = oqish_vaqti

#     def info(self):
#         return f"{self.get_info()}\nO'qish vaqti {self.vaqti}"
    
# class Ustoz(Shaxs):
#     def __init__(self, ismi, yoshi, ishlashjoyi , darslari_vaqti , malumot_darajasi):
#         super().__init__(ismi, yoshi, ishlashjoyi)
#         self.darslar = darslari_vaqti
#         self.malumot = malumot_darajasi

#     def teacher_info(self):
#         return f"{self.get_info()}\nDarslari jami vaqti {self.darslar}\nMalumot darajasi {self.malumot}"

# odam = Ustoz("Odilbek" , "45 yosh" , "20-sonli maktab" , 20 , "o'rta")
          
# print(odam.teacher_info())





























