interface Props{

    report:string;

    pdf:string;

    slides?:string;

}

export default function ActionButtons({

    report,

    pdf,

    slides,

}:Props){

    return(

        <div className="mt-8 flex gap-5">

            <a

                href={`http://127.0.0.1:8000${report}`}

                target="_blank"

                className="rounded-lg bg-black px-6 py-3 text-white"

            >

                Download Report

            </a>

            <a

                href={`http://127.0.0.1:8000${pdf}`}

                target="_blank"

                className="rounded-lg bg-blue-600 px-6 py-3 text-white"

            >

                Download PDF

            </a>

            {

                slides && (

                    <a

                        href={`http://127.0.0.1:8000${slides}`}

                        target="_blank"

                        className="rounded-lg bg-green-600 px-6 py-3 text-white"

                    >

                        Download Slides

                    </a>

                )

            }

        </div>

    )

}