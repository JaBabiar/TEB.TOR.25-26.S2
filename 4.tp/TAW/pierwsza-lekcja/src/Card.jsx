function Card({Title, Tresc}){

    return(
        <>
            <div className="card">
                <h2>{Title}</h2>
                <div>
                    <p>
                        {Tresc}
                    </p>
                </div>
            </div>
        </>
    )
}

export default Card

