import React, { useState, useRef } from 'react';
import {AmortizationForm} from './AmortizationForm'
function AmortizationModule(){

  const [monto, setMonto] = useState(0);
  const [tasaAnual, setTasaAnual] = useState(0);
  const [plazoMeses, setPlazoMeses] = useState(0);
  const [table, setTable] = useState({});

  async function getAmortizationTable (event) {
    event.preventDefault();

    const amortizationData = {
      "monto": monto,
      "tasa_anual": tasaAnual,
      "plazo_meses": plazoMeses
    }
    let response
    
    response = fetch('http://localhost:8000/simulate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(amortizationData),
      }).then((data) => {
        return data.json()
      }).then((data) => setTable(data)).catch(error => {
      console.log(error);
    });

    
    setMonto("")
    setTasaAnual("")
    setPlazoMeses("")
  }

  return (
    <div>
      <AmortizationForm 
      monto = {monto}
      setMonto = {setMonto}
      plazoMeses = {plazoMeses}
      setPlazoMeses = {setPlazoMeses}
      tasaAnual = {tasaAnual}
      setTasaAnual = {setTasaAnual}
      getAmortizationTable = {getAmortizationTable}
      />
      <p>{table?(JSON.stringify(table)):"loading"}</p>
      <p>{monto}</p>
      <p>{tasaAnual}</p>
      <p>{plazoMeses}</p>
      
    </div>
    
  );
}
export default AmortizationModule;
