interface Props {

    title: string;

    value: string;

}

export default function MetricCard({

    title,

    value,

}: Props) {

    return (

        <div className="rounded-xl border border-[#3a331f] bg-[#1c1810] p-5 shadow">

            <p className="text-sm text-[#a89968]">

                {title}

            </p>

            <h2 className="mt-2 text-2xl font-bold text-[#f2cf6b]">

                {value}

            </h2>

        </div>

    );

}
