import DashboardHeader from "./DashboardHeader";
import FinancialTable from "./FinancialTable";
import FinancialChart from "./FinancialChart";
import ReportViewer from "./ReportViewer";
import DownloadSection from "./DownloadSection";

import type { AnalyzeResponse } from "@/types/api";

interface Props {
  data: AnalyzeResponse;
}

export default function Dashboard({
  data,
}: Props) {
  return (
    <div className="mx-auto max-w-7xl space-y-8 p-2 py-8 sm:p-8">
      <DashboardHeader
        company={data.company}
        ticker={data.ticker}
        industry={data.industry}
        recommendation={data.recommendation}
      />

      <div className="grid grid-cols-1 gap-6 xl:grid-cols-2">
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