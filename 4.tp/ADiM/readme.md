
# 🐍 CZĘŚĆ 1: LISTY W PYTHONIE – SZCZEGÓŁOWO

### Podstawowe operacje na listach – co robi każda funkcja?

```python
imiona = ["Adam", "Bartek", "Czarek", "Marek", "Jarek"]
```

| Metoda/Funkcja | Co robi? | Przykład | Wynik |
|---------------|----------|----------|-------|
| `lista[i]` | Pobiera element o indeksie `i` (liczymy od 0!) | `imiona[2]` | `"Czarek"` |
| `lista.append(x)` | **Dodaje** element `x` **na koniec** listy | `imiona.append("Adrian")` | `[..., "Adrian"]` |
| `lista.pop(i)` | **Usuwa i zwraca** element o indeksie `i`. Jeśli brak argumentu – usuwa ostatni | `imiona.pop(1)` | usuwa `"Bartek"` |
| `lista.reverse()` | **Odwraca kolejność** elementów w miejscu (bez tworzenia nowej listy) | `imiona.reverse()` | `["Jarek", "Marek", ...]` |
| `len(lista)` | Zwraca **liczbę elementów** w liście | `len(imiona)` | `5` |
| `x in lista` | Sprawdza, czy wartość `x` **występuje** w liście (zwraca `True/False`) | `"Adam" in imiona` | `True` |

### 🔍 List comprehension – filtrowanie i transformacja
```python
# Składnia: [wyrażenie for element in iterable if warunek]

# Przykład 1: Tylko imiona na "A"
imieNaA = [imie for imie in imiona if imie.startswith("A")]
# Działa tak:
# 1. Bierze każdy 'imie' z listy 'imiona'
# 2. Sprawdza warunek: czy zaczyna się od "A"?
# 3. Jeśli TAK – dodaje do nowej listy

# Przykład 2: Imiona + długość
dane = [(imie, len(imie)) for imie in imiona]
# Wynik: [("Adam", 4), ("Bartek", 6), ...]
```

### 🔗 `zip()` – łączenie list w pary
```python
imiona = ["Anna", "Piotr", "Kasia"]
nazwiska = ["Kowalski", "Nowak", "Wiśniewski"]

# zip() łączy elementy o tym samym indeksie z obu list
for imie, nazwisko in zip(imiona, nazwiska):
    print(f"{imie} {nazwisko}")

# Tworzenie listy list:
imieNazwisko = [list(para) for para in zip(imiona, nazwiska)]
# Wynik: [["Anna", "Kowalski"], ["Piotr", "Nowak"], ["Kasia", "Wiśniewski"]]

# ⚠️ Jeśli listy mają różną długość, zip() kończy na krótszej!
```

---

## 🗂️ CZĘŚĆ 2: SŁOWNIKI (DICTIONARIES) – WYJAŚNIENIA

### Struktura słownika – co się gdzie znajduje?
```python
uczen = {
    "imię": "Jan",           # klucz: "imię" → wartość: "Jan" (string)
    "nazwisko": "Kowalski",  # klucz: "nazwisko" → wartość: "Kowalski"
    "klasa": "3TP",          # klucz: "klasa" → wartość: "3TP"
    "oceny": [5, 4, 6, 3]    # klucz: "oceny" → wartość: LISTA liczb
}
```

| Operacja | Co robi? | Przykład | Uwagi |
|----------|----------|----------|-------|
| `dict[key]` | Pobiera wartość pod kluczem `key` | `uczen["imię"]` | ❗ Jeśli klucz nie istnieje → błąd `KeyError` |
| `dict.get(key, default)` | Bezpieczne pobieranie – zwraca `default`, jeśli brak klucza | `uczen.get("wiek", 18)` | Bezpieczniejsze niż `dict[key]` |
| `dict[key] = value` | Dodaje nowy klucz lub **nadpisuje** istniejący | `uczen["wiek"] = 19` | - |
| `key in dict` | Sprawdza, czy klucz istnieje w słowniku | `"imię" in uczen` | Zwraca `True/False` |
| `dict.keys()` | Zwraca wszystkie klucze | `uczen.keys()` | `dict_keys(['imię', 'nazwisko', ...])` |
| `dict.values()` | Zwraca wszystkie wartości | `uczen.values()` | `dict_values(['Jan', 'Kowalski', ...])` |
| `dict.items()` | Zwraca pary `(klucz, wartość)` | `uczen.items()` | Przydatne w pętlach `for k, v in dict.items()` |

