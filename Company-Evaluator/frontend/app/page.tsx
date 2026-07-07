import Navbar from "@/components/Navbar";
import SearchForm from "@/components/SearchForm";

export default function HomePage() {

    return (

        <main className="min-h-screen bg-[#0e0d0b]">

            <Navbar />

            <div className="mx-auto max-w-3xl px-6 py-16">

                <div className="relative overflow-hidden rounded-2xl border border-[#3a331f] bg-gradient-to-b from-[#161410] to-[#0e0d0b] p-10 shadow-[0_0_60px_-15px_rgba(212,175,55,0.25)]">

                    <div className="pointer-events-none absolute -top-24 -right-24 h-64 w-64 rounded-full bg-[#d4af37]/10 blur-3xl" />

                    <p className="mb-3 text-xs font-medium tracking-[0.25em] text-[#a89968] uppercase">
                        Equity Research, Automated
                    </p>

                    <h1 className="mb-3 text-4xl font-bold tracking-tight text-[#f4ecd8]">
                        Company{" "}
                        <span className="gold-text">Evaluator</span>
                    </h1>

                    <p className="text-[#a89968]">
                        AI Powered Equity Research Platform
                    </p>

                    <div className="gold-divider my-8" />

                    <SearchForm />

                </div>

            </div>

        </main>

    );

}
