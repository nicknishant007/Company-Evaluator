export default function Navbar() {
  return (
    <nav className="sticky top-0 z-20 border-b border-[#262626] bg-black/90 backdrop-blur supports-[backdrop-filter]:bg-black/80">
      <div className="mx-auto flex h-20 max-w-7xl items-center justify-between px-6">
        <div className="flex items-center gap-3">
          <span className="flex h-10 w-10 items-center justify-center rounded-full border border-[#404040] bg-gradient-to-br from-[#262626] to-black text-sm font-bold text-white">
            CE
          </span>
          <div>
            <h1 className="text-base leading-tight font-semibold tracking-tight text-white">
              Company Evaluator
            </h1>
            <span className="inline-flex items-center rounded-full bg-white/10 px-2 py-0.5 text-[10px] font-medium tracking-wide text-gray-300 uppercase">
              AI Research Partner
            </span>
          </div>
        </div>

        <div className="hidden items-center gap-1 rounded-full border border-[#262626] bg-[#111111] p-1.5 md:flex">
          {["Analyze", "Metrics", "Reports", "Pricing"].map((item) => (
            <a
              key={item}
              href="#"
              className="rounded-full px-4 py-2 text-sm font-medium text-gray-400 transition hover:bg-white/10 hover:text-white"
            >
              {item}
            </a>
          ))}
        </div>

        <a
          href="#analyze"
          className="inline-flex items-center gap-2 rounded-full bg-white px-5 py-2.5 text-sm font-semibold text-black transition hover:bg-gray-200"
        >
          <span className="h-2 w-2 rounded-full bg-green-500" />
          Get Started
        </a>
      </div>
    </nav>
  );
}