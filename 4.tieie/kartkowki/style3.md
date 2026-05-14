
# Kartkówka: Manipulacja DOM i CSS (Wersja C)

## 1. Struktura HTML (bez zmian w kodzie)

Przeanalizuj poniższy fragment kodu:

```html
<div id="visual-preview">
    Element testowy
</div>

<form>
    <label>Szerokość: <input type="text" placeholder="np. 300px"></label><br>
    <label>Wysokość: <input type="text" placeholder="np. 10vh"></label><br>
    <label>Kolor tła: <input type="text" placeholder="np. #ff0000"></label><br>
    <label>Obramowanie: <input type="text" placeholder="np. 2px dashed blue"></label><br>
    <label>Nowy tekst: <input type="text" placeholder="Wpisz treść..."></label><br>
    
    <button id="btn-submit">Zmień wygląd</button>
</form>

```

## 2. Zadanie programistyczne (JavaScript)

Napisz skrypt w języku JavaScript, który obsłuży powyższy formularz. Stwórz funkcję o nazwie `zmienStylElementu()`, która zostanie wywołana po kliknięciu przycisku.

**Wymagania szczegółowe:**

* **Krok 1: Przechwycenie zdarzenia**
Podepnij funkcję pod przycisk, pamiętając o zablokowaniu domyślnej akcji przeładowania strony (`event.preventDefault()`).
* **Krok 2: Pobranie wartości**
Pobierz wartości wpisane przez użytkownika do wszystkich pięciu pól `input`. Zwróć uwagę na kolejność pól w formularzu (Szerokość, Wysokość, Kolor, Obramowanie, Tekst).
* **Krok 3: Manipulacja elementem #visual-preview**
* Zmień parametry CSS elementu o ID `visual-preview` (szerokość, wysokość, kolor tła, obramowanie) zgodnie z danymi z formularza.
* Zmień tekst wewnątrz elementu na ten podany w ostatnim polu.
