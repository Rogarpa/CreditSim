export function AmortizationForm({ monto, setMonto, tasaAnual, setTasaAnual, plazoMeses, setPlazoMeses, getAmortizationTable }){
    return(
        <div className="form-container">
            <h2>Cálculo de Amortizacion</h2>
            <form onSubmit={getAmortizationTable}>
            <div>
                <input
                type="number"
                id="monto"
                name="monto"
                placeholder="Monto"
                value={monto}
                onChange={(e) => setMonto(e.target.value)}
                required
                />
            </div>
            <div>
                <input
                type="number"
                id="tasa_anual"
                name="tasa_anual"
                placeholder="Tasa anual"
                step="0.001"
                value={tasaAnual}
                onChange={(e) => setTasaAnual(e.target.value)}
                required
                />
            </div>
            <div>
                <input
                type="number"
                id="plazo_meses"
                name="plazo_meses"
                placeholder="Plazo a meses"
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