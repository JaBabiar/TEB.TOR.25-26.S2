import { useEffect, useRef, useState } from "react"

function Counter(){
    const [count, setCount] = useState(0)
    const prevCount = useRef()
    // Klikamy +
    // React dostaje zmiane na elemencie count 
    // wykonuje się useEffect z [count]
    // Wykonuje się oryginalna funkcja setCount
    useEffect(function(){
        prevCount.current = count
    }, [count])

    function dodajJeden(){
        setCount(count+1)
    }

    return(
        <>
            <p>Aktualnie: {count}</p>
            <p>Poprzednia: {prevCount.current}</p>
            <button onClick={() => setCount(count-1)}>-</button>
            <button onClick={dodajJeden}>+</button>
        </>
    )
}

export default Counter