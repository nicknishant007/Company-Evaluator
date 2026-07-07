import ReactMarkdown from "react-markdown";

interface Props {

    report: string;

}

export default function ReportViewer({

    report,

}: Props) {

    return (

        <div className="rounded-xl border border-[#3a331f] bg-[#161410] p-6 shadow-lg">

            <h2 className="mb-5 text-2xl font-bold text-[#f4ecd8]">

                Research Report

            </h2>

            <div className="prose prose-invert max-w-none prose-headings:text-[#f2cf6b] prose-strong:text-[#f4ecd8] prose-a:text-[#d4af37] prose-p:text-[#c9c0a3] prose-li:text-[#c9c0a3] prose-hr:border-[#3a331f]">

                <ReactMarkdown>

                    {report}

                </ReactMarkdown>

            </div>

        </div>

    );

}
