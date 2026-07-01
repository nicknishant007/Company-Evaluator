"use client";

import { useMutation } from "@tanstack/react-query";
import { analyzeCompany } from "@/services/company";

export function useAnalyze() {

    return useMutation({

        mutationFn: analyzeCompany,

    });

}