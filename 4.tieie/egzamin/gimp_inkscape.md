# INF.03 - Kompletny Poradnik Graficzny (GIMP i Inkscape)

Ten dokument to zbiór rozwiązań "krok po kroku" dla każdego typu zadania graficznego, jakie może pojawić się na egzaminie INF.03.

---

## 1. GIMP - Gotowe Scenariusze (Grafika Rastrowa)

### Scenariusz A: "Wytnij obiekt z tła i zachowaj przezroczystość"

*Typowe polecenie: Przygotuj grafikę pozbawioną tła, aby idealnie komponowała się ze stroną.*

1. **Otwórz plik:** Przeciągnij zdjęcie do GIMPa.
2. **Dodaj kanał alfa (Kluczowe!):** Kliknij prawym przyciskiem myszy (PPM) na warstwę w panelu warstw -> **Dodaj kanał alfa**. Bez tego usunięte tło będzie białe, a nie przezroczyste.
3. **Zaznacz tło:**
   * *Jeśli tło jest jednolite:* Użyj narzędzia **Różdżka (U)**, kliknij na tło. Dostosuj suwak "Progowanie" w opcjach narzędzia, jeśli zaznacza za dużo lub za mało.
   * *Jeśli tło jest skomplikowane:* Użyj narzędzia **Odręczne zaznaczanie obszarów (Lasso - F)** i obrysuj obiekt. Odwróć zaznaczenie (**Zaznaczenie -> Odwróć** lub `Ctrl+I`).
4. **Usuń tło:** Wciśnij `Delete`. Pojawi się szachownica oznaczająca przezroczystość.
5. **Eksport (Kluczowe!):** Kliknij **Plik -> Wyeksportuj jako...** (`Shift+Ctrl+E`). Zmień rozszerzenie na `.png` (tylko ten format zachowa przezroczystość!).

### Scenariusz B: "Przygotuj baner o dokładnych wymiarach X na Y px"

*Typowe polecenie: Stwórz baner o wymiarach 800x200 px, zawierający logo i tekst.*

1. **Utwórz nowy plik:** **Plik -> Nowy** (`Ctrl+N`). Wpisz dokładnie szerokość (800) i wysokość (200). W opcjach zaawansowanych upewnij się, że rozdzielczość to 72 ppi (standard webowy).
2. **Dodaj tło:** Wypełnij warstwę tła kolorem za pomocą narzędzia **Wypełnienie kubkiem (Shift+B)** lub wklej wykadrowane zdjęcie.
3. **Dodaj tekst:** Użyj narzędzia **Tekst (T)**.
   * *Dobra praktyka webowa:* Zadbaj o wysoki kontrast między tekstem a tłem banera. Ciemny tekst na jasnym tle lub odwrotnie. Gwarantuje to czytelność na stronie.
4. **Skalowanie warstw:** Jeśli wklejasz inne zdjęcie na baner, użyj narzędzia **Skalowanie (Shift+S)**, aby dopasować je do wymiarów.
5. **Eksport:** Zapisz jako `.jpg` (jeśli to zdjęcie) lub `.png` (jeśli to płaska grafika z tekstem, co zapobiegnie "rozmyciu" liter). Nadaj plikowi prostą nazwę bez polskich znaków (np. `baner_glowny.png`), aby ułatwić osadzenie go w HTML i nadanie atrybutu `alt`.

### Scenariusz C: "Wykadruj i przeskaluj zdjęcie (np. zrób miniaturkę)"

*Typowe polecenie: Z pliku wykadruj twarz i przeskaluj obraz do wymiarów 150x150 px.*

1. **Kadrowanie:** Użyj narzędzia **Kadrowanie (Shift+C)**. W opcjach narzędzia zaznacz opcję **Stałe: Proporcje** i wpisz 1:1, aby uzyskać idealny kwadrat. Zaznacz interesujący Cię obszar i wciśnij `Enter`.
2. **Skalowanie:** Kliknij **Obraz -> Skaluj obraz...**. Upewnij się, że łańcuszek obok szerokości i wysokości jest "zapięty" (chroni przed zniekształceniem). Wpisz 150 w polu Szerokość. Zastosuj zmianę.
3. **Zapis:** Wyeksportuj jako `.jpg`, używając jakości około 80-85%, aby zoptymalizować wagę pliku na stronę WWW.

