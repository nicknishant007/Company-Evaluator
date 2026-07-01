import ReactMarkdown from "react-markdown";

interface Props {

    report: string;

}

export default function ReportViewer({

    report,

}: Props) {

    return (

        <div className="rounded-xl border bg-white p-6 shadow">

            <h2 className="mb-5 text-2xl font-bold">

                Research Report

            </h2>

            <div className="prose max-w-none">

                <ReactMarkdown>

                    {report}

                </ReactMarkdown>

            </div>

        </div>

    );

}