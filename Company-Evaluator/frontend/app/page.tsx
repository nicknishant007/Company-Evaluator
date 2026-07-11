import Navbar from "@/components/Navbar";
import SearchForm from "@/components/SearchForm";

const AVATARS = ["#404040", "#666666", "#999999"];

export default function HomePage() {
  return (
    <main className="min-h-screen bg-black">
      <Navbar />

      <div className="mx-auto max-w-4xl px-6 py-16">
        <div className="relative overflow-hidden rounded-2xl border border-[#262626] bg-gradient-to-b from-[#111111] to-black p-10 shadow-[0_0_60px_-15px_rgba(255,255,255,0.08)]">
          <div className="pointer-events-none absolute -top-24 -right-24 h-64 w-64 rounded-full bg-white/5 blur-3xl" />

          <span className="mb-6 inline-flex items-center rounded-full border border-[#262626] bg-[#161616] px-4 py-1.5 text-xs font-medium text-gray-400">
            AI-Native Equity Research
          </span>

          <h1 className="mb-4 max-w-2xl text-4xl leading-[1.1] font-bold tracking-tight text-white sm:text-5xl">
            Evaluate any company <span className="gold-text">instantly</span>
          </h1>

          <p className="max-w-xl text-gray-400">
            Helping investors get institution-grade financial research
            without the overhead of an in-house analyst team.
          </p>

          <div className="mt-8 flex flex-wrap gap-3">
            <a
              href="#analyze"
              className="inline-flex items-center gap-2 rounded-lg bg-white px-6 py-3 font-semibold text-black transition hover:bg-gray-200"
            >
              Start Analysis
            </a>
            <a
              href="#analyze"
              className="inline-flex items-center gap-2 rounded-lg border border-[#262626] bg-[#161616] px-6 py-3 font-medium text-gray-300 transition hover:border-gray-500 hover:text-white"
            >
              View Sample Report
            </a>
          </div>

          <div className="mt-10 flex items-center gap-3">
            <div className="flex -space-x-2">
              {AVATARS.map((color, i) => (
                <span
                  key={i}
                  className="h-8 w-8 rounded-full border-2 border-black"
                  style={{ backgroundColor: color }}
                />
              ))}
            </div>
            <p className="text-sm text-gray-400">
              500+ reports generated.{" "}
              <a href="#analyze" className="text-white hover:underline">
                See a sample
              </a>
            </p>
          </div>

          <span className="absolute right-6 bottom-6 hidden items-center gap-1.5 rounded-full border border-[#262626] bg-[#111111]/90 px-3 py-1.5 text-xs font-medium text-gray-400 sm:inline-flex">
            Powered by AI
          </span>

          <div className="gold-divider my-8" />

          <div id="analyze">
            <SearchForm />
          </div>
        </div>
      </div>
    </main>
  );
}