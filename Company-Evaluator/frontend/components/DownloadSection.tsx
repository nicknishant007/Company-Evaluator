interface Props {

    report: string;

    pdf: string;

    slides: string;

}

export default function DownloadSection({

    report,

    pdf,

    slides,

}: Props) {

    return (

        <div className="flex gap-5">

            <a

                href={report}

                className="rounded-lg bg-blue-600 px-5 py-3 text-white"

            >

                Report

            </a>

            <a

                href={pdf}

                className="rounded-lg bg-red-600 px-5 py-3 text-white"

            >

                PDF

            </a>

            <a

                href={slides}

                className="rounded-lg bg-green-600 px-5 py-3 text-white"

            >

                Slides

            </a>

        </div>

    );

}