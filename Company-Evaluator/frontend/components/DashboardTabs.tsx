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

            <TabsList>

                <TabsTrigger value="overview">

                    Company

                </TabsTrigger>

                <TabsTrigger value="financial">

                    Financial

                </TabsTrigger>

                <TabsTrigger value="news">

                    News

                </TabsTrigger>

                <TabsTrigger value="risk">

                    Risk

                </TabsTrigger>

                <TabsTrigger value="valuation">

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

            <TabsContent value="news">

                News Analysis

            </TabsContent>

            <TabsContent value="risk">

                Risk Analysis

            </TabsContent>

            <TabsContent value="valuation">

                Valuation Analysis

            </TabsContent>

        </Tabs>

    )

}