### 🧮 Obliczanie średniej – krok po kroku
```python
oceny = uczen["oceny"]  # [5, 4, 6, 3]

# Krok 1: sum() dodaje wszystkie elementy listy
suma = sum(oceny)  # 5+4+6+3 = 18

# Krok 2: len() zwraca liczbę elementów
liczba_ocen = len(oceny)  # 4

# Krok 3: dzielimy sumę przez liczbę
srednia = suma / liczba_ocen  # 18 / 4 = 4.5
```

### 🔁 Zagnieżdżone struktury – jak się po nich poruszać?
```python
klasy = {
    "3TP": {
        "uczniowie": [
            {"imie": "Ziutek", "oceny": [5, 6]},  # indeks 0
            {"imie": "Ania", "oceny": [2, 4]}     # indeks 1
        ],
        "wychowawca": "Jan Nowak"
    }
}

# Dostęp do imienia drugiego ucznia w 3TP:
klasy["3TP"]["uczniowie"][1]["imie"]  # "Ania"

# Dodawanie nowego ucznia:
nowy = {"imie": "Kasia", "oceny": [4, 3]}
klasy["3TP"]["uczniowie"].append(nowy)  # dodaje na koniec listy
```

---

## 💡 CZĘŚĆ 2.5: `lambda` – PEŁNE WYJAŚNIENIE

### ❓ Czym jest `lambda`?
`lambda` to **funkcja anonimowa** (bez nazwy), zapisywana w jednej linii. Używamy jej tam, gdzie potrzebujemy prostej funkcji "w locie", np. jako argumentu do `sorted()`, `max()`, `filter()`.

### 🔧 Składnia:
```python
lambda argumenty: wyrażenie
```
- `argumenty` – mogą być jeden lub więcej, oddzielone przecinkiem
- `wyrażenie` – **jedno** wyrażenie, którego wynik jest automatycznie zwracany
- ❗ Nie może zawierać instrukcji (np. `if/else` jako bloku, pętli, `return`)

### 🎯 Przykłady krok po kroku:

#### Przykład 1: Prosta lambda – dodawanie
```python
# Zwykła funkcja:
def dodaj(a, b):
    return a + b

# To samo jako lambda:
dodaj = lambda a, b: a + b

# Użycie:
dodaj(3, 5)  # zwraca 8
```

#### Przykład 2: Lambda z `max()` – znajdź ucznia z najwyższą średnią
```python
uczniowie = [
    {"imie": "Ziutek", "oceny": [5, 6]},      # średnia: 5.5
    {"imie": "Ania", "oceny": [2, 4]},        # średnia: 3.0
    {"imie": "Kasia", "oceny": [6, 6, 5]}     # średnia: 5.67 ← najwyższa
]

# max() potrzebuje klucza, po którym porównywać elementy
# lambda bierze jednego ucznia 'u' i zwraca jego średnią
najlepszy = max(uczniowie, key=lambda u: sum(u["oceny"]) / len(u["oceny"]))

# Co się dzieje "pod maską"?
# 1. max() bierze pierwszego ucznia: {"imie": "Ziutek", ...}
# 2. Uruchamia lambda: sum([5,6])/len([5,6]) = 5.5
# 3. Powtarza dla każdego ucznia
# 4. Zwraca tego, dla którego lambda zwróciła NAJWIĘKSZĄ wartość

print(najlepszy["imie"])  # "Kasia"
```

