import Navbar from "@/components/Navbar";
import SearchForm from "@/components/SearchForm";

export default function HomePage() {

    return (

        <main className="min-h-screen bg-background">

            <Navbar />

            <div className="mx-auto max-w-4xl px-6 py-16">

                <div className="relative overflow-hidden rounded-2xl border border-border bg-card p-10 shadow-[0_20px_60px_-25px_rgba(124,92,255,0.35)]">

                    <div className="pointer-events-none absolute -top-24 -right-24 h-64 w-64 rounded-full bg-[#7c5cff]/10 blur-3xl" />
                    <div className="pointer-events-none absolute -bottom-24 -left-24 h-64 w-64 rounded-full bg-[#ec4899]/10 blur-3xl" />

                    <p className="mb-3 text-xs font-medium tracking-[0.25em] text-muted-foreground uppercase">
                        Equity Research, Automated
                    </p>

                    <h1 className="mb-3 text-4xl font-bold tracking-tight text-foreground">
                        Company{" "}
                        <span className="gold-text">Evaluator</span>
                    </h1>

                    <p className="text-muted-foreground">
                        AI Powered Equity Research Platform
                    </p>

                    <div className="gold-divider my-8" />

                    <SearchForm />

                </div>

            </div>

        </main>

    );

}
