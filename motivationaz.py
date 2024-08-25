import streamlit as st

# Menampilkan pesan selamat datang
st.write("Halo kamu! >_<")
st.write("Sebelumnya aku akan mengajukan beberapa pertanyaan nih, kamu bisa menjawabnya dengan mengetik kalimat/kata sesuai dengan panduan yang akan diberikan! (dengan catatan ketik semua jawaban kamu dengan huruf kecil ya!)")

# Fungsi ready untuk menanyakan apakah pengguna sudah siap
def ready():
    ask_ready = st.radio("Apakah kamu sudah siap?👊🏻", ["ya", "tidak"])
    if ask_ready == "ya":
        return st.text_input("Oke sip, sebelumnya cewek apa cowok nih?🤔").lower()
    elif ask_ready == "tidak":
        st.text_input("Wah... Kalau gitu kamu tarik nafas dulu yak, rileksin dirimu dulu.🥺 Sudah? (jawab 'sudah')")
        return st.text_input("Oke sip, sebelumnya cewek apa cowok nih?🤔 (jawab 'cewek' atau 'cowok')").lower()

# Menyimpan hasil dari fungsi ready
gender_ask = ready()

# Fungsi name untuk menanyakan nama panggilan
def name(gender_ask):
    if gender_ask == "cewek":
        return st.text_input(f"Wah ada {gender_ask} cantik nih.🤩 Nama panggilannya siapa kalau boleh tahu?")
    elif gender_ask == "cowok":
        return st.text_input(f"Wah ada {gender_ask} ganteng nih.🤩 Nama panggilannya siapa kalau boleh tahu?")

# Menyimpan hasil dari fungsi name
name_ask = name(gender_ask)

# Fungsi gift untuk menanyakan pilihan hadiah
def gift():
    satuduatiga = st.selectbox(
        "By the way, aku mau ngasih kamu hadiah nih, cukup ketik satu angka saja di antara angka 1 atau 2 atau 3🎁😼",
        ["1", "2", "3"]
    )
    return satuduatiga

# Menyimpan hasil dari fungsi gift
gift_ask = gift()

# Fungsi surprise untuk memberikan pesan berdasarkan pilihan hadiah
def surprise():
    if gift_ask == "1":
        st.write(f"Hai, {name_ask}😃 Terima kasih ya! Kamu sudah memperjuangkan dirimu sampai saat ini. Bukan perihal yang mudah loh untuk mencapai masa kini🤯 Tentu butuh effort yang super duper banyak💪🏻 Dan sekarang kamu berhasil loh?! Selamat ya!!!")
        for _ in range(10):
            st.write(f"Terima kasih telah berjuang! Kamu hebat, {name_ask}🌟")
            
    elif gift_ask == "2":
        st.write(f"Hai, {name_ask}😃 Kamu pasti baru capek dan banyak hal yang sedang kamu pikirin☹️ It's okay, {name_ask}🫂 Yang perlu kamu ingat selalu adalah bahwa capekmu hari ini adalah suksesmu di masa nanti. Keep it going okay!!! Selalu percaya pada proses😎🤏🏻")
        for _ in range(10):
            st.write(f"Percayalah, kamu pasti bisa! Terus semangat, {name_ask}🦸🏻‍♂️")
            
    elif gift_ask == "3":
        st.write(f"Hai, {name_ask}😃 Loh ada apa? Kamu sedang tidak yakin dengan dirimu? Kamu sedang merasa apapun yang kamu lalukan sampai saat ini adalah sia-sia? atau Kamu sedang dihadapkan dengan suatu masalah?☹️ Hai, tau gak bahwa Tuhan gapernah memberi ujian kepada hamba-Nya ujian yang sungguh berat bila hamba-Nya tidak bisa melewatinya loh🤩 So yakinlah dengan apa yang kau anggap bisa! Lakukanlah apa yang kamu percaya selama itu yang terbaik bagimu🏆 Jalani prosesnya, {name_ask}! Sungguh kamu tidak mengetahui apa yang Tuhan ketahui🙇🏻‍♂️ Hal indah terkadang datang dari sebuah penderitaan. So, mari kita lawan penderitaan itu, {name_ask}💪🏻😼")
        for _ in range(10):
            st.write(f"Lawan penderitaanmu itu. Kamu bisa, {name_ask}😾👊🏻")

# Menampilkan hasil akhir
surprise()

st.write("Thank you for visiting")
st.write("coding by @darius.azzam 👾")