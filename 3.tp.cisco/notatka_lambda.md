# PROSTE TŁUMACZENIE: Czym jest ta cała "Lambda"?

Wyobraź sobie, że normalna funkcja (taka z `def`) to duża fabryka. Ma nazwę, drzwi wejściowe, taśmę produkcyjną i magazyn wyjściowy (`return`).

**`Lambda` to taka mała, jednorazowa maszynka.** Nie ma nazwy. Robi tylko jedną prostą rzecz i od razu podaje wynik.

Każda lambda składa się z 3 elementów. Zobacz, jak to prosto wygląda:

1. Słowo **`lambda`** (czyli: "Uwaga, uruchamiam maszynkę!")
2. **Wejście** (to, co wrzucasz do maszynki)
3. **Dwukropek `:`** (oznacza: "zamień to na...")
4. **Wyjście** (wynik, który wypluwa maszynka)
    

> **PRZYKŁAD:** `lambda x: x + 1`
> 
> _Tłumaczenie:_ "Maszynko (`lambda`), weź liczbę `x` (`x`), i zamień ją na (`:`) tę samą liczbę powiększoną o jeden (`x + 1`)."

```python
# 1. Budujemy maszynkę i naklejamy karteczkę "podwojenie"
podwojenie = lambda liczba: liczba * 2

# 2. Odpalamy maszynkę! Wrzucamy do środka piątkę (używamy nawiasów)
print(podwojenie(5)) # Wypisze: 10
```
## ZADANIE 1: Maszynka decyzyjna (Kategoria cenowa)

**Twój cel:** Chcemy stworzyć maszynkę, która patrzy na cenę i mówi "Premium", jeśli cena to 100 lub więcej, a "Standard", jeśli jest mniejsza.

**Jak myśli maszyna:**

- "Biorę cenę..." -> `lambda cena:`
- "Zwracam napis Premium, jeśli cena jest większa lub równa 100..." -> `"Premium" if cena >= 100`
- "W przeciwnym razie zwracam napis Standard." -> `else "Standard"`

**Gotowy kod do wpisania:**
```python
kategoria_cenowa = lambda cena: "Premium" if cena >= 100 else "Standard"
```

## ZADANIE 2: Używanie sita, czyli `filter()`

Mamy pudełko z produktami. Chcemy zostawić w nim tylko te dobre, a resztę wyrzucić. Do tego służy narzędzie `filter()`. Działa jak prawdziwe sito.

Sito potrzebuje dwóch rzeczy, żeby zadziałać:
1. **Zasady przepuszczania (to nasza lambda):** Mówimy maszynce: "Weź pojedynczy `produkt`, spójrz na jego `ocenę` i przepuść tylko wtedy, gdy jest większa niż `4.0`". Zapisujemy to tak: `lambda produkt: produkt["ocena"] > 4.0`.
2. **Rzeczy do przesiania:** Wsypujemy tam naszą główną listę, czyli `produkty`.
Całość musimy na końcu zamknąć w słowie `list()`, żeby z powrotem spakować to do listy.
```python
polecane_produkty = list(filter(lambda produkt: produkt["ocena"] > 4.0, produkty))
```

## ZADANIE 3: Układanie na półce, czyli `.sort()`
Wyobraź sobie, że każesz komputerowi posortować produkty. Komputer jest głupi i pyta: _"Ale jak? Po nazwie? Po cenie? Od a do z?"_.

Musimy mu pokazać palcem, na co ma patrzeć podczas układania. Tym "palcem wskazującym" jest parametr `key=` oraz nasza maszynka `lambda`.
Chcemy posortować rosnąco według ilości w magazynie.
- Mówimy komputerowi: "Kluczem do sortowania (`key=`) będzie maszynka (`lambda`), która weźmie pojedynczy `produkt` i wskaże ci palcem na jego `stan_magazynowy`".

Zapisujemy to tak: `key=lambda produkt: produkt["stan_magazynowy"]`.
```python
produkty.sort(key=lambda produkt: produkt["stan_magazynowy"])
```

### GOTOWE ROZWIĄZANIE (Zadania 1, 2 i 3)

```
# ZADANIE 1
kategoria_cenowa = lambda cena: "Premium" if cena >= 100 else "Standard"

# ZADANIE 2
polecane_produkty = list(filter(lambda produkt: produkt["ocena"] > 4.0, produkty))

# ZADANIE 3
produkty.sort(key=lambda produkt: produkt["stan_magazynowy"])
```

