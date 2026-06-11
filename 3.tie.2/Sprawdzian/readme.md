# Sprawdzian Praktyczny INF.03: Obsługa formularzy i DOM – Grupa A

## **Część 1: HTML (Struktura)**
Stwórz w pliku HTML semantyczny interfejs użytkownika w postaci formularza. Zbuduj system rezerwacji stanowiska w szkolnej sali e-sportowej, zawierający:

1. Pole na **Nick (pseudonim) gracza**.
2. Pole na **Wybrany tytuł gry** (np. CS2, Valorant).
3. Pole na **Czas rezerwacji (w godzinach)**.
4. Przycisk zatwierdzający formularz.
5. Pusty element, w którym wyświetli się ostateczny komunikat dla użytkownika.

**Wymóg:** Struktura formularza musi być poprawna semantycznie i w pełni zgodna ze standardami dostępności (WCAG) – zadbaj o poprawne powiązanie etykiet z polami.

## **Część 2: JavaScript (Logika)**
Napisz skrypt, który obsłuży proces wysyłania stworzonego formularza. Skrypt musi realizować następujące punkty:

1. **Podpięcie zdarzenia:** Nasłuchuj momentu wysłania formularza, korzystając z nowoczesnych standardów pisania kodu w JS.
2. **Zatrzymanie przeładowania:** Zablokuj domyślne zachowanie przeglądarki następujące po zatwierdzeniu danych.
3. **Pobieranie i typowanie danych:** Pobierz wartości wpisane przez użytkownika. Zadbaj o to, aby "Czas rezerwacji" miał odpowiedni typ danych, pozwalający na wykonywanie operacji matematycznych.
4. **Walidacja danych (Wczesny powrót):** Zastosuj architekturę Guard Clause, aby zabezpieczyć skrypt przed błędnymi danymi:
* W przypadku pustego pola z nickiem lub tytułem gry, wyświetl komunikat o błędzie i natychmiast przerwij działanie funkcji.
* W przypadku, gdy wpisany czas rezerwacji jest mniejszy od 1 lub w ogóle nie jest poprawną liczbą, wyświetl komunikat o błędzie i natychmiast przerwij funkcję.


5. **Logika i wynik:** Jeżeli wszystkie dane są poprawne, oceń długość sesji i wyświetl odpowiedni tekst w przygotowanym do tego elemencie HTML:
* Jeżeli czas rezerwacji wynosi **do 2 godzin włącznie**, wypisz: *„Stanowisko zarezerwowane. Gracz [Nick] ma przypisane [Czas] godziny na trening w grze [Tytuł gry].”*
* Jeżeli czas rezerwacji jest **dłuższy niż 2 godziny**, wypisz: *„Wniosek gracza [Nick] o sesję trwającą [Czas] godzin w [Tytuł gry] wymaga dodatkowej zgody administratora sali.”*



**⭐ Zadanie dodatkowe (na ocenę celującą - 6):**
Tuż po udanym wyświetleniu pozytywnego komunikatu (gdy formularz przejdzie całą walidację), skrypt powinien automatycznie wyczyścić zawartość wszystkich trzech pól wejściowych, przygotowując formularz na wpisanie kolejnego ucznia.

---

## Kryteria i system oceniania
**Skala procentowa:**

* **0% – 49%** (0 – 9,5 pkt): niedostateczny (1)
* **50% – 64%** (10 – 12,5 pkt): dopuszczający (2)
* **65% – 74%** (13 – 14,5 pkt): dostateczny (3)
* **75% – 89%** (15 – 17,5 pkt): dobry (4)
* **90% – 100%** (18 – 20 pkt): bardzo dobry (5)
* **Powyżej 100%** (100% z podstawy + wykonane zadanie dodatkowe): celujący (6)