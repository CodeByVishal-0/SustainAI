function NewsSection({ news }) {
  if (!news || news.length === 0) return null;

  return (
    <div className="bg-white rounded-xl shadow p-6">

      <h2 className="text-xl font-bold mb-6">
        📰 Environmental News
      </h2>

      <div className="space-y-4">

        {news.map((article, index) => (

          <div
            key={index}
            className="
            bg-gray-50
            p-4
            rounded-lg
            hover:bg-green-50
            transition
            "
          >

            <h3 className="font-semibold text-lg">
              {article.title}
            </h3>

            <p className="text-gray-600 mt-2">
              {article.description}
            </p>

          </div>

        ))}

      </div>

    </div>
  );
}

export default NewsSection;