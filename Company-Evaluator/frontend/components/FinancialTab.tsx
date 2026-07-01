import SectionCard from "./SectionCard";

interface Props{

    report:string;

}

export default function FinancialTab({

    report,

}:Props){

    return(

        <SectionCard title="Financial Analysis">

            <pre className="whitespace-pre-wrap">

                {report}

            </pre>

        </SectionCard>

    )

}