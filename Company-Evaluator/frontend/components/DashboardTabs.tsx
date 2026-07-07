"use client";

import {

Tabs,

TabsContent,

TabsList,

TabsTrigger,

} from "@/components/ui/tabs";

import OverviewTab from "./OverviewTab";

import FinancialTab from "./FinancialTab";

interface Props{

    data:any;

}

export default function DashboardTabs({

    data,

}:Props){

    return(

        <Tabs defaultValue="overview">

            <TabsList className="border border-[#3a331f] bg-[#1c1810]">

                <TabsTrigger value="overview" className="text-[#a89968] data-active:bg-[#d4af37]/15 data-active:text-[#f2cf6b]">

                    Company

                </TabsTrigger>

                <TabsTrigger value="financial" className="text-[#a89968] data-active:bg-[#d4af37]/15 data-active:text-[#f2cf6b]">

                    Financial

                </TabsTrigger>

                <TabsTrigger value="news" className="text-[#a89968] data-active:bg-[#d4af37]/15 data-active:text-[#f2cf6b]">

                    News

                </TabsTrigger>

                <TabsTrigger value="risk" className="text-[#a89968] data-active:bg-[#d4af37]/15 data-active:text-[#f2cf6b]">

                    Risk

                </TabsTrigger>

                <TabsTrigger value="valuation" className="text-[#a89968] data-active:bg-[#d4af37]/15 data-active:text-[#f2cf6b]">

                    Valuation

                </TabsTrigger>

            </TabsList>

            <TabsContent value="overview">

                <OverviewTab

                    company={data.company}

                    industry={data.industry}

                />

            </TabsContent>

            <TabsContent value="financial">

                <FinancialTab

                    report="Financial Report Coming From API"

                />

            </TabsContent>

            <TabsContent value="news" className="text-[#c9c0a3]">

                News Analysis

            </TabsContent>

            <TabsContent value="risk" className="text-[#c9c0a3]">

                Risk Analysis

            </TabsContent>

            <TabsContent value="valuation" className="text-[#c9c0a3]">

                Valuation Analysis

            </TabsContent>

        </Tabs>

    )

}
