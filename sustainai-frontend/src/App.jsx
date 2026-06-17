import { useState } from "react";
import API from "./services/api";

import Header from "./components/Header";
import SearchForm from "./components/SearchForm";
import ScoreCard from "./components/ScoreCard";
import WeatherCard from "./components/WeatherCard";
import NewsSection from "./components/NewsSection";
import ReportSection from "./components/ReportSection";
import Footer from "./components/Footer";

import { ClipLoader } from "react-spinners";

function App() {
  const [city, setCity] = useState("Mumbai");

  const [question, setQuestion] = useState(
    "How sustainable is Mumbai today?"
  );

  const [data, setData] = useState(null);

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  const analyze = async () => {
    try {
      setLoading(true);
      setError("");

      const response = await API.post("/analyze", {
        city,
        question,
      });

      setData(response.data);

    } catch (error) {

      console.error(error);

      setError(
        "Failed to generate sustainability report. Please try again."
      );

    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      className="
      min-h-screen
      bg-gradient-to-br
      from-green-50
      via-blue-50
      to-slate-100
      "
    >
      <Header />

      <div className="max-w-screen-xl mx-auto px-6 pb-10">

        <SearchForm
          city={city}
          setCity={setCity}
          question={question}
          setQuestion={setQuestion}
          onSubmit={analyze}
          loading={loading}
        />

        {/* Error Message */}
        {error && (
          <div
            className="
            bg-red-100
            text-red-700
            p-4
            rounded-xl
            mt-6
            shadow
            "
          >
            {error}
          </div>
        )}

        {/* Loading Spinner */}
        {loading && (
          <div className="text-center py-12">

            <ClipLoader
              size={60}
              color="#16a34a"
            />

            <p className="mt-4 text-lg text-gray-700">
              Generating Sustainability Report...
            </p>

          </div>
        )}

        {/* Dashboard Content */}
        {!loading && data && (
          <>
            <div className="grid md:grid-cols-2 gap-6 mt-8">

              <ScoreCard impact={data.impact} />

              <WeatherCard weather={data.weather} />

            </div>

            <div className="mt-8">
              <NewsSection news={data.news} />
            </div>

            <div className="mt-8">
              <ReportSection report={data.report} />
            </div>
          </>
        )}

      </div>

      <Footer />
    </div>
  );
}

export default App;