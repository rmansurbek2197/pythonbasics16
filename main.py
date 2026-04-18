def top_sonlar():
    N = int(input("N ni kiriting: "))
    sonlar = []
    for i in range(1, N+1):
        if i % 3 == 0 and i % 5 == 0:
            sonlar.append(i)
    print("1 dan", N, "gacha 3 va 5 ga bo'linadigan sonlar: ", sonlar)

def asosiy():
    print("1 dan N gacha 3 va 5 ga bo'linadigan sonlarni topish dasturi")
    top_sonlar()
    savol = input("Dasturni qayta ishga tushirishni hohlaysizmi? (ha/yo'q): ")
    if savol.lower() == "ha":
        asosiy()
    else:
        print("Dastur to'xtatildi")

asosiy()