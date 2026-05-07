
# Zadanie: Pobieranie i weryfikacja danych (INF.03)

## HTML
W pliku `index.html` wygeneruj strukturę, korzystając z poniższego schematu Emmet (bez użycia bloku `<form>`):

```text
(label+input)*2+button
```

**Wymagania techniczne:**
1.  **Pierwsze pole:** Etykieta "Imię", pole typu tekstowego.
2.  **Drugie pole:** Etykieta "Wiek", pole typu liczbowego.
3.  **Przycisk:** Napis "Sprawdź dane".
4.  **Dostępność:** Każdy `label` musi być powiązany z odpowiednim polem `input` za pomocą atrybutów `for` oraz `id`.

## Krok 2: Skrypt JavaScript
W pliku `script.js` (lub wewnątrz znacznika `<script>`) napisz kod, który:

1.  Zostanie uruchomiony po kliknięciu przycisku.
2.  Pobierze wartości z obu pól do zmiennych.
3.  **Przeprowadzi walidację:**
    * Sprawdzi, czy pole "Imię" nie jest puste.
    * Sprawdzi, czy pole "Wiek" zawiera wartość większą od 0.
4.  **Wyświetli wynik w konsoli:**
    * Jeśli dane są poprawne: `Witaj [Imię], Twój wiek to [Wiek]`.
    * Jeśli dane są błędne: `Wprowadzono niepoprawne dane`.
