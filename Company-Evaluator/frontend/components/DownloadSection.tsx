interface Props {
  report: string;
  pdf: string;
  slides: string | null;
}

const BACKEND_URL = "http://127.0.0.1:8000";

export default function DownloadSection({
  report,
  pdf,
  slides,
}: Props) {
  return (
    <div className="flex flex-wrap gap-4">
      <a
        href={`${BACKEND_URL}${report}`}
        target="_blank"
        rel="noopener noreferrer"
        className="rounded-xl border border-[#7c5cff]/30 bg-card px-5 py-3 font-medium text-[#5b3fd6] shadow-sm transition hover:border-[#7c5cff] hover:bg-[#7c5cff]/10"
      >
        Report
      </a>

      <a
        href={`${BACKEND_URL}${pdf}`}
        target="_blank"
        rel="noopener noreferrer"
        className="rounded-xl border border-[#7c5cff]/30 bg-card px-5 py-3 font-medium text-[#5b3fd6] shadow-sm transition hover:border-[#7c5cff] hover:bg-[#7c5cff]/10"
      >
        PDF
      </a>

      {slides && (
        <a
          href={`${BACKEND_URL}${slides}`}
          target="_blank"
          rel="noopener noreferrer"
          className="rounded-xl bg-gradient-to-r from-[#7c5cff] via-[#a78bfa] to-[#ec4899] bg-[length:200%_auto] px-5 py-3 font-semibold text-white shadow-[0_10px_28px_-8px_rgba(124,92,255,0.7)] transition hover:bg-right"
        >
          Slides
        </a>
      )}
    </div>
  );
}
