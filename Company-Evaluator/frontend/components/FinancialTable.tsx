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

<div className="rounded-xl border bg-white p-6 shadow">

<h2 className="mb-5 text-2xl font-bold">

Financial Metrics

</h2>

<Table>

<TableHeader>

<TableRow>

<TableHead>

Metric

</TableHead>

<TableHead>

Value

</TableHead>

</TableRow>

</TableHeader>

<TableBody>

<TableRow>

<TableCell>

Revenue Growth

</TableCell>

<TableCell>

{metrics.revenue_growth}%

</TableCell>

</TableRow>

<TableRow>

<TableCell>

Net Margin

</TableCell>

<TableCell>

{metrics.net_margin}%

</TableCell>

</TableRow>

<TableRow>

<TableCell>

ROE

</TableCell>

<TableCell>

{metrics.roe}%

</TableCell>

</TableRow>

<TableRow>

<TableCell>

ROA

</TableCell>

<TableCell>

{metrics.roa}%

</TableCell>

</TableRow>

<TableRow>

<TableCell>

Debt / Equity

</TableCell>

<TableCell>

{metrics.debt_equity}

</TableCell>

</TableRow>

<TableRow>

<TableCell>

Free Cash Flow

</TableCell>

<TableCell>

₹ {metrics.free_cash_flow.toLocaleString()}

</TableCell>

</TableRow>

</TableBody>

</Table>

</div>

);

}