#### Przykład 3: Lambda z `sorted()` – sortowanie po nazwisku
```python
uczniowie = [
    {"imie": "Jan", "nazwisko": "Zieliński"},
    {"imie": "Anna", "nazwisko": "Nowak"},
    {"imie": "Piotr", "nazwisko": "Kowalski"}
]

# Sortowanie alfabetycznie po nazwisku:
posortowani = sorted(uczniowie, key=lambda u: u["nazwisko"])

# Wynik:
# [Anna Nowak, Piotr Kowalski, Jan Zieliński]
```

#### Przykład 4: Lambda z `filter()` – filtruj uczniów z średnią > 4.0
```python
dobrzy = list(filter(lambda u: sum(u["oceny"])/len(u["oceny"]) > 4.0, uczniowie))
# filter() zwraca iterator, dlatego używamy list(), żeby zobaczyć wynik
```

### ⚠️ Kiedy NIE używać `lambda`?
- Gdy logika jest zbyt skomplikowana (lepiej napisać zwykłą funkcję z `def`)
- Gdy potrzebujesz dokumentacji lub wielokrotnego użycia w wielu miejscach
- Gdy kod staje się nieczytelny – **czytelność > zwięzłość!**

### 🆚 `lambda` vs `def` – porównanie
```python
# To samo zadanie – dwie formy:

# Forma 1: lambda (zwięzła)
srednia = lambda oceny: sum(oceny) / len(oceny) if oceny else 0

# Forma 2: def (czytelna, z obsługą błędów)
def oblicz_srednia(oceny):
    """Zwraca średnią arytmetyczną z listy ocen."""
    if not oceny:  # pusta lista?
        return 0
    return sum(oceny) / len(oceny)
```

---

## 🏗️ CZĘŚĆ 3: PROGRAMOWANIE OBIEKTOWE (OOP) – SZCZEGÓŁY

### 🔑 Kluczowe pojęcia OOP

| Pojęcie | Co to jest? | Przykład z kodu |
|---------|-------------|-----------------|
| **Klasa** | Szablon/plan tworzenia obiektów | `class Uczen:` |
| **Obiekt (instancja)** | Konkretny egzemplarz utworzony z klasy | `uczen1 = Uczen("Jan", "Kowalski")` |
| **Atrybut** | Dane przechowywane w obiekcie | `self.imie`, `self.oceny` |
| **Metoda** | Funkcja należąca do klasy, operująca na obiekcie | `def dodaj_ocene(self, ocena):` |
| **`__init__`** | **Konstruktor** – uruchamiany automatycznie przy tworzeniu obiektu | `def __init__(self, imie): self.imie = imie` |
| **`self`** | Referencja do **bieżącego obiektu** – pozwala odwoływać się do jego atrybutów i metod | `self.imie = imie` |

### 🧱 Przykład klasy z komentarzami krok-po-kroku
```python
class Uczen:
    # Konstruktor – wywoływany przy: uczen = Uczen("Jan", "Kowalski")
    def __init__(self, imie, nazwisko):
        self.imie = imie          # przypisz argument 'imie' do atrybutu obiektu
        self.nazwisko = nazwisko  # przypisz argument 'nazwisko' do atrybutu obiektu
        self.oceny = []           # każdy uczeń zaczyna z pustą listą ocen
    
    # Metoda instancji – dodaje jedną ocenę do listy
    def dodaj_ocene(self, ocena):
        """Dodaje ocenę (liczbę) do listy ocen ucznia."""
        if 1 <= ocena <= 6:  # walidacja: ocena musi być z zakresu 1-6
            self.oceny.append(ocena)
        else:
            print(f"Nieprawidłowa ocena: {ocena}")
    
    # Metoda obliczająca średnią
    def srednia(self):
        """Zwraca średnią arytmetyczną ocen lub 0, jeśli brak ocen."""
        if not self.oceny:  # jeśli lista pusta
            return 0
        return sum(self.oceny) / len(self.oceny)
    
    # Metoda zwracająca czytelny opis ucznia
    def __str__(self):
        """Zwraca string z danymi ucznia – używane przy print(uczen)"""
        return f"{self.imie} {self.nazwisko}, średnia: {self.srednia():.2f}"
```

