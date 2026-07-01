interface Props {

    title: string;

    value: string;

}

export default function MetricCard({

    title,

    value,

}: Props) {

    return (

        <div className="rounded-xl bg-slate-50 p-5 shadow">

            <p className="text-sm text-gray-500">

                {title}

            </p>

            <h2 className="mt-2 text-2xl font-bold">

                {value}

            </h2>

        </div>

    );

}