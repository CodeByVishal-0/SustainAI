const getAQIColor = (aqi) => {
  if (aqi === 1) return "text-green-600";
  if (aqi === 2) return "text-lime-500";
  if (aqi === 3) return "text-yellow-500";
  if (aqi === 4) return "text-orange-500";
  return "text-red-600";
};

function WeatherCard({ weather }) {
  if (!weather) return null;

  return (
    <div className="bg-white rounded-xl shadow p-6 hover:shadow-lg transition">

      <h2 className="text-xl font-bold mb-4">
        🌤 Weather Information
      </h2>

      <div className="space-y-3">

        <p>
          🌡 Temperature:
          <span className="font-semibold ml-2">
            {weather.temperature}°C
          </span>
        </p>

        <p>
          💧 Humidity:
          <span className="font-semibold ml-2">
            {weather.humidity}%
          </span>
        </p>

        <p>
          🌫 AQI:
          <span
            className={`font-bold ml-2 ${getAQIColor(
              weather.aqi
            )}`}
          >
            {weather.aqi}
          </span>
        </p>

        <p>
          ☁ Condition:
          <span className="font-semibold ml-2">
            {weather.weather}
          </span>
        </p>

      </div>

    </div>
  );
}

export default WeatherCard;