import {
  LayoutDashboard,
  FileBarChart,
  CalendarClock,
  BarChart3,
  MessageSquare,
  Settings,
} from "lucide-react";

const NAV_ITEMS = [
  { label: "Home", icon: LayoutDashboard, active: true },
  { label: "Reports", icon: FileBarChart, active: false },
  { label: "Planning", icon: CalendarClock, active: false },
  { label: "Statistics", icon: BarChart3, active: false },
  { label: "Messages", icon: MessageSquare, active: false },
  { label: "Settings", icon: Settings, active: false },
];

export default function Sidebar() {
  return (
    <aside className="sticky top-0 hidden h-screen w-64 shrink-0 flex-col justify-between bg-sidebar px-4 py-6 text-sidebar-foreground lg:flex">
      <div>
        <div className="mb-8 flex items-center gap-3 px-2">
          <span className="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br from-[#a78bfa] to-[#7c5cff] text-sm font-bold text-white shadow-[0_4px_16px_-4px_rgba(124,92,255,0.7)]">
            CE
          </span>
          <span className="text-base font-semibold tracking-tight text-white">
            Company Evaluator
          </span>
        </div>

        <nav className="space-y-1">
          {NAV_ITEMS.map(({ label, icon: Icon, active }) => (
            <a
              key={label}
              href="#"
              className={`flex items-center gap-3 rounded-xl px-3 py-2.5 text-sm font-medium transition-colors ${
                active
                  ? "bg-sidebar-primary text-white shadow-[0_4px_16px_-6px_rgba(124,92,255,0.8)]"
                  : "text-sidebar-foreground/70 hover:bg-sidebar-accent hover:text-sidebar-accent-foreground"
              }`}
            >
              <Icon className="size-4" />
              {label}
            </a>
          ))}
        </nav>
      </div>

      <div className="rounded-2xl bg-gradient-to-br from-[#a78bfa] via-[#7c5cff] to-[#ec4899] p-5 text-white shadow-[0_8px_28px_-10px_rgba(124,92,255,0.8)]">
        <p className="text-sm font-semibold leading-snug">
          AI Equity Research, in one click
        </p>
        <p className="mt-1 text-xs text-white/80">
          Type a ticker to generate a full report
        </p>
      </div>
    </aside>
  );
}


