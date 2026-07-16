interface Props {

    title: string;

    value: string;

}

export default function StatCard({

    title,

    value,

}: Props){

    return(

        <div className="rounded-2xl border border-border bg-card p-6 shadow-[0_10px_30px_-18px_rgba(124,92,255,0.35)]">

            <p className="text-sm font-medium text-muted-foreground">

                {title}

            </p>

            <h2 className="mt-2 text-3xl font-bold text-foreground">

                {value}

            </h2>

            <div className="mt-3 h-1 w-10 rounded-full bg-gradient-to-r from-[#7c5cff] to-[#ec4899]" />

        </div>

    )

}
