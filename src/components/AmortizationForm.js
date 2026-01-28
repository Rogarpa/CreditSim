export function AmortizationForm({monto, setMonto, tasaAnual, setTasaAnual, plazoMeses, setPlazoMeses, getAmortizationTable}){
    return(
        <div>
            <h2>Formulario de Cálculo de Préstamo</h2>
            <form onSubmit={getAmortizationTable}>
            <div>
                <label htmlFor="monto">Monto:</label>
                <input
                type="number"
                id="monto"
                name="monto"
                value={monto}
                onChange={(e) => setMonto(e.target.value)}
                required
                />
            </div>
            <div>
                <label htmlFor="tasa_anual">Tasa Anual (%):</label>
                <input
                type="number"
                id="tasa_anual"
                name="tasa_anual"
                step="0.01"
                value={tasaAnual}
                onChange={(e) => setTasaAnual(e.target.value)}
                required
                />
            </div>
            <div>
                <label htmlFor="plazo_meses">Plazo (Meses):</label>
                <input
                type="number"
                id="plazo_meses"
                name="plazo_meses"
                value={plazoMeses}
                onChange={(e) => setPlazoMeses(e.target.value)}
                required
                />
            </div>
            <button type="submit" >Calcular</button>
            </form>
        </div>
    )
}
export default AmortizationForm;