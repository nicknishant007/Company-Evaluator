import {

Table,

TableBody,

TableCell,

TableHead,

TableHeader,

TableRow,

} from "@/components/ui/table";

interface Props{

metrics:any;

}

export default function FinancialTable({

metrics,

}:Props){

return(

<div className="rounded-2xl border border-border bg-card p-6 shadow-[0_10px_30px_-18px_rgba(124,92,255,0.35)]">

<h2 className="mb-5 text-2xl font-bold text-foreground">

Financial Metrics

</h2>

<Table>

<TableHeader>

<TableRow className="border-border hover:bg-transparent">

<TableHead className="text-muted-foreground">

Metric

</TableHead>

<TableHead className="text-right text-muted-foreground">

Value

</TableHead>

</TableRow>

</TableHeader>

<TableBody>

<TableRow className="border-border hover:bg-[#7c5cff]/5">

<TableCell className="text-foreground">

Revenue Growth

</TableCell>

<TableCell className="text-right font-semibold text-[#5b3fd6]">

{metrics.revenue_growth}%

</TableCell>

</TableRow>

<TableRow className="border-border hover:bg-[#7c5cff]/5">

<TableCell className="text-foreground">

Net Margin

</TableCell>

<TableCell className="text-right font-semibold text-[#5b3fd6]">

{metrics.net_margin}%

</TableCell>

</TableRow>

<TableRow className="border-border hover:bg-[#7c5cff]/5">

<TableCell className="text-foreground">

ROE

</TableCell>

<TableCell className="text-right font-semibold text-[#5b3fd6]">

{metrics.roe}%

</TableCell>

</TableRow>

<TableRow className="border-border hover:bg-[#7c5cff]/5">

<TableCell className="text-foreground">

ROA

</TableCell>

<TableCell className="text-right font-semibold text-[#5b3fd6]">

{metrics.roa}%

</TableCell>

</TableRow>

<TableRow className="border-border hover:bg-[#7c5cff]/5">

<TableCell className="text-foreground">

Debt / Equity

</TableCell>

<TableCell className="text-right font-semibold text-[#5b3fd6]">

{metrics.debt_equity}

</TableCell>

</TableRow>

<TableRow className="border-border hover:bg-[#7c5cff]/5">

<TableCell className="text-foreground">

Free Cash Flow

</TableCell>

<TableCell className="text-right font-semibold text-[#5b3fd6]">

₹ {metrics.free_cash_flow.toLocaleString()}

</TableCell>

</TableRow>

</TableBody>

</Table>

</div>

);

}
