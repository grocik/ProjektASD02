import heapq
from heapq import heappop, heappush


# wezel drzewa
class wezel:
    def __init__(self, litera, czestotliwosc, lewy=None, prawy=None):
        self.litera = litera
        self.czestotliwosc = czestotliwosc
        self.lewy = lewy
        self.prawy = prawy
    # obiekt z najwiekszym priorytetem ma najniszcza czestotliwosc
    def __lt__(self, other):
        return self.czestotliwosc < other.czestotliwosc

def jestLisciem(root):
    return root.lewy is None and root.prawy is None

def kodowanie(root, s, huffman_code):
    if root is None:
        return

    # znajdowanie liscia
    if jestLisciem(root):
        print(s)
        huffman_code[root.litera] = s if len(s) > 0 else '1'
        print(huffman_code[root.litera])

    kodowanie(root.lewy, s + '0', huffman_code)
    kodowanie(root.prawy, s + '1', huffman_code)

def czestotliwosc(text):
    freq = {i: text.count(i) for i in set(text)}
    print(freq)
    return freq

# budowanie drzewa
def drzewoHuffman(text):
    # pusty plik
    if len(text) == 0:
        return

    freq = czestotliwosc(text)
    kolejkaPrio = [wezel(k, v) for k, v in freq.items()]
    heapq.heapify(kolejkaPrio)

    # powtarzanie do jednego elementu w kolejce
    while len(kolejkaPrio) != 1:
        #  usuwanie 2 wezlow o najwyzszym priorytecie czyli najnizszej czestotliwosci
        lewy = heappop(kolejkaPrio)
        prawy = heappop(kolejkaPrio)
        # tworzenie nowego wezla  z dwoma wezlami jako dziecmi i dodanie wezla do kolejki
        total = lewy.czestotliwosc + prawy.czestotliwosc
        heappush(kolejkaPrio, wezel(None, total, lewy, prawy))

    # wskaznik na korzen drzewa
    root = kolejkaPrio[0]

    # przeszukanie drzewa i przechowywanie kodow huffmana
    kod = {}
    kodowanie(root, '', kod)

    # wyswietlanie kodow huffmana
    # wyswietlanie zakodowanego tekstu
    s = ''
    for c in text:
        s += kod.get(c)

    file = open("po.txt", "w")
    file.write(str(kod) + "\n")
    file.write(s)
    file.close()
    print(kod)
    print(s)



if __name__ == '__main__':
    file = open("przed.txt", "r")
    text = file.read()
    file.close()
    drzewoHuffman(text)
