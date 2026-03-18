function Card({title, descr, thumbnail}) {
    return (
    <>
        <div className="card w-25 m-1 sm:w-50">
            <img src={thumbnail} className="card-img-top" />
            <div className="card-body">
                <h5 className="card-title">{title}</h5>
                <p className="card-text">{descr}</p>
            </div>
        </div>
    </>
    )
}

export default Card