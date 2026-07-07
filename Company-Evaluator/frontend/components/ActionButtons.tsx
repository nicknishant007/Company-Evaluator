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

        <div className="mt-8 flex flex-wrap gap-5">

            <a

                href={`http://127.0.0.1:8000${report}`}

                target="_blank"

                className="rounded-lg bg-gradient-to-r from-[#8a6d1f] via-[#d4af37] to-[#8a6d1f] bg-[length:200%_auto] px-6 py-3 font-semibold text-[#161410] shadow-[0_4px_20px_-6px_rgba(212,175,55,0.6)] transition hover:bg-right"

            >

                Download Report

            </a>

            <a

                href={`http://127.0.0.1:8000${pdf}`}

                target="_blank"

                className="rounded-lg border border-[#d4af37]/40 bg-[#1c1810] px-6 py-3 font-medium text-[#f2cf6b] transition hover:border-[#d4af37] hover:bg-[#d4af37]/10"

            >

                Download PDF

            </a>

            {

                slides && (

                    <a

                        href={`http://127.0.0.1:8000${slides}`}

                        target="_blank"

                        className="rounded-lg border border-[#3a331f] bg-[#1c1810] px-6 py-3 font-medium text-[#d9d2bd] transition hover:border-[#d4af37]/60 hover:text-[#f2cf6b]"

                    >

                        Download Slides

                    </a>

                )

            }

        </div>

    )

}
