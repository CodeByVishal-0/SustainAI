import {
  CircularProgressbar,
  buildStyles
} from "react-circular-progressbar";

import "react-circular-progressbar/dist/styles.css";

const getRiskColor = (risk) => {
  if (risk === "Low") return "#16a34a";
  if (risk === "Moderate") return "#eab308";
  if (risk === "High") return "#f97316";
  return "#dc2626";
};

function ScoreCard({ impact }) {
  if (!impact) return null;

  return (
    <div className="bg-white rounded-xl shadow p-6">

      <h2 className="text-xl font-bold mb-6">
        Sustainability Score
      </h2>

      <div className="w-40 h-40 mx-auto">

        <CircularProgressbar
          value={impact.score}
          text={`${impact.score}`}
          styles={buildStyles({
            pathColor: getRiskColor(
              impact.risk_level
            ),
            textColor: "#111827"
          })}
        />

      </div>

      <p className="text-center mt-4">
        Risk Level:
        <span
          className="font-bold ml-2"
          style={{
            color: getRiskColor(
              impact.risk_level
            )
          }}
        >
          {impact.risk_level}
        </span>
      </p>

    </div>
  );
}

export default ScoreCard;