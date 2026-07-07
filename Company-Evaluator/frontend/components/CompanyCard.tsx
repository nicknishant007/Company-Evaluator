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

        <div className="rounded-xl border border-[#3a331f] bg-[#161410] p-6 shadow-lg">

            <h2 className="text-2xl font-bold text-[#f4ecd8]">

                {company}

            </h2>

            <p className="mt-2 font-medium text-[#d4af37]">

                {ticker}

            </p>

            <p className="text-[#a89968]">

                {industry}

            </p>

        </div>

    );

}
