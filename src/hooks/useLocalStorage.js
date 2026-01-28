import { useState } from 'react'

export function useLocalStorage (key, initialValue){
    const getInitialValue = (() => {
        try{
            const item = window.localStorage.getItem(key)
            return item? JSON.parse(item) : initialValue
        } catch (error) {
            return initialValue
        }
    })
    const [storedValue, setStoredValue] = useState(getInitialValue)
    
    const setValue = (value) => {
        try{
            setStoredValue(value)
            window.localStorage.setItem(key, JSON.stringify(value))
        }catch(error){
            throw new Error("Local storage writing unavailable")
        }
    }
    return [storedValue, setValue]
}