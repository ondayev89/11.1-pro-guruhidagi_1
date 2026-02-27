"""
7. Fayllarni guruhlash:
fayllar = [ “kitob.jpg”, “kuk jiguli.mp3”, “tabiat.jpg”, “malohat.mp3”, “iphone16.jpg”]
musiqalar=[ ] va rasmlar=[ ] nomli listlar yarating. Fayllar ustida sikl aylantirib “.jpg”
larni rasmlar listiga, “.mp3” larni musiqalar listiga qo’shing. Yordam: find() string
metodi va append() list metodidan foydalaning.
"""
fayllar = ["kitob.jpg", "kuk jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
musiqalar=[]
rasmlar=[]
for note in fayllar:
    if note.find(".jpg")!=-1:
        rasmlar.append(note)
    if note.find(".mp3")!=-1:
        musiqalar.append(note)
print(rasmlar)
print(musiqalar)