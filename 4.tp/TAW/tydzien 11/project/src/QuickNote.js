import { useEffect, useRef, useState } from "react"

function QuickNote(){
    const [nodeText, setNodeText] = useState(
        () => { 
            return localStorage.getItem("saved_note")

        }
    )
    const textareaRef = useRef()
    /*
    useEffect(() => {}, [])
    */
    useEffect(function(){textareaRef.current.focus()},[])
    useEffect(function(){
        document.title = "Zapisano Zmiany! - " + nodeText
        localStorage.setItem("saved_note", nodeText)
    },[nodeText])
    return(
        <>
            <textarea 
                value={nodeText}
                ref={textareaRef} 
                // onChange={function(e){setNodeText(e.target.value)}}
                onChange={(e) => { setNodeText(e.target.value)}}
            >  
            </textarea>
        </>
    )
}

export default QuickNote