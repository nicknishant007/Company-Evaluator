import { Bell, Mail } from "lucide-react";

export default function Navbar() {
  return (
    <nav className="sticky top-0 z-20 border-b border-border/70 bg-background/80 backdrop-blur supports-[backdrop-filter]:bg-background/70">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-6">
        <div className="flex items-center gap-3">
          <span className="flex h-8 w-8 items-center justify-center rounded-lg bg-gradient-to-br from-[#a78bfa] to-[#7c5cff] text-sm font-bold text-white shadow-[0_4px_14px_-4px_rgba(124,92,255,0.7)]">
            CE
          </span>
          <h1 className="text-lg font-semibold tracking-tight text-foreground">
            Company Evaluator
          </h1>
        </div>

        <div className="flex items-center gap-4">
          <p className="hidden text-sm tracking-wide text-muted-foreground sm:block">
            AI Equity Research Platform
          </p>

          <div className="flex items-center gap-2">
            <button className="flex h-9 w-9 items-center justify-center rounded-full border border-border bg-card text-muted-foreground shadow-sm transition hover:text-primary">
              <Mail className="size-4" />
            </button>
            <button className="flex h-9 w-9 items-center justify-center rounded-full border border-border bg-card text-muted-foreground shadow-sm transition hover:text-primary">
              <Bell className="size-4" />
            </button>
            <span className="flex h-9 w-9 items-center justify-center rounded-full bg-gradient-to-br from-[#a78bfa] to-[#ec4899] text-xs font-semibold text-white shadow-sm">
              CE
            </span>
          </div>
        </div>
      </div>

      <div className="h-px w-full bg-gradient-to-r from-transparent via-[#7c5cff]/40 to-transparent" />
    </nav>
  );
}
