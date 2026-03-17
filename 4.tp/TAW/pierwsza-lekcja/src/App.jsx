import './App.css'
import Header from './Header'
import Card from './Card'

/*
npx create-react-app@latest [nazwa_folderu]
cd [nazwa_folderu]
npm install 
npm strat

*/
function App() {

  const lista = [
    {"id": 1, "title": "Pan Tadeusz", "tresc": "lowkey slaba lektura"},
    {"id": 2, "title": "One Piece", "tresc": "Nowa Biblia"},
    {"id": 3, "title": "Jądro Ciemności", "tresc": "Pani kazała przeczytac"}
  ]
  const elementy = lista.map((el) => <Card key={el.id} Title={el.title} Tresc={el.tresc} />)

  return (
    <>
    <Header />
      <section className='data-container'>
        {elementy}
      </section>

      <section>
        
      </section>
    </>
  )
}

export default App
