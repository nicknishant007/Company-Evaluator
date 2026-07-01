interface Props {

    company: string;

    ticker: string;

    industry: string;

}

export default function CompanyCard({

    company,

    ticker,

    industry,

}: Props) {

    return (

        <div className="rounded-xl border bg-white p-6 shadow">

            <h2 className="text-2xl font-bold">

                {company}

            </h2>

            <p className="mt-2 text-gray-600">

                {ticker}

            </p>

            <p className="text-gray-600">

                {industry}

            </p>

        </div>

    );

}