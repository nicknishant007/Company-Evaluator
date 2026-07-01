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

        <div className="rounded-xl bg-white p-8 shadow">

            <h1 className="text-3xl font-bold">

                {company}

            </h1>

            <p className="mt-2 text-gray-500">

                {industry}

            </p>

            <div className="mt-6">

                <span className="rounded-full bg-green-100 px-4 py-2">

                    {recommendation}

                </span>

            </div>

        </div>

    )

}