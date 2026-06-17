import ReactMarkdown from "react-markdown";

function ReportSection({ report }) {
  if (!report) return null;

  return (
    <div className="bg-white rounded-xl shadow p-6">

      <h2 className="text-2xl font-bold mb-6">
        📄 AI Sustainability Report
      </h2>

      <div className="prose max-w-none">
        <ReactMarkdown>
          {report}
        </ReactMarkdown>
      </div>

    </div>
  );
}

export default ReportSection;