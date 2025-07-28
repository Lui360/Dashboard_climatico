import "../ControlPanel.css";
const ciudades = [
  "Madrid",
  "Valencia",
  "Barcelona",
  "Sevilla",
  "Leon",
  "Oviedo",
  "Badajoz",
  "Santiago de Compostela",
];

const variables = {
  T2M: "Temperatura (°C)",
  RH2M: "Humedad Relativa (%)",
  PRECTOTCORR: "Precipitación (mm)",
};

const modos = {
  chart: "Gráfico",
  tabla: "Tabla",
};

const ControlPanel = ({
  ciudad,
  setCiudad,
  variable,
  setVariable,
  modo,
  setModo,
  modoFecha,
  setModoFecha,
  fechaInicio,
  setFechaInicio,
  fechaFin,
  setFechaFin,
  handleFetch,
}) => {
  return (
    <div className="control-panel">
      <label>
        Ciudad:
        <select value={ciudad} onChange={(e) => setCiudad(e.target.value)}>
          {ciudades.map((c) => (
            <option key={c} value={c}>
              {c}
            </option>
          ))}
        </select>
      </label>
      <label>
        Variable:
        <select value={variable} onChange={(e) => setVariable(e.target.value)}>
          {Object.entries(variables).map(([key, label]) => (
            <option key={key} value={key}>
              {label}
            </option>
          ))}
        </select>
      </label>
      <label>
        Modo:
        <select value={modo} onChange={(e) => setModo(e.target.value)}>
          <option value="chart">Gráfico</option>
          <option value="tabla">Tabla</option>
        </select>
      </label>
      <label>
        Ver datos:
        <select
          value={modoFecha}
          onChange={(e) => setModoFecha(e.target.value)}
        >
          <option value="ultimos30">Últimos 30 días</option>
          <option value="rango">Seleccionar fechas</option>
        </select>
      </label>
      {modoFecha === "rango" && (
        <>
          <label>
            Desde:
            <input
              type="date"
              value={fechaInicio}
              onChange={(e) => setFechaInicio(e.target.value)}
            />
          </label>
          <label>
            Hasta:
            <input
              type="date"
              value={fechaFin}
              onChange={(e) => setFechaFin(e.target.value)}
            />
          </label>
        </>
      )}
      <div className="button-wrapper">
        <button onClick={handleFetch}>Obtener Datos</button>
      </div>
    </div>
  );
};

export default ControlPanel;
