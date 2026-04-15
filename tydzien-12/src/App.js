/*
Z1 
- wyświetla licznik i przyciski + i - 
- useState do przechowywania wartości 
- useRef do zapisania poprzedniej wartości i wyświetlania 
- useEffect do aktualizacji przy każdej zmianie count 

Z2 
- Komponent SearchBox
- pole input z useState 
- Automatycznie focus na starcie strony 
- po naciśnięciu enter wypisuje w konsoli i czyści input 
- Wyświetla liczbe znaków poniżej pola


*/

import Counter from "./Counter";
import SearchBox from "./SearchBox";

function App() {
  return (
    <>
      <Counter />
      <SearchBox />
    </>
  );
}

export default App;
