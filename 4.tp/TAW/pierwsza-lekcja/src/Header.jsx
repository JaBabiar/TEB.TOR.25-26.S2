
function Header(props) {
    const links = props.sigiemka
    const liElems = links.map(link => <li key={link}>{link}</li>)
    console.log(liElems)
  return (
    <>
    <header>
        <figure>
            <img alt="" />
        </figure>
        <nav>
           <ul>
            {liElems}
           </ul>
        </nav>
    </header>
    </>
  )
}

export default Header
