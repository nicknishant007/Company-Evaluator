import { ReactNode } from "react";

interface Props {

    title:string;

    children:ReactNode;

}

export default function SectionCard({

    title,

    children,

}:Props){

    return(

        <div className="rounded-xl border border-[#3a331f] bg-[#161410] p-6 shadow-lg">

            <h2 className="mb-5 text-xl font-bold text-[#f4ecd8]">

                {title}

            </h2>

            <div className="text-[#c9c0a3]">

                {children}

            </div>

        </div>

    )

}
