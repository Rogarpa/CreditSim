
export class Constants{
    // Amortization module
    static AMORTIZATION_API_ENDPOINT= "https://creditaria-technical-test-api.fly.dev/simulate";
    static TABLE_FETCH_ERROR_MSG = 'Ocurrio un error al obtener la tabla de amortización'
    static TABLE_ENDPOINT_ERROR_MSG = "Amortization endpoint unsuccessfull response"
    static TABLE_DATA_ERROR_MSG = "Data syntax error"
    static MONTO= "monto";
    static MONTO_FIELD_PLACEHOLDER= "Monto";
    static MONTO_INITIAL_VALUE= "";
    static TASA_ANUAL= "tasa_anual";
    static TASA_ANUAL_FIELD_PLACEHOLDER= "Tasa anual (%)";
    static TASA_ANUAL_INITIAL_VALUE= "";
    static PLAZO_MESES= "plazo_meses";
    static PLAZO_MESES_FIELD_PLACEHOLDER= "Plazo en meses";
    static PLAZO_MESES_INITIAL_VALUE= "";
    static TABLE_INITIAL_STATE= undefined;
    // Fetch function
    static FETCH_POST_METHOD= 'POST';
    static CONTENT_TYPE_HEADER= {'Content-Type': 'application/json'};
    // Hooks
    static USE_LOCAL_STORAGE_ERROR_MSG= 'Local storage writing unavailable';
    
}
export default Constants

































