const TableView = ({ data, variable }) => (
  <table
    style={{
      background: "#111",
      color: "#fff",
      borderCollapse: "collapse",
      marginTop: "1rem",
      width: "100%",
    }}
  >
    <thead>
      <tr>
        <th style={{ border: "1px solid #333", padding: "0.5rem" }}>Fecha</th>
        <th style={{ border: "1px solid #333", padding: "0.5rem" }}>
          {variable}
        </th>
      </tr>
    </thead>
    <tbody>
      {data.map(({ fecha, valor }) => (
        <tr key={fecha}>
          <td style={{ border: "1px solid #333", padding: "0.5rem" }}>
            {fecha}
          </td>
          <td style={{ border: "1px solid #333", padding: "0.5rem" }}>
            {valor}
          </td>
        </tr>
      ))}
    </tbody>
  </table>
);

export default TableView;
