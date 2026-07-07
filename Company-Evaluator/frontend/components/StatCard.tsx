interface Props {

    title: string;

    value: string;

}

export default function StatCard({

    title,

    value,

}: Props){

    return(

        <div className="rounded-xl border border-[#3a331f] bg-[#161410] p-6 shadow-lg">

            <p className="text-[#a89968]">

                {title}

            </p>

            <h2 className="mt-2 text-3xl font-bold text-[#f2cf6b]">

                {value}

            </h2>

        </div>

    )

}
