import api from "./api";
import { AnalyzeRequest, AnalyzeResponse } from "@/types/api";

export async function analyzeCompany(
  data: AnalyzeRequest
): Promise<AnalyzeResponse> {

  const response = await api.post<AnalyzeResponse>(
    "/analyze",
    data
  );

  return response.data;
}
