import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const ChartView = ({ data }) => (
  <ResponsiveContainer width="100%" height={300}>
    <LineChart data={data}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="fecha" tick={{ fontSize: 10 }} />
      <YAxis />
      <Tooltip />
      <Line type="monotone" dataKey="valor" stroke="#00d8ff" dot={false} />
    </LineChart>
  </ResponsiveContainer>
);

export default ChartView;