### 🔗 Relacje między klasami – kompozycja
```python
class Klasa:
    def __init__(self, nazwa_klasy, kierunek):
        self.nazwa_klasy = nazwa_klasy
        self.kierunek = kierunek
        self.uczniowie = []  # lista OBIEKTÓW klasy Uczen
    
    def dodaj_ucznia(self, u):
        """Dodaje obiekt Uczen do klasy."""
        if isinstance(u, Uczen):  # sprawdza, czy 'u' to instancja Uczen
            self.uczniowie.append(u)
        else:
            print("Błąd: można dodać tylko obiekt klasy Uczen")
    
    def policz_uczniow(self):
        """Zwraca liczbę uczniów w klasie."""
        return len(self.uczniowie)
    
    def ranking(self):
        """Zwraca listę uczniów posortowaną malejąco po średniej."""
        # sorted() + lambda: sortuj po u.srednia(), od największej
        return sorted(self.uczniowie, key=lambda u: u.srednia(), reverse=True)
```

---

## 🌐 CZĘŚĆ 4: DJANGO – CO I PO CO?

### 🗂️ Struktura projektu – opis plików
```
TestDjango/
├── manage.py          # 🔧 Narzędzie CLI: uruchamia serwer, tworzy migracje, itp.
├── db.sqlite3         # 💾 Plik bazy danych (SQLite – domyślna w Django)
├── TestDjango/        # 🎛️ Główna konfiguracja projektu
│   ├── __init__.py    # Oznacza folder jako pakiet Pythona
│   ├── settings.py    # ⚙️ Ustawienia: baza danych, aplikacje, security, itp.
│   ├── urls.py        # 🗺️ Mapuje adresy URL na widoki (views)
│   ├── asgi.py        # Serwer asynchroniczny (dla produkcji)
│   └── wsgi.py        # Serwer synchroniczny (dla produkcji)
└── bibleApi/          # 📦 Aplikacja w ramach projektu (może być wiele)
    ├── models.py      # 🗃️ Definicje tabel bazy danych (klasy → tabele)
    ├── views.py       # 👁️ Logika aplikacji: co zwrócić na żądanie HTTP
    ├── urls.py        # 🔗 URL-e specyficzne dla tej aplikacji
    └── admin.py       # 👮 Konfiguracja panelu administratora
```

### 🚀 Kluczowe komendy `manage.py` – co robią?

```bash
# 🖥️ Uruchom serwer deweloperski (dostępny pod http://127.0.0.1:8000)
python manage.py runserver

# 🔄 Przygotuj migracje – Django analizuje models.py i tworzy "plan zmian" w bazie
python manage.py makemigrations

# 🛠️ Zastosuj migracje – wykonuje plan zmian na rzeczywistej bazie danych
python manage.py migrate

# 👤 Utwórz superużytkownika z dostępem do panelu admina
python manage.py createsuperuser

# 🐍 Uruchom interaktywną konsolę Pythona z załadowanym projektem Django
python manage.py shell

# 🧪 Uruchom testy automatyczne zdefiniowane w aplikacjach
python manage.py test
```

### 🔐 Dlaczego `os.environ.setdefault()` w `manage.py`?
```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestDjango.settings')
```
- Ustawia zmienną środowiskową, która mówi Django: **"który plik settings.py użyć"**
- `setdefault()` ustawia wartość TYLKO jeśli zmienna jeszcze nie istnieje – pozwala na nadpisanie z zewnątrz (np. w produkcji)

---

## ⚡ SZYBKA POWTÓRKA – FUNKCJE I ICH DZIAŁANIE

