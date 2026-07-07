export default function Navbar() {
  return (
    <nav className="sticky top-0 z-20 border-b border-[#3a331f] bg-[#0e0d0b]/90 backdrop-blur supports-[backdrop-filter]:bg-[#0e0d0b]/80">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-6">
        <div className="flex items-center gap-3">
          <span className="flex h-8 w-8 items-center justify-center rounded-md border border-[#d4af37]/50 bg-gradient-to-br from-[#3a331f] to-[#0e0d0b] text-sm font-bold text-[#f2cf6b]">
            CE
          </span>
          <h1 className="text-lg font-semibold tracking-tight text-[#f4ecd8]">
            Company Evaluator
          </h1>
        </div>

        <p className="hidden text-sm tracking-wide text-[#a89968] sm:block">
          AI Equity Research Platform
        </p>
      </div>

      <div className="h-px w-full bg-gradient-to-r from-transparent via-[#d4af37]/70 to-transparent" />
    </nav>
  );
}
