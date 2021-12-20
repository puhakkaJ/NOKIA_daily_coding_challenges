import React from 'react'

const GenreButton = ({ setGenre, genre }) => {
    return (
        <button onClick={() => setGenre(genre)}>genre</button>
    )
}

export default GenreButton