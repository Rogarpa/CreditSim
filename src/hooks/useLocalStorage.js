import { useState } from 'react'
import Constants from'../utils/Constants';

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
            throw new Error(Constants.USE_LOCAL_STORAGE_ERROR_MSG.toString())
        }
    }
    return [storedValue, setValue]
}