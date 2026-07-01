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

        <div className="rounded-xl border bg-white p-6 shadow">

            <div className="flex justify-between items-start">

                <div>

                    <h1 className="text-3xl font-bold">

                        {company}

                    </h1>

                    <p className="mt-2 text-gray-600">

                        {ticker}

                    </p>

                    <p className="text-gray-500">

                        {industry}

                    </p>

                </div>

                <div>

                    <span className="rounded-full bg-green-100 px-4 py-2 font-semibold text-green-700">

                        {recommendation}

                    </span>

                </div>

            </div>

        </div>

    );

}