| Funkcja / Składnia | Typ zwracany | Opis działania | Przykład użycia |
|-------------------|--------------|----------------|-----------------|
| `sum(iterable)` | `int`/`float` | Sumuje wszystkie elementy iterowalnego (listy, krotki) | `sum([1,2,3]) → 6` |
| `len(iterable)` | `int` | Zwraca liczbę elementów | `len("hello") → 5` |
| `range(start, stop, step)` | `range` | Generuje sekwencję liczb (używana w pętlach) | `list(range(2, 10, 2)) → [2,4,6,8]` |
| `enumerate(iterable)` | `enumerate` | Zwraca pary `(indeks, wartość)` – przydatne w pętlach | `for i, val in enumerate(lista):` |
| `str.startswith(prefix)` | `bool` | Sprawdza, czy string zaczyna się od `prefix` | `"Anna".startswith("A") → True` |
| `dict.get(key, default)` | dowolny | Bezpieczne pobieranie wartości ze słownika | `uczen.get("wiek", 18)` |
| `isinstance(obj, Class)` | `bool` | Sprawdza, czy obiekt jest instancją danej klasy | `isinstance(x, Uczen)` |
| `sorted(iterable, key=..., reverse=...)` | `list` | Zwraca **nową**, posortowaną listę | `sorted(uczniowie, key=lambda u: u.srednia())` |
| `lambda x: wyrażenie` | funkcja | Tworzy anonimową funkcję jednolinijkową | `key=lambda u: sum(u["oceny"])/len(u["oceny"])` |

---

## ❓ POTENCJALNE PYTANIA EGZAMINOWE + ODPOWIEDZI

1. **Jak obliczyć średnią ocen z listy?**  
   → `sum(oceny) / len(oceny)` – ale najpierw sprawdź, czy lista nie jest pusta!

2. **Jak dodać nowy klucz do słownika?**  
   → `slownik["nowy_klucz"] = wartość` – jeśli klucz istniał, zostanie **nadpisany**.

3. **Jak stworzyć instancję klasy?**  
   → `uczen = Uczen("Jan", "Kowalski")` – wywoła to metodę `__init__`.

4. **Do czego służy `self` w klasach?**  
   → To referencja do **bieżącego obiektu**. Dzięki `self.imie` wiemy, że chodzi o atrybut *tego konkretnego* ucznia, a nie innego.

5. **Jak uruchomić serwer Django?**  
   → `python manage.py runserver` – domyślnie na `http://127.0.0.1:8000`.

6. **Jak przefiltrować listę imion na literę "A"?**  
   → `[i for i in lista if i.startswith("A")]` – list comprehension + `startswith()`.

7. **Czym różni się `list.append()` od `list.insert()`?**  
   → `append(x)` dodaje na **koniec**, `insert(i, x)` dodaje na **konkretny indeks** `i`.

8. **Co zwraca `lambda x: x*2`?**  
   → Funkcję, która po wywołaniu `f(5)` zwróci `10`. Sama w sobie `lambda` nie wykonuje kodu – tylko go definiuje.

---

> 💡 **Pro tip na egzamin**:  
> - Zawsze sprawdzaj, czy lista/słownik nie jest pusty przed operacjami (`if lista:`)  
> - `lambda` jest świetna do krótkich kluczy sortowania, ale nie nadużywaj jej – czytelność jest ważniejsza niż zwięzłość!  
> - W Django: `makemigrations` = "przygotuj zmiany", `migrate` = "zastosuj zmiany" – nie pomyl kolejności!

---

✅ **Gotowe!** Ta wersja zawiera **szczegółowe wyjaśnienia**, przykłady krok-po-kroku i odpowiedzi na potencjalne wątpliwości. Możesz ją zapisać jako `powtorka_ADiM.md` i używać jako kompletnego materiału do nauki.

Chcesz, żebym dodał jeszcze:
- 🎨 Przykładowe zadania do samodzielnego rozwiązania?
- 🧪 Testowe pytania z odpowiedziami (typu "co wypisze ten kod?")?
- 📊 Schemat blokowy relacji między klasami?

Daj znać, a rozwinę! 😊📚