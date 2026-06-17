function SearchForm({
  city,
  setCity,
  question,
  setQuestion,
  onSubmit,
  loading
}) {
  return (
    <div className="bg-white rounded-xl shadow p-6">

      <input
        type="text"
        placeholder="Enter City"
        value={city}
        onChange={(e) => setCity(e.target.value)}
        className="
        w-full
        border
        rounded-lg
        p-3
        mb-4
        focus:ring-2
        focus:ring-green-500
        "
      />

      <textarea
        placeholder="Ask sustainability question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        rows="4"
        className="
        w-full
        border
        rounded-lg
        p-3
        focus:ring-2
        focus:ring-green-500
        "
      />

      <button
        onClick={onSubmit}
        disabled={loading}
        className="
        bg-green-600
        hover:bg-green-700
        text-white
        px-6
        py-3
        rounded-lg
        mt-4
        transition
        "
      >
        {loading
          ? "Analyzing Sustainability..."
          : "Generate Report"}
      </button>

    </div>
  );
}

export default SearchForm;