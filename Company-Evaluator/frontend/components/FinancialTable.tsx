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

<div className="rounded-xl border border-[#3a331f] bg-[#161410] p-6 shadow-lg">

<h2 className="mb-5 text-2xl font-bold text-[#f4ecd8]">

Financial Metrics

</h2>

<Table>

<TableHeader>

<TableRow className="border-[#3a331f] hover:bg-transparent">

<TableHead className="text-[#a89968]">

Metric

</TableHead>

<TableHead className="text-right text-[#a89968]">

Value

</TableHead>

</TableRow>

</TableHeader>

<TableBody>

<TableRow className="border-[#2a2519] hover:bg-[#d4af37]/5">

<TableCell className="text-[#d9d2bd]">

Revenue Growth

</TableCell>

<TableCell className="text-right font-semibold text-[#f2cf6b]">

{metrics.revenue_growth}%

</TableCell>

</TableRow>

<TableRow className="border-[#2a2519] hover:bg-[#d4af37]/5">

<TableCell className="text-[#d9d2bd]">

Net Margin

</TableCell>

<TableCell className="text-right font-semibold text-[#f2cf6b]">

{metrics.net_margin}%

</TableCell>

</TableRow>

<TableRow className="border-[#2a2519] hover:bg-[#d4af37]/5">

<TableCell className="text-[#d9d2bd]">

ROE

</TableCell>

<TableCell className="text-right font-semibold text-[#f2cf6b]">

{metrics.roe}%

</TableCell>

</TableRow>

<TableRow className="border-[#2a2519] hover:bg-[#d4af37]/5">

<TableCell className="text-[#d9d2bd]">

ROA

</TableCell>

<TableCell className="text-right font-semibold text-[#f2cf6b]">

{metrics.roa}%

</TableCell>

</TableRow>

<TableRow className="border-[#2a2519] hover:bg-[#d4af37]/5">

<TableCell className="text-[#d9d2bd]">

Debt / Equity

</TableCell>

<TableCell className="text-right font-semibold text-[#f2cf6b]">

{metrics.debt_equity}

</TableCell>

</TableRow>

<TableRow className="border-[#2a2519] hover:bg-[#d4af37]/5">

<TableCell className="text-[#d9d2bd]">

Free Cash Flow

</TableCell>

<TableCell className="text-right font-semibold text-[#f2cf6b]">

₹ {metrics.free_cash_flow.toLocaleString()}

</TableCell>

</TableRow>

</TableBody>

</Table>

</div>

);

}
