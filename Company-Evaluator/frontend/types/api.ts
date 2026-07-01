export interface AnalyzeRequest {
  ticker: string;
}

export interface FinancialMetrics {

    revenue_growth:number | null;

    net_margin:number | null;

    roe:number | null;

    roa:number | null;

    debt_equity:number | null;

    free_cash_flow:number | null;

}

export interface AnalyzeResponse{

    company:string;

    ticker:string;

    industry:string;

    recommendation:string;

    overall_risk:string;

    financial_metrics:FinancialMetrics;

    report:string;

    status:string;

    report_url:string;

    pdf_url:string;

    slides_url:string;

}