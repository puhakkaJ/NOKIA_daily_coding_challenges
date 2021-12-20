import React, { useState, useEffect } from 'react'
import Select from 'react-select'
import { useMutation } from '@apollo/client'

import { EDIT_AUTHOR, ALL_AUTHORS } from '../queries'
import Notification from './Notification'


const SetBirth = (props) => {
    const [selectedOption, setSelectedOption] = useState(null)
    const [errorMessage, setError] = useState(null)
    const [born, setBorn] = useState('')

    const options = props.authors.map(author => { return { value: author.name, label: author.name } })

    const [editAuthor, result] = useMutation(EDIT_AUTHOR, {
        refetchQueries: [{ query: ALL_AUTHORS }],
        onError: (error) => {
            setError(error.graphQLErrors[0].message)
        }
    })

    useEffect(() => {
        if (result.data && result.data.editAuthor === null) {
            setError('author not found')
        }
    }, [result.data])

    if (!props.show) {
        return null
    }

    const submit = (event) => {
        event.preventDefault()
        console.log('update birthdate...')

        const name = selectedOption.value

        editAuthor({ variables: { name, born } })

        setSelectedOption(null)
        setBorn('')
    }

    return (
        <div>
            <Notification errorMessage={errorMessage} />
            <h2>Set birthyear</h2>
            <form onSubmit={submit}>
                <div>
                    Choose name:
                    <Select
                        defaultValue={selectedOption}
                        onChange={setSelectedOption}
                        options={options}
                    />
                </div>
                <div>
                    born:
                    <input
                        value={born}
                        onChange={({ target }) => setBorn(target.value)}
                    />
                </div>
                <button type='submit'>update author</button>
            </form>
        </div>
    )

}

export default SetBirth
