
import './App.css';
import { useEffect, useRef, useState } from 'react';
import Kompot from './Kompot';

function App() {
  const [name, setName] = useState('')
  const textRef = useRef('')
  const [elems, setElems] = useState([])
  const autor = useRef('')
  const title = useRef('')
  const genre = useRef('')

  function handleTextRefChange(){
    setName(textRef.current.value)
  }
  function handleFormUpload(){
    console.log(title.current.value)
    console.log(autor.current.value)
    console.log(genre.current.value)

    setElems(prev => [...prev, [title.current.value, autor.current.value, genre.current.value]]);
  }

  useEffect(function(){
    console.log(elems)    
  }, [elems])
  return (
    <>
      <form onSubmit={(e) => e.preventDefault()}>

        <label for="title">Tytuł</label>
        <input type="text" name="title" id="title" ref={title}/>
        
        <label for="author">Autor</label>
        <input type="text" name="author" id="author" ref={autor}/>
        
        <label for="genre">Gatunek</label>
        <input type="text" name="genre" id="genre" ref={genre}/>

        <button onClick={handleFormUpload}>Dodaj</button>
      </form>

      {String(elems)}

      <Kompot />
    </>
  );
}

export default App;
