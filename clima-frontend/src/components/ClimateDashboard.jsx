import { useState } from "react";
import { motion } from "framer-motion";
import ControlPanel from "./ControlPanel";
import ChartView from "./ChartView";
import TableView from "./TableView";

const variables = {
  T2M: "Temperatura (°C)",
  RH2M: "Humedad Relativa (%)",
  PRECTOTCORR: "Precipitación (mm)",
};

const ClimateDashboard = () => {
  const [ciudad, setCiudad] = useState("Madrid");
  const [variable, setVariable] = useState("T2M");
  const [modo, setModo] = useState("chart");
  const [modoFecha, setModoFecha] = useState("ultimos30");
  const [fechaInicio, setFechaInicio] = useState("");
  const [fechaFin, setFechaFin] = useState("");
  const [datos, setDatos] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFetch = async () => {
    setLoading(true);
    setError("");
    setDatos(null);

    try {
      const res = await fetch(`http://127.0.0.1:8000/clima?ciudad=${ciudad}`);
      const json = await res.json();

      if (json.error) {
        setError(json.error);
      } else {
        setDatos(json.data);
      }
    } catch (err) {
      setError("Error al conectar con el backend");
    } finally {
      setLoading(false);
    }
  };

  let dataFormateada = [];

  if (datos?.[variable]) {
    const rawEntries = Object.entries(datos[variable]);

    let filtrado;

    if (modoFecha === "ultimos30") {
      filtrado = rawEntries.slice(-30);
    } else {
      filtrado = rawEntries.filter(([fecha]) => {
        return (
          (!fechaInicio || fecha >= fechaInicio.replaceAll("-", "")) &&
          (!fechaFin || fecha <= fechaFin.replaceAll("-", ""))
        );
      });
    }

    dataFormateada = filtrado.map(([fecha, valor]) => ({
      fecha,
      valor,
    }));
  }

  return (
    <motion.div
      style={{ padding: "1rem" }}
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.5 }}
    >
      <h1>🌦️ Dashboard Climático</h1>

      <ControlPanel
        ciudad={ciudad}
        setCiudad={setCiudad}
        variable={variable}
        setVariable={setVariable}
        modo={modo}
        setModo={setModo}
        modoFecha={modoFecha}
        setModoFecha={setModoFecha}
        fechaInicio={fechaInicio}
        setFechaInicio={setFechaInicio}
        fechaFin={fechaFin}
        setFechaFin={setFechaFin}
        handleFetch={handleFetch}
      />

      {loading && (
        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: [0.2, 1, 0.2] }}
          transition={{ repeat: Infinity, duration: 1.2 }}
          style={{ fontStyle: "italic", color: "#00d8ff" }}
        >
          🔄 Consultando satélites...
        </motion.p>
      )}

      {error && <p style={{ color: "red" }}>{error}</p>}

      {!loading && datos && dataFormateada.length > 0 && (
        <motion.div
          initial={{ y: 30, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ type: "spring", stiffness: 60 }}
        >
          <h3>{variables[variable]}</h3>
          {modo === "chart" ? (
            <ChartView data={dataFormateada} />
          ) : (
            <TableView data={dataFormateada} variable={variables[variable]} />
          )}
        </motion.div>
      )}
    </motion.div>
  );
};

export default ClimateDashboard;
