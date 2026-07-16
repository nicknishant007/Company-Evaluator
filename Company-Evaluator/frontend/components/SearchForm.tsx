"use client";

import axios from "axios";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import { Search } from "lucide-react";
import Dashboard from "./Dashboard";

import { useAnalyze } from "@/hooks/useAnalyze";

const schema = z.object({

    ticker: z.string()

        .min(1, "Ticker is required")

        .max(20)

});

type FormData = z.infer<typeof schema>;

export default function SearchForm() {

    const mutation = useAnalyze();

    const {

        register,

        handleSubmit,

        formState: {

            errors

        }

    } = useForm<FormData>({

        resolver: zodResolver(schema)

    });

    function onSubmit(data: FormData) {

        console.log("Submitting:",data)

        mutation.mutate(data,{

        onSuccess: (res) => {

            console.log("SUCCESS");

            console.log(res);

        },

        onError: (err) => {
    if (axios.isAxiosError(err)) {
        console.log("STATUS:", err.response?.status);
        console.log("BACKEND DATA:", err.response?.data);
        console.log("MESSAGE:", err.message);
    } else {
        console.log("UNKNOWN ERROR:", err);
    }
}

    });

    }

    return (

        <div className="mt-10">

            <form

                onSubmit={handleSubmit(onSubmit)}

                className="space-y-5"

            >

                <div className="relative">

                    <Search className="pointer-events-none absolute top-1/2 left-4 size-4 -translate-y-1/2 text-muted-foreground" />

                    <input

                        {...register("ticker")}

                        placeholder="Enter Company Ticker (e.g. HDFCBANK.NS)"

                        className="w-full rounded-xl border border-border bg-muted p-3 pl-11 text-foreground placeholder:text-muted-foreground outline-none transition focus:border-[#7c5cff] focus:ring-2 focus:ring-[#7c5cff]/25"

                    />

                </div>

                {errors.ticker && (

                    <p className="text-sm text-destructive">

                        {errors.ticker.message}

                    </p>

                )}

                <button

                    type="submit"

                    disabled={mutation.isPending}

                    className="w-full rounded-xl bg-gradient-to-r from-[#7c5cff] via-[#a78bfa] to-[#ec4899] bg-[length:200%_auto] px-6 py-3 font-semibold text-white shadow-[0_10px_28px_-8px_rgba(124,92,255,0.7)] transition hover:bg-right disabled:cursor-not-allowed disabled:opacity-60 sm:w-auto"

                >

                    {

                        mutation.isPending

                        ?

                        "Analyzing..."

                        :

                        "Analyze"

                    }

                </button>

                {mutation.isError && (

                    <p className="text-sm text-destructive">

                        Something went wrong. Please try again.

                    </p>

                )}

            </form>

            {

                mutation.isSuccess && (

                    <Dashboard

                    data={mutation.data}

                    />

                )

            }

        </div>

    );

}
