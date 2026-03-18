import { useRef, useState } from 'react';
import './App.css';


function AppEgzamin() {
  const listaKursow = [
    "Programowanie w C#",
    "Angular dla początkujących",
    "Kurs Django",
    "INF 04 w 2 miesiace"
  ]
  const imieNazwiskoRef = useRef('');
  const numerKursuRef = useRef('')

  function handleSubmit(e){
    e.preventDefault()
    const imienazwisko = imieNazwiskoRef.current.value;
    const numerKursu = numerKursuRef.current.value;
    const kurs = listaKursow[numerKursu-1]
    if(!kurs){
      console.error("Błędny numer kursu")
      return
    }

    console.log(kurs)
  

  }

  

  return (
    <>
      <h2>Liczba Kursow: {listaKursow.length}</h2>
      <ol>
        {listaKursow.map((kurs,index) => (
          <li key={index}>{kurs}</li>
        ))}
      </ol>

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="imienazwisko">Imię i nazwisko:</label>
          <input
            type="text"
            id="imienazwisko"
            name="imienazwisko"
            className="form-control"
            ref={imieNazwiskoRef}
          />
        </div>
        <div className="form-group">
          <label htmlFor="numerkursu">Numer kursu:</label>
          <input
            type="number"
            id="numerkursu"
            name="numerkursu"
            className="form-control"
            ref={numerKursuRef}
          />
        </div>
        <div className="form-group mt-3">
          <button type="submit" className="btn btn-primary">
            Zapisz do kursu
          </button>
        </div>
      </form>

    </>
  );
}

export default AppEgzamin;