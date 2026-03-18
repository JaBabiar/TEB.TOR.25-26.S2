import { useRef, useState } from 'react';
import './App.css';
import gryData from './gry.json'
import Card from './Card';
function App() {
    let nazwaGryRef = useRef('');
    const [gry, setGry] = useState(gryData.map((gra) => <Card key={gra.id} title={gra.title} descr={gra.short_description} thumbnail={gra.thumbnail} />))

    
    function szukajGry(e){
        e.preventDefault()
        let szukane = nazwaGryRef.current.value
        let filtrowaneGry = gryData.filter((g) => g.title.indexOf(szukane) > -1)
        setGry(filtrowaneGry.map((gra) => <Card key={gra.id} title={gra.title} descr={gra.short_description} thumbnail={gra.thumbnail} />))
    }
    
    
    
    return (
        <>
        <form onSubmit={szukajGry}>
            <input
                name='nazwaGry'
                className='input-text'
                id='nazwaGry'
                ref={nazwaGryRef}/>
            <input type="submit" value={"testowanie"} />
        </form>

        <section className='container-lg d-flex flex-wrap'>
            {gry}
        </section>
        </>
    )
}

export default App;