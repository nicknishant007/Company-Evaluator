interface Props{

    company:string;

    industry:string;

    recommendation?:string;

}

export default function SummaryCard({

    company,

    industry,

    recommendation="Data Not Available",

}:Props){

    return(

        <div className="rounded-xl border border-[#3a331f] bg-[#161410] p-8 shadow-lg">

            <h1 className="text-3xl font-bold text-[#f4ecd8]">

                {company}

            </h1>

            <p className="mt-2 text-[#a89968]">

                {industry}

            </p>

            <div className="mt-6">

                <span className="rounded-full border border-[#d4af37]/40 bg-[#d4af37]/10 px-4 py-2 text-[#f2cf6b]">

                    {recommendation}

                </span>

            </div>

        </div>

    )

}
