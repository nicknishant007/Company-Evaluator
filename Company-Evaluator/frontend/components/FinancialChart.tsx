import {

    ResponsiveContainer,

    BarChart,

    Bar,

    CartesianGrid,

    XAxis,

    YAxis,

    Tooltip,

} from "recharts";

interface Props {

    metrics: any;

}

export default function FinancialChart({

    metrics,

}: Props) {

    const data = [

        {

            name: "Revenue",

            value: metrics.revenue_growth,

        },

        {

            name: "Margin",

            value: metrics.net_margin,

        },

        {

            name: "ROE",

            value: metrics.roe,

        },

        {

            name: "ROA",

            value: metrics.roa,

        },

    ];

    return (

        <div className="rounded-xl border bg-white p-6 shadow">

            <h2 className="mb-4 text-xl font-bold">

                Financial Performance

            </h2>

            <div className="h-80">

                <ResponsiveContainer width="100%" height="100%">

                    <BarChart data={data}>

                        <CartesianGrid strokeDasharray="3 3"/>

                        <XAxis 
                        dataKey="name"
                        tick={{fontSize:12}}
                        />

                        <YAxis tick={{fontSize:12}}
                        />

                        <Tooltip/>

                        <Bar
                         dataKey="value"
                         radius={[8,8,0,0]}
                        />

                    </BarChart>

                </ResponsiveContainer>

            </div>

        </div>

    );

}