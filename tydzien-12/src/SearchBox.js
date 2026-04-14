import { useEffect, useState, useRef } from "react"

function SearchBox() {
    const [value, setValue] = useState('');
    const inputRef = useRef(null)

    useEffect(function(){
        inputRef.current.focus()
    },[])

    function handleKeyDown(e){
        if(e.key == "Enter"){
            console.log(value)
        }
    }
    return(
        <>
            <div>
                <input 
                    type="text"
                    ref={inputRef}
                    value={value.value}
                    onChange={(e) => setValue(e.target.value)}
                    onKeyDown={handleKeyDown}
                    placeholder="sdhbfdajhb"
                    />
                    <p>Znaki: {value.length}</p>
            </div>
        </>
    )
}
export default SearchBox