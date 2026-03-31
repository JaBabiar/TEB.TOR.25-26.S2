# Pobieranie Danych z Formularzy i Pola Radio

## 1. Odczytywanie wartości z pól tekstowych i liczbowych

Aby pobrać to, co użytkownik wpisał w pole `<input>` (np. typu `text` lub `number`), używamy właściwości `.value`.

* **Ważne:** Wszystko, co pobieramy z formularza, jest domyślnie traktowane przez przeglądarkę jako tekst (String).
* Jeśli pobieramy dane z pól `n1` i `n2` z zamiarem wykonania obliczeń matematycznych, musimy zamienić ten tekst na prawdziwą liczbę używając `parseFloat(zmienna.value)` lub `parseInt(zmienna.value)`. W przeciwnym razie operacja dodawania "2" + "2" da nam "22", a nie 4.

## 2. Obsługa pól wielokrotnego wyboru (Radio i Checkbox)

W przypadku pól typu `radio` (wybór jednej opcji z wielu) oraz `checkbox` (wybór wielu opcji), samo sprawdzenie `.value` nie wystarczy. Musimy wiedzieć, czy element został w ogóle zaznaczony.

* Służy do tego właściwość `.checked`, która zwraca wartość logiczną: `true` (zaznaczone) lub `false` (niezaznaczone).
* W podstawowym podejściu możemy pobrać każdy przycisk radio oddzielnie i użyć instrukcji warunkowej `if (element.checked == true)`, aby sprawdzić jego stan.

## 3. Optymalizacja za pomocą `querySelectorAll`

Gdy mamy wiele przycisków radio należących do tej samej grupy (ten sam atrybut `name="typ"`), pisanie osobnego `if` dla każdego z nich jest uciążliwe.

* Zamiast tego możemy pobrać całą grupę naraz za pomocą `document.querySelectorAll('input[name="typ"]')`.
* Funkcja ta zwraca listę wszystkich pasujących elementów. Następnie możemy użyć pętli `forEach`, aby przejść przez każdy element i sprawdzić, który z nich ma status `checked == true`. To znacznie czystsze i bardziej profesjonalne podejście!

## 💡 Dostępność cyfrowa (WCAG) - Etykiety to podstawa

* **Poprawne powiązanie:** Przyciski operacji matematycznych (dodawanie, odejmowanie itp.) zostały poprawnie powiązane z etykietami `<label>` za pomocą atrybutów `for` oraz `id`. Dzięki temu użytkownik może kliknąć w sam tekst "dodawanie", aby zaznaczyć kółko obok. Jest to kluczowe dla osób z niepełnosprawnościami motorycznymi.
* **Brakujące etykiety:** Zwróć uwagę, że pola na liczby (`#n1` i `#n2`) nie posiadają znaczników `<label>`. Czytnik ekranowy po napotkaniu takiego pola powie tylko "Pole edycji", nie informując użytkownika, co powinien tam wpisać. Zawsze używaj `<label>`!
