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

const VIOLET_SHADES = ["#7c5cff", "#a78bfa", "#ec4899", "#5b3fd6"];

function ChartTooltip({ active, payload, label }: any) {

    if (!active || !payload || !payload.length) return null;

    return (

        <div className="rounded-lg border border-[#7c5cff]/30 bg-card px-4 py-2 shadow-[0_10px_30px_-8px_rgba(124,92,255,0.4)]">

            <p className="text-xs tracking-wide text-muted-foreground uppercase">

                {label}

            </p>

            <p className="text-lg font-semibold text-[#5b3fd6]">

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

        <div className="rounded-2xl border border-border bg-card p-6 shadow-[0_10px_30px_-18px_rgba(124,92,255,0.35)]">

            <h2 className="mb-4 text-xl font-bold text-foreground">

                Financial Performance

            </h2>

            <div className="h-80">

                <ResponsiveContainer width="100%" height="100%">

                    <BarChart data={data} margin={{ top: 24, right: 8, left: 0, bottom: 0 }}>

                        <defs>

                            {VIOLET_SHADES.map((color, i) => (

                                <linearGradient

                                    key={color}

                                    id={`violetBar-${i}`}

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

                            stroke="var(--border)"

                            vertical={false}

                        />

                        <XAxis

                            dataKey="name"

                            tick={{ fontSize: 12, fill: "var(--muted-foreground)" }}

                            axisLine={{ stroke: "var(--border)" }}

                            tickLine={false}

                        />

                        <YAxis

                            tick={{ fontSize: 12, fill: "var(--muted-foreground)" }}

                            axisLine={{ stroke: "var(--border)" }}

                            tickLine={false}

                        />

                        <Tooltip

                            cursor={{ fill: "rgba(124,92,255,0.08)" }}

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

                                    fill={`url(#violetBar-${index % VIOLET_SHADES.length})`}

                                    stroke={VIOLET_SHADES[index % VIOLET_SHADES.length]}

                                    strokeWidth={1}

                                />

                            ))}

                            <LabelList

                                dataKey="value"

                                position="top"

                                formatter={((v: any) => `${v}%`) as any}

                                fill="var(--foreground)"

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
