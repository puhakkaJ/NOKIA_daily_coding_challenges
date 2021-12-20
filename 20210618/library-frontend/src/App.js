
import React, { useState } from 'react'
import { useQuery } from '@apollo/client'

import Authors from './components/Authors'
import SetBirth from './components/SetBirth'
import Books from './components/Books'
import NewBook from './components/NewBook'
import { ALL_BOOKS } from './queries'
import { ALL_AUTHORS } from './queries'


const App = () => {
  const [errorMessage, setErrorMessage] = useState(null)
  const [page, setPage] = useState('authors')

  const authors = useQuery(ALL_AUTHORS)
  const books = useQuery(ALL_BOOKS)

  if (authors.loading) {
    return <div>loading...</div>
  }

  if (books.loading) {
    return <div>loading...</div>
  }

  const notify = (message) => {
    setErrorMessage(message)
    setTimeout(() => {
      setErrorMessage(null)
    }, 10000)
  }


  return (
    <div>
      <div>
        <button onClick={() => setPage('authors')}>authors</button>
        <button onClick={() => setPage('books')}>books</button>
        <button onClick={() => setPage('add')}>add book</button>
      </div>

      <Authors
        show={page === 'authors'} authors={authors.data.allAuthors}
      />

      <SetBirth
        show={page === 'authors'} authors={authors.data.allAuthors}
      />

      <Books
        show={page === 'books'} books={books.data.allBooks}
      />

      <NewBook
        show={page === 'add'} setError={notify} errorMessage={errorMessage}
      />

    </div>
  )
}

export default App