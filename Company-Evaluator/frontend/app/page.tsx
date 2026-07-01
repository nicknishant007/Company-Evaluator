import Navbar from "@/components/Navbar";
import SearchForm from "@/components/SearchForm";

export default function HomePage() {

    return (

        <main className="min-h-screen bg-slate-100">

            <Navbar />

            <div className="mx-auto max-w-3xl p-10">

                <div className="rounded-xl bg-white p-10 shadow">

                    <h1 className="mb-3 text-4xl font-bold">

                        Company Evaluator

                    </h1>

                    <p className="text-gray-600">

                        AI Powered Equity Research Platform

                    </p>

                    <SearchForm />

                </div>

            </div>

        </main>

    );

}