### Scenariusz D: "Zmień kolorystykę / Popraw jakość zdjęcia"

*Typowe polecenie: Zdjęcie jest za ciemne lub należy zmienić je na czarno-białe.*

* **Rozjaśnianie:** **Kolory -> Poziomy...** (przesuń środkowy suwak lekko w lewo) lub **Kolory -> Jasność i kontrast...**.
* **Czarno-białe:** **Kolory -> Desaturacja -> Desaturacja...** (lub **Kolory -> Odcień i nasycenie**, zjedź nasyceniem na 0).
* **Zmiana koloru elementu:** Użyj **Kolory -> Barwienie** lub **Odcień i nasycenie**, aby podmienić barwę konkretnej, zaznaczonej wcześniej części obrazka.

---

## 2. Inkscape - Gotowe Scenariusze (Grafika Wektorowa)

### Scenariusz A: "Stwórz proste logo / ikonę z kilku figur"

*Typowe polecenie: Wykonaj logo składające się z nakładających się kół lub innych kształtów geometrycznych.*

1. **Rysowanie:** Użyj narzędzi po lewej stronie (**Okrąg/Elipsa (E)**, **Prostokąt (R)**). Trzymaj `Ctrl` podczas rysowania, aby uzyskać idealne koło lub kwadrat.
2. **Kolorowanie:** Otwórz panel **Wypełnienie i kontur** (`Shift+Ctrl+F`). Ustaw kolor środka (Wypełnienie) oraz styl obramowania (Kontur). Utrzymuj wyraźny kontrast, aby ikona była wyraźna nawet w małym rozmiarze.
3. **Operacje logiczne na figurach (Ścieżka -> ...):**
   * *Suma (Ctrl++):* Łączy dwie figury w jedną.
   * *Różnica (Ctrl+-):* Wycina kształt górnej figury z tej pod spodem.
   * To najszybszy sposób na tworzenie skomplikowanych kształtów (np. księżyc zrobiony przez wycięcie jednego koła z drugiego).

### Scenariusz B: "Dodaj tekst do logo, który będzie działał wszędzie"

*Typowe polecenie: Umieść w logo nazwę firmy. Gwarancja, że tekst nie "rozsypie się" u egzaminatora.*

1. **Wprowadź tekst:** Narzędzie **Tekst (T)**, wpisz nazwę, wybierz krój pisma i rozmiar.
2. **Konwersja na krzywe (Złota zasada!):** Zaznacz tekst, a następnie kliknij w menu górnym: **Ścieżka -> Obiekt w ścieżkę** (`Shift+Ctrl+C`).
3. **Efekt:** Twój tekst przestał być edytowalnym tekstem, a stał się zbiorem wektorowych kształtów. Egzaminator zobaczy dokładnie to samo, co Ty, nawet jeśli nie ma Twojej czcionki na swoim komputerze. (Pamiętaj, by upewnić się, że tekst po zamianie jest wciąż czytelny).

### Scenariusz C: "Dopasuj obszar roboczy i wyeksportuj do SVG/PNG"

*Typowe polecenie: Zapisz wynik pracy jako plik wektorowy lub bitmapę bez białych marginesów.*

1. **Dopasowanie strony:** Zaznacz całe logo (`Ctrl+A`). Kliknij **Plik -> Właściwości dokumentu** (`Shift+Ctrl+D`). W zakładce "Strona" rozwiń opcję "Zmień rozmiar strony na zawartość" i kliknij ten przycisk. Biała kartka obetnie się idealnie do krawędzi Twojego logo.
2. **Eksport jako Wektor (HTML):** Kliknij **Plik -> Zapisz jako...**. Jako format wybierz koniecznie **Zwykły SVG (Plain SVG)** (nie Inkscape SVG!). Zwykły SVG nie zawiera śmieciowego kodu i jest idealny do użycia na stronie internetowej.
3. **Eksport jako Rastr (PNG):** Jeśli polecenie wymaga pliku PNG z logo: Kliknij **Plik -> Wyeksportuj obraz PNG** (`Shift+Ctrl+E`). Upewnij się, że w zakładce "Obszar eksportu" zaznaczone jest "Strona" lub "Zaznaczenie", wpisz nazwę pliku, wybierz ścieżkę i kliknij przycisk **Eksportuj**.
