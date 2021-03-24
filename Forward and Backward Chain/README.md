global fact
global is_changed

is_changed = True
facts = [["Action","Genre"],["Romance","Genre"],["School","Film"]]

facts sebagai variabel global

def assert_fact(fact):
    global facts
    global is_changed
    if not fact in facts:
        facts += [fact]
        is_changed = True

sebuah class yang berupa method perulangan dan menyimpan data baru

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "School":
            assert_fact(["Film",A1[1]])
        if A1[0] == "Action":
            assert_fact(["Thriller",A1[1]])
        if A1[0] == "Action" and ["Sadistic",A1[1]] in facts:
            assert_fact(["Surprise",A1[1]])

method perulangan yang membuat fakta baru dengan metode forward chain

while is_changed:
    is_changed = False
    for A1 in facts:
        if A1[0] == "Action" and ["Kill",A1[1]] in facts:
            assert_fact(["Thriller",A1[1]])
        if A1[0] == "Action":
            assert_fact(["Sadis",A1[1]])
        if A1[0] == "Surprise":
            assert_fact(["Shock",A1[1]])
        
print("BackwardChain")     
print(facts)

method perulangan yang membuat fakta baru dengan metode backward chain

from mal import AnimeSearch

memanggil module AnimeSearch dari library mal

nama=input("Masukan Nama Anda : ")

variabel nama yang meminta user untuk memasukkan nama

pilihan=input("\nHi, "+nama+". Apakah Anda ingin melihat info anime? (y/n) : ")

variabel pilihan yang meminta user untuk memasukkan boolean yes atau no

while pilihan == "y":
    print("Masukkan Judul Anime yang ingin Anda Cari")
    print("Contoh : Naruto Shippuden\n")

jika pilihan yes lanjut ke method search

search = AnimeSearch(input("Judul : "))

variabel search yang meminta user untuk memasukkan judul anime

    print(search.results[0].title) 
    print(search.results[0].score)
    print(search.results[0].mal_id)
    print(search.results[0].episodes)
    print(search.results[0].url)

mencetak title, score, mal id, episodes, dan url dari judul anime yang dimasukkan

pilihan=input("\nHi, "+nama+". Mau lihat info lagi? (y/n) : ")

setelah user mendapat info anime, user di minta apakah masih ingin melihat atau tidak

if pilihan=="y":

jika pilih yes akan mengulang method dari awal

    else:
        print("\n+----------------------Terima Kasih------------------------+")
        print("+--------------Telah Berkunjung di Info Anime--------------+")

jika pilih no, akan muncul pesan terima kasih