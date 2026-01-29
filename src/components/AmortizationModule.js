import React, { useState, useEffect } from 'react'
import { useLocalStorage } from '../hooks/useLocalStorage'
import { Table } from '../components/Table'
import Constants from'../utils/Constants'
import { AmortizationResponseSchema } from '../schemas/AmortizationTableSchema'

function AmortizationModule(){

  const [monto, setMonto] = useLocalStorage(Constants.MONTO.toString(), Constants.MONTO_INITIAL_VALUE);
  const [tasaAnual, setTasaAnual] = useLocalStorage(Constants.TASA_ANUAL.toString(), Constants.TASA_ANUAL_INITIAL_VALUE);
  const [plazoMeses, setPlazoMeses] = useLocalStorage(Constants.PLAZO_MESES.toString(), Constants.PLAZO_MESES_INITIAL_VALUE);
  const [table, setTable] = useState(Constants.TABLE_INITIAL_STATE);
  const [firstReactCycle, setFirstReactCycle] = useState(true);
  const [tableError, setTableError] = useState(undefined);

  useEffect(() => {
    if(firstReactCycle){
      setFirstReactCycle(false)
      return
    }
    setTable(undefined)
  },[monto, firstReactCycle])

  async function getAmortizationTable (event) {
    event.preventDefault();
    
    setTableError(undefined)
    const amortizationData = {}
    amortizationData[Constants.MONTO.toString()] = monto
    amortizationData[Constants.TASA_ANUAL.toString()] = tasaAnual
    amortizationData[Constants.PLAZO_MESES.toString()] = plazoMeses
    
    
    
    fetch(Constants.AMORTIZATION_API_ENDPOINT, {
        method: Constants.FETCH_POST_METHOD,
        headers: {
          ...Constants.CONTENT_TYPE_HEADER,
        },
        body: JSON.stringify(amortizationData),
      }).then((response) => {
        if(!response.ok){
          throw new Error("Amortization endpoint unsuccessfull response")
        }
        return response.json()
      }).then((data) => {
        if(!data || !AmortizationResponseSchema.safeParse(data).success){
          throw new Error(Constants.TABLE_FETCH_ERROR_MSG.toString())  
        }
        setTable(data.amortization_periods)
        
      }).catch(error => {
        setTableError({msg: error.message})
    });
    setMonto(Constants.MONTO_INITIAL_VALUE)
    setTasaAnual(Constants.MONTO_INITIAL_VALUE)
    setPlazoMeses(Constants.MONTO_INITIAL_VALUE)
  }

  return (
    <div className='amortization-container'>
      <div className="form-container">
            <h2>Cálculo de Amortizacion</h2>
            <form onSubmit={getAmortizationTable}>
              <input
              type="number"
              id={Constants.MONTO}
              name={Constants.MONTO}
              placeholder={Constants.MONTO_FIELD_PLACEHOLDER}
              value={monto}
              onChange={(e) => setMonto(e.target.value)}
              required
              />
              <input
              type="number"
              id={Constants.TASA_ANUAL}
              name={Constants.TASA_ANUAL}
              placeholder={Constants.TASA_ANUAL_FIELD_PLACEHOLDER}
              value={tasaAnual}
              onChange={(e) => setTasaAnual(e.target.value)}
              required
              />
              <input
              type="number"
              id={Constants.PLAZO_MESES}
              name={Constants.PLAZO_MESES}
              placeholder={Constants.PLAZO_MESES_FIELD_PLACEHOLDER}
              value={plazoMeses}
              onChange={(e) => setPlazoMeses(e.target.value)}
              required
              />
            <button type="submit" >Calcular</button>
            </form>
            <p>{tableError?tableError.msg:""}</p>
        </div>
      {!table? "":(
        <Table
          nodes = {table}
      />)}
       
      
      
    </div>
    
  );
}
export default AmortizationModule;
