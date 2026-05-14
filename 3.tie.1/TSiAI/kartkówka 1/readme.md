# Kartkówka: Tworzenie i obsługa formularzy (HTML + JS)

## Część 1: HTML (Struktura)
Stwórz w pliku HTML interfejs użytkownika zawierający następujące elementy:
1. Pole tekstowe na **Imię ucznia**.
2. Pole tekstowe na **Nazwisko ucznia**.
3. Pole numeryczne na **Ocenę ucznia**.
4. Przycisk z napisem (np. "Wystaw ocenę"), który po kliknięciu uruchomi odpowiednią funkcję w JavaScript.
5. Pusty element (np. akapit `<p>`), w którym wyświetli się ostateczny wynik.

*Wskazówka (WCAG): Pamiętaj, aby do każdego pola wejściowego dodać etykietę `<label>` i poprawnie powiązać ją z polem za pomocą atrybutów `for` oraz `id`.*

## Część 2: JavaScript (Logika)
Napisz funkcję, która zostanie wywołana po kliknięciu w przycisk z pierwszej części zadania. Skrypt powinien realizować następujące punkty:

1. **Pobieranie danych:** Przypisz do zmiennych wartości wpisane przez użytkownika w pola formularza oraz pobierz element, w którym wyświetlony zostanie wynik.
2. **Sprawdzanie danych:** Użyj instrukcji warunkowej, aby sprawdzić, czy wszystkie pola są wypełnione. Jeśli którekolwiek z pól jest puste, przerwij działanie funkcji (możesz też wypisać ostrzeżenie w konsoli).
3. **Wyświetlenie wyniku:** Jeżeli wszystkie dane zostały wpisane poprawnie, wypisz na stronie w przygotowanym elemencie tekst w formacie: 
   `<imię ucznia> <nazwisko ucznia> otrzymał(a) ocenę: <ocena>`

> ⭐ **Zadanie dodatkowe (na ocenę celującą - 6):**
> Rozbuduj walidację (sprawdzanie) z punktu 2. Zanim skrypt wypisze wynik na stronie, sprawdź, czy wpisana ocena jest poprawna, czyli czy jej wartość jest większa lub równa 1 **oraz** mniejsza lub równa 6. Jeśli ocena nie mieści się w tym przedziale, skrypt nie powinien wyświetlać wyniku.