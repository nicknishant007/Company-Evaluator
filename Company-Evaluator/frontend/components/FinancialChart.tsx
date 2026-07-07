import {

    ResponsiveContainer,

    BarChart,

    Bar,

    Cell,

    LabelList,

    CartesianGrid,

    XAxis,

    YAxis,

    Tooltip,

} from "recharts";

interface Props {

    metrics: any;

}

const GOLD_SHADES = ["#f2cf6b", "#d4af37", "#b8922c", "#8a6d1f"];

function ChartTooltip({ active, payload, label }: any) {

    if (!active || !payload || !payload.length) return null;

    return (

        <div className="rounded-lg border border-[#d4af37]/50 bg-[#161410] px-4 py-2 shadow-[0_4px_20px_-4px_rgba(212,175,55,0.4)]">

            <p className="text-xs tracking-wide text-[#a89968] uppercase">

                {label}

            </p>

            <p className="text-lg font-semibold text-[#f2cf6b]">

                {payload[0].value}%

            </p>

        </div>

    );

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

        <div className="rounded-xl border border-[#3a331f] bg-[#161410] p-6 shadow-lg">

            <h2 className="mb-4 text-xl font-bold text-[#f4ecd8]">

                Financial Performance

            </h2>

            <div className="h-80">

                <ResponsiveContainer width="100%" height="100%">

                    <BarChart data={data} margin={{ top: 24, right: 8, left: 0, bottom: 0 }}>

                        <defs>

                            {GOLD_SHADES.map((color, i) => (

                                <linearGradient

                                    key={color}

                                    id={`goldBar-${i}`}

                                    x1="0"

                                    y1="0"

                                    x2="0"

                                    y2="1"

                                >

                                    <stop offset="0%" stopColor={color} stopOpacity={1} />

                                    <stop offset="100%" stopColor={color} stopOpacity={0.45} />

                                </linearGradient>

                            ))}

                        </defs>

                        <CartesianGrid

                            strokeDasharray="3 3"

                            stroke="#3a331f"

                            vertical={false}

                        />

                        <XAxis

                            dataKey="name"

                            tick={{ fontSize: 12, fill: "#a89968" }}

                            axisLine={{ stroke: "#3a331f" }}

                            tickLine={false}

                        />

                        <YAxis

                            tick={{ fontSize: 12, fill: "#a89968" }}

                            axisLine={{ stroke: "#3a331f" }}

                            tickLine={false}

                        />

                        <Tooltip

                            cursor={{ fill: "rgba(212,175,55,0.08)" }}

                            content={<ChartTooltip />}

                        />

                        <Bar

                         dataKey="value"

                         radius={[8,8,0,0]}

                         maxBarSize={64}

                        >

                            {data.map((entry, index) => (

                                <Cell

                                    key={entry.name}

                                    fill={`url(#goldBar-${index % GOLD_SHADES.length})`}

                                    stroke={GOLD_SHADES[index % GOLD_SHADES.length]}

                                    strokeWidth={1}

                                />

                            ))}

                            <LabelList

                                dataKey="value"

                                position="top"

                                formatter={((v: any) => `${v}%`) as any}

                                fill="#f4ecd8"

                                fontSize={12}

                                fontWeight={600}

                            />

                        </Bar>

                    </BarChart>

                </ResponsiveContainer>

            </div>

        </div>

    );

}
