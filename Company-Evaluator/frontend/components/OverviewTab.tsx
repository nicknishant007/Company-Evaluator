import SectionCard from "./SectionCard";

interface Props{

    company:string;

    industry:string;

}

export default function OverviewTab({

    company,

    industry,

}:Props){

    return(

        <SectionCard title="Company Overview">

            <p>

                <strong>Company:</strong> {company}

            </p>

            <p className="mt-3">

                <strong>Industry:</strong> {industry}

            </p>

        </SectionCard>

    )

}