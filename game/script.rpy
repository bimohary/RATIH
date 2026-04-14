# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg blck = im.Scale ("images/ISTAROTH.png", config.screen_width, config.screen_height)

# Deklarasikan karakter yang digunakan di game.
define a = Character('Ayah Ratih', color="#c8ffc8")
define r = Character('Ratih', color="#c8ffc8")
define i = Character('Ibu Ratih', color="#c8ffc8")
define s = Character('Santika', color="#c8ffc8")
define k = Character('Kayla', color="#c8ffc8")
define d = Character('Danedra', color="#004304")
define b = Character('Bellina', color="#c8ffc8")
define u = Character('Monster Id', color="#c8ffc8")
define p = Character('Monster Superego', color="#c8ffc8")
define e = Character('Bellina (Ego)', color="#c8ffc8")
define l = Character('Lunabell (Ego Baru)', color="#c8ffc8")
define g = Character('Guru', color='#c8ffc8')

# Game dimulai disini:
# Deklarasi video sebagai sebuah image
label splashscreen:
    scene black
    show movie
    $ renpy.movie_cutscene("cyrene1.webm")
    return

label start:

    scene bg blck with dissolve
    a "Wah, anakku benar-benar sangat cantik."

    "Saat Ratih berumur 9 Tahun dan ia sedang menonton sebuah drama di TV"

    "Ratih pun terkagum dan ingin menjadi seorang aktris seperti artis yang memainkan peran di sebuah drama"

    "Sejak itu, Ratih pun menyukai bernyanyi dan bermain peran dan ia pun menganggap apa yang dia lakukan itu adalah hobinya"
    
    "Ah, dia hanya beruntung saja dapat peran utama berkat kecantikan dia tapi cara berakting tuh b aja banget nggak sih ?!"
    scene teater
    "Di saat sedang bertampil di panggung, Ratih tidak sengaja menguping perkataan jelek padanya"
    show ratih shock
    "..."
    
    "Sehabis bertampil dipanggung, Ratih pun mencoba menguping percakapan tentang dirinya"

    s "liat tuh Ratih. Aktingnya biasa aja, pikmi banget dia mah. Ngandelin modal cantik doang"

    "Aku juga bisa lebih bagus dan lebih cantik daripada dia kalau ada kesempatan"
    

    menu:
        "Apakah Ratih perlu melawan teman yang suka mengejek?"
        
        "Ya! Lawan mereka!":
            jump ratih_melawan
            
        "Kabur sajalah! cari aman":
            jump ratih_kabur
# Alur cerita jika memilih opsi 1A
label ratih_melawan:
    hide ratih shock
    r "Cukup! Aku tidak akan membiarkan kalian mengejekku lagi!"
    "Ratih merasa sedikit lebih berani setelah mengutarakan perasaannya. Namun, teman pun tetap melawan tanpa alasan"

    "Ratih pun capek dan bertemu dengan orang tua di luar backstage dan Ratih mau berbicara sesuatu tapi..."

    i "Ratih, tadi kamu bertampil dengan baik dan bagus tapi rasanya kurang menarik... apa yang terjadi padamu?"
    a "Iya bener, padahal kamu itu sudah berusaha dengan baik tapi kok aktingnya jelek dan tidak menang sama sekali? Ada apa denganmu??"

    "Ratih hanya terdiam dan menangis ketika ditanya"

    menu:
        "Apa perlu menjawab atau tidak?"

        "Ya, menjawab dengan permintamaaf":
            jump ratih_menjawab
        
        "Tidak menjawab dan hanya mengangguk":
            jump ratih_tidakmenjawab

#Alur cerita jika memilih opsi 2A
label ratih_menjawab:
    r "A.. aku meminta maaf dan.. hanya gugup saja.."

    "Ratih pulang dengan penuh kecemasan dan melihat pemandangan dengan tatapan kosong"

    "Ego melihat dirinya dan merasa sedih dan penuh kekhawatiran"

    jump transisi_chapter_2

#Alur cerita jika memilih opsi 2B
label ratih_tidakmenjawab:
    "Ratih hanya mengangguk dan tidak menjawab sama sekali"

    "Ratih pulang dengan penuh kecemasan dan melihat pemandangan dengan tatapan kosong"
    jump transisi_chapter_2

# Alur cerita jika memilih opsi 1B
label ratih_kabur:
    "Ratih menunduk dan berjalan cepat menjauhi kerumunan itu."
    r "Lebih baik aku pulang saja..."
    
    i "Ratih, tadi kamu bertampil dengan baik dan bagus tapi rasanya kurang menarik... apa yang terjadi padamu?"
    a "Iya bener, padahal kamu itu sudah berusaha dengan baik tapi kok aktingnya jelek dan tidak menang sama sekali ?"

    "Ratih hanya terdiam dan menangis ketika ditanya"

    menu:
        "Apa perlu menjawab atau tidak?"

        "Ya, menjawab dengan permintamaaf":
            jump ratih_menjawab1
        
        "Tidak menjawab dan hanya mengangguk":
            jump ratih_tidakmenjawab1

#Alur cerita jika memilih opsi 2A
label ratih_menjawab1:
    r "A.. aku meminta maaf dan.. hanya gugup saja.."

    "Ratih pulang dengan penuh kecemasan dan melihat pemandangan dengan tatapan kosong"

    jump transisi_chapter_2

#Alur cerita jika memilih opsi 2B
label ratih_tidakmenjawab1:
    "Ratih hanya mengangguk dan tidak menjawab sama sekali"

    "Ratih pulang dengan penuh kecemasan dan melihat pemandangan dengan tatapan kosong"

    jump transisi_chapter_2

# Akhir dari Chapter 1
label transisi_chapter_2:
    scene black with dissolve
    window hide
    
    # Panggil screen dengan isi teks yang kamu mau
    call screen chapter_next_button("CHAPTER 2", "Gema Kecemasan")
    
    window show
    
    jump isi_chapter_2 # Melompat ke isi Chapter 2

label isi_chapter_2:
    "Memasuki masa SMP, Ratih pun banyak berubah dari masa SD."

    # Lanjutkan ceritamu di sini

    "Ratih melamun pada pemandangan luar dan banyak pikiran"
    "Tiba-tiba Guru memanggil Ratih untuk membacakan buku karena Ratih tidak memperhatikan kelas"
    g "Ratih, kamu saja tidak memperhatikannya, bisakah kamu membaca buku halaman 16 ?"
    "Ratih berdiri tegang dan gugup karena rasa takut padanya. Ratih pun mencoba membacakan tapi jantungku terasa cepat dan tidak berhenti"
    r "Rasanya aku tidak kuat dan sesek (dalam hati)"
    
    menu:
        "Perlu kabur atau tidak ?"

        "Kabur sajalah !!":
            jump ratih_kaburkelas

        "Tetap berusaha membacakan buku sebisanya":
            jump ratih_membaca

#Alur cerita Chapter II opsi 1A
label ratih_kaburkelas:
    "Kabur dari kelasnya dan ditertawain satu kelas"

    "Ratih langsung berlari dan ia menangis bersembunyi di dalam kamar mandi"
    "Setelah kelas pun selesai, Kayla mengetuk pintu kamar mandi"
    k "hey, ratih. Are u okay ? kalo ada apa, langsung kasih tau padaku ya"
    "Ratih pun keluar dari kamar mandinya"
    k "Gak apa apa ?"
    r "Gapapa"
    k "Yasudah, ayo ke kantin"
    "Kayla dan Ratih pun pergi menuju kantin sambil menggandeng tangan"
    "Tiba-tiba seorang laki-laki menabrak secara tidak sengaja"
    d "eh, gapapa ? maafkan aku"

#Alur cerita Chapter II opsi 1B
label ratih_membaca:
    "Saat Ratih mencoba, tiba-tiba Kayla memintaku duduk dan menggantikannya membaca buku."

    k "hey, biar aku yang baca saja, kamu duduk saja."

    "Aku pun mengangguk saja dan duduk dengan penuh khawatir"
    "Setelah beberapa menit yang berlalu"
    scene kaylaratih3:
        fit "cover"
        yalign 0.2
    k "kamu gapapa ? kalau ada apa, bilang saja ke aku ya"
    r "a-aku gak apa apa kok, kenapa ?"
    k "baiklah, mau ke kantin ?"
    "Ratih mengangguk dan berdua pun pergi menuju kantin sambil menggandeng tangan"
    "Tiba-tiba seorang laki-laki menabrak secara tidak sengaja"
    d "eh, gapapa ? maafkan aku"
    
    "Sekolah pun selesai, Ratih pulang dan beristirahat di rumah"
    "tiba-tiba..."
    "Ratih terbangun dan berada di dunia..."
    scene ratih world:
        fit "cover"
        yalign 0.9
    "dunia tidak biasa, Ratih's Mind"
    "Monster pun menyambut dan mengenalkan diri"
    "Monster Id menemani dan keliling dunia Ratih"
    "Tetiba Monster Id tidak sengaja menabrak properti Superego"
    p "Hey! kamu merusak propertiku!"
    u "kamu aja menaruh di tempat sembarangan!"
    "mereka pun mulai bertengkar, sedangkan Ratih melihat sesuatu yang gak biasa"
    "bukankah itu ego dirinya ?"
    "Ratih pun terbangun"
    r "haa!"
    "Esoknya, Ratih dan Kayla diberi tugas presentasi"
    "Ratih dan Kayla pun berlatih berpresentasi"
    "Ratih dan Kayla bersiap memulai mempresentasikan materi"
    "tapi...."
    "Ratih tiba-tiba mulai merasakan kegugupan (anxiety)"
    "jantungnya pun berdegub kencang dan rasanya mau kabur darinya"
    "anxiety pun melonjak naik, ia berlari dan bersembunyi"
    "begitu jadwal sekolah semua selesai dan dia pulang tanpa pamit kayla"
    "Di rumah"
    "Tiba-tiba bapak mengomel Ratih karena diberitahu guru bahwa Ratih mendapatkan posisi 3 terbaik sekolah"
    "Ratih tidak bisa berkata-kata tapi ia pun merasa posisi 3 itu sudah cukup"
    "Ia pun terdiam dan merenung dikamar menangis dan menelepon Kayla"

    jump transisi_chapter_3

# Akhir dari Chapter II
label transisi_chapter_3:
    scene black with dissolve
    window hide
    
    # Panggil screen dengan isi teks yang kamu mau
    call screen chapter_next_button("CHAPTER III", "FINALE (?)")
    
    window show
    
    jump isi_chapter_3 # Melompat ke isi Chapter 3

label isi_chapter_3:
    scene bg_kamar_ratih with dissolve
    "memasuki SMA"
    ""