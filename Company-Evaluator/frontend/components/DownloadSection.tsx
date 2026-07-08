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
        className="rounded-lg border border-[#d4af37]/40 bg-[#1c1810] px-5 py-3 font-medium text-[#f2cf6b] transition hover:border-[#d4af37] hover:bg-[#d4af37]/10"
      >
        Report
      </a>

      <a
        href={`${BACKEND_URL}${pdf}`}
        target="_blank"
        rel="noopener noreferrer"
        className="rounded-lg border border-[#d4af37]/40 bg-[#1c1810] px-5 py-3 font-medium text-[#f2cf6b] transition hover:border-[#d4af37] hover:bg-[#d4af37]/10"
      >
        PDF
      </a>

      {slides && (
        <a
          href={`${BACKEND_URL}${slides}`}
          target="_blank"
          rel="noopener noreferrer"
          className="rounded-lg bg-gradient-to-r from-[#8a6d1f] via-[#d4af37] to-[#8a6d1f] bg-[length:200%_auto] px-5 py-3 font-semibold text-[#161410] shadow-[0_4px_20px_-6px_rgba(212,175,55,0.6)] transition hover:bg-right"
        >
          Slides
        </a>
      )}
    </div>
  );
}