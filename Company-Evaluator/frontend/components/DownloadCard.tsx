interface Props {

    report: string;

    pdf: string;

}

export default function DownloadCard({

    report,

    pdf,

}: Props) {

    return (

        <div className="rounded-xl border bg-white p-6 shadow">

            <h2 className="mb-5 text-xl font-bold">

                Downloads

            </h2>

            <div className="flex gap-4">

                <a

                    href={`http://127.0.0.1:8000${report}`}

                    target="_blank"

                    className="rounded-lg bg-black px-5 py-3 text-white"

                >

                    Report

                </a>

                <a

                    href={`http://127.0.0.1:8000${pdf}`}

                    target="_blank"

                    className="rounded-lg bg-blue-600 px-5 py-3 text-white"

                >

                    PDF

                </a>

            </div>

        </div>

    );

}