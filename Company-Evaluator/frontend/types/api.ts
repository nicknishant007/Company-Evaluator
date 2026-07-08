export interface AnalyzeRequest {
  ticker: string;
}

export interface FinancialMetrics {
  revenue_growth: number | null;
  net_margin: number | null;
  roe: number | null;
  roa: number | null;
  debt_equity: number | null;
  free_cash_flow: number | null;
}

export interface HeadingBlock {
  type: "heading";
  level: string;
  text: string;
}

export interface ParagraphBlock {
  type: "paragraph";
  text: string;
}

export interface BulletListBlock {
  type: "bullet_list";
  items: string[];
}

export type ReportBlock =
  | HeadingBlock
  | ParagraphBlock
  | BulletListBlock;

export interface AnalyzeResponse {
  company: string;
  ticker: string;
  industry: string | null;
  recommendation: string | null;
  overall_risk: string | null;
  financial_metrics: FinancialMetrics;
  report: ReportBlock[];
  status: string;
  report_url: string;
  pdf_url: string;
  slides_url: string | null;
}