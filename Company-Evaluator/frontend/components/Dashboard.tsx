import DashboardHeader from "./DashboardHeader";
import FinancialTable from "./FinancialTable";
import FinancialChart from "./FinancialChart";
import ReportViewer from "./ReportViewer";
import DownloadSection from "./DownloadSection";

interface Props {

    data: any;

}

export default function Dashboard({
    data,
}:Props) {

    
    
    // const data=dummyData;

    return (

        <div className="max-w-7xl mx-auto space-y-8 p-8"
>

            <DashboardHeader

                company={data.company}

                ticker={data.ticker}

                industry={data.industry}

                recommendation={data.recommendation}

            />

            <div className="grid grid-cols-1 xl:grid-cols-2 gap-6">

                <FinancialTable

                    metrics={data.financial_metrics}

                />

                <FinancialChart

                    metrics={data.financial_metrics}

                />

            </div>

            <ReportViewer

                report={data.report}

            />

            <DownloadSection

                report={data.report_url}

                pdf={data.pdf_url}

                slides={data.slides_url}

            />

        </div>

    );

}