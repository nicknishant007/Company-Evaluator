interface Props {

    report: string;

    pdf: string;

}

export default function DownloadCard({

    report,

    pdf,

}: Props) {

    return (

        <div className="rounded-xl border border-[#3a331f] bg-[#161410] p-6 shadow-lg">

            <h2 className="mb-5 text-xl font-bold text-[#f4ecd8]">

                Downloads

            </h2>

            <div className="flex gap-4">

                <a

                    href={`http://127.0.0.1:8000${report}`}

                    target="_blank"

                    className="rounded-lg bg-gradient-to-r from-[#8a6d1f] via-[#d4af37] to-[#8a6d1f] bg-[length:200%_auto] px-5 py-3 font-semibold text-[#161410] shadow-[0_4px_20px_-6px_rgba(212,175,55,0.6)] transition hover:bg-right"

                >

                    Report

                </a>

                <a

                    href={`http://127.0.0.1:8000${pdf}`}

                    target="_blank"

                    className="rounded-lg border border-[#d4af37]/40 bg-[#1c1810] px-5 py-3 font-medium text-[#f2cf6b] transition hover:border-[#d4af37] hover:bg-[#d4af37]/10"

                >

                    PDF

                </a>

            </div>

        </div>

    );

}
