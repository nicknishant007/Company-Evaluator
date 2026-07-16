interface Props {

    company: string;

    ticker: string;

    industry: string | null;

    recommendation: string | null;

}

export default function DashboardHeader({

    company,

    ticker,

    industry,

    recommendation,

}: Props) {

    return (

        <div className="relative overflow-hidden rounded-2xl border border-border bg-card p-6 shadow-[0_10px_30px_-18px_rgba(124,92,255,0.35)]">

            <div className="pointer-events-none absolute -top-16 -right-16 h-48 w-48 rounded-full bg-[#7c5cff]/10 blur-3xl" />

            <div className="flex flex-col justify-between gap-4 sm:flex-row sm:items-start">

                <div>

                    <h1 className="text-3xl font-bold tracking-tight text-foreground">

                        {company}

                    </h1>

                    <p className="mt-2 font-medium text-[#7c5cff]">

                        {ticker}

                    </p>

                    <p className="text-muted-foreground">

                        {industry}

                    </p>

                </div>

                <div>

                    <span className="inline-flex rounded-full border border-[#7c5cff]/30 bg-[#7c5cff]/10 px-4 py-2 font-semibold text-[#5b3fd6]">

                        {recommendation}

                    </span>

                </div>

            </div>

        </div>

    );

}
