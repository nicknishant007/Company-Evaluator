import SectionCard from "./SectionCard";

interface Props{

    report:string;

}

export default function FinancialTab({

    report,

}:Props){

    return(

        <SectionCard title="Financial Analysis">

            <pre className="whitespace-pre-wrap text-[#c9c0a3]">

                {report}

            </pre>

        </SectionCard>

    )

}
