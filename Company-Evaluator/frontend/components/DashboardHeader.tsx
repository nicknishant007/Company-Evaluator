interface Props {

    company: string;

    ticker: string;

    industry: string;

    recommendation: string;

}

export default function DashboardHeader({

    company,

    ticker,

    industry,

    recommendation,

}: Props) {

    return (

        <div className="relative overflow-hidden rounded-xl border border-[#3a331f] bg-gradient-to-b from-[#161410] to-[#111009] p-6 shadow-lg">

            <div className="pointer-events-none absolute -top-16 -right-16 h-48 w-48 rounded-full bg-[#d4af37]/10 blur-3xl" />

            <div className="flex flex-col justify-between gap-4 sm:flex-row sm:items-start">

                <div>

                    <h1 className="text-3xl font-bold tracking-tight text-[#f4ecd8]">

                        {company}

                    </h1>

                    <p className="mt-2 font-medium text-[#d4af37]">

                        {ticker}

                    </p>

                    <p className="text-[#a89968]">

                        {industry}

                    </p>

                </div>

                <div>

                    <span className="inline-flex rounded-full border border-[#d4af37]/40 bg-[#d4af37]/10 px-4 py-2 font-semibold text-[#f2cf6b]">

                        {recommendation}

                    </span>

                </div>

            </div>

        </div>

    );

}
