import React, { useState, useEffect } from 'react';
import { AmortizationForm } from './AmortizationForm'
import { useLocalStorage } from '../hooks/useLocalStorage'
import { Table } from '../components/Table'

function AmortizationModule(){

  const [monto, setMonto] = useLocalStorage("monto", "");
  const [tasaAnual, setTasaAnual] = useLocalStorage("tasaAnual", "");
  const [plazoMeses, setPlazoMeses] = useLocalStorage("plazoMeses", "");
  const [table, setTable] = useState(undefined);
  const [firstReactCycle, setFirstReactCycle] = useState(true);

  useEffect(() => {
    if(firstReactCycle){
      setFirstReactCycle(false)
      return
    }
    setTable(undefined)
  },[monto, firstReactCycle])

  async function getAmortizationTable (event) {
    event.preventDefault();

    const amortizationData = {
      "monto": monto,
      "tasa_anual": tasaAnual,
      "plazo_meses": plazoMeses
    }
    
    fetch('http://creditaria-technical-test.fly.dev/simulate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ''
        },
        body: JSON.stringify(amortizationData),
      }).then((data) => {
        console.log(data)
        return data.json()
      }).then((data) => setTable(data)).catch(error => {
      console.log(error);
    });

    
    setMonto("")
    setTasaAnual("")
    setPlazoMeses("")
  }

  return (
    <div className='amortization-container'>
      <AmortizationForm 
      monto = {monto}
      setMonto = {setMonto}
      plazoMeses = {plazoMeses}
      setPlazoMeses = {setPlazoMeses}
      tasaAnual = {tasaAnual}
      setTasaAnual = {setTasaAnual}
      getAmortizationTable = {getAmortizationTable}
      />

      {!table? "":(
      <Table
        nodes = {table.amortization_periods}
      />)}
       
      
      
    </div>
    
  );
}
export default AmortizationModule;
