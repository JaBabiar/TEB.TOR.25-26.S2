# Podstawowe Hooki React: useState, useRef, useEffect

### 1. useState – Zarządzanie Stanem

Służy do przechowywania danych, które **zmieniają się w czasie** i na których zmianę React ma zareagować **ponownym wyrenderowaniem komponentu**.

* **Zastosowanie:** Formularze, liczniki, przełączniki, dane z API.
* **Działanie:** Wywołanie funkcji ustawiającej stan (np. `setCount`) wymusza na React odświeżenie widoku.

```javascript
const [count, setCount] = useState(0);

function handleIncrement() {
  setCount(count + 1);
}

// Wykorzystanie w przycisku:
<button onClick={handleIncrement}>Dodaj</button>

```

---

### 2. useRef – Referencje i "Cicha Pamięć"

Tworzy obiekt, który przechowuje wartość przez cały cykl życia komponentu, ale **jej zmiana NIE powoduje ponownego wyrenderowania**.

* **Zastosowanie:**
1. Dostęp do elementów DOM (np. ręczne ustawienie focusa).
2. Przechowywanie zmiennych, które nie wpływają na wygląd (np. timery).


* **Działanie:** Dostęp do danych odbywa się zawsze przez `ref.current`.

```javascript
const inputRef = useRef(null);

function focusInput() {
  inputRef.current.focus(); 
}

<input ref={inputRef} type="text" />
<button onClick={focusInput}>Ustaw kursor w polu</button>

```

---

### 3. useEffect – Efekty Uboczne

Służy do synchronizacji komponentu z zewnętrznymi systemami lub wykonywania kodu w określonych momentach.

* **Zastosowanie:** Pobieranie danych, ustawianie nasłuchiwania zdarzeń (event listeners).
* **Logika działania:**
* `[]` – tylko raz przy uruchomieniu.
* `[zmienna]` – przy uruchomieniu i każdej zmianie `zmiennej`.



```javascript
useEffect(function() {
  console.log("Efekt uruchomiony!");

  return function cleanup() {
    console.log("Sprzątanie przed usunięciem komponentu.");
  };
}, [count]);

```

---

### Podsumowanie dla programisty

| Hook | Re-render? | Główny cel |
| --- | --- | --- |
| **useState** | **Tak** | Dane, które muszą być widoczne na ekranie. |
| **useRef** | **Nie** | Odwołania do DOM i zmienne "techniczne". |
| **useEffect** | Zależy od deps | Logika poza samym renderowaniem (np. API). |
