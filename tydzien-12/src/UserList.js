import { useEffect, useRef, useState } from "react"

function UserList(){
    const [lista, setLista] = useState(["Admin", "Adam", "Uczen"])
    const [tekst, setTekst] = useState("")
    const tekstRef = useRef();

    function zmianaTekstu(){
        setTekst(tekstRef.value)
    }

    useEffect(function(){
        lista.filter((element) => element.indexOf(tekst) > -1)
    }, [tekst])
    return(
        <>
            <input 
                value={tekst}
                onChange={zmianaTekstu()}
                ref={tekstRef}
            />

            {UserList}
        </>
    )
}
export default UserList