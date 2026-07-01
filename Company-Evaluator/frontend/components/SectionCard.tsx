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

        <div className="rounded-xl border bg-white p-6 shadow">

            <h2 className="mb-5 text-xl font-bold">

                {title}

            </h2>

            {children}

        </div>

    )

}