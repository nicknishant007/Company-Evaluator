"use client";

import axios from "axios";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
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

                <input

                    {...register("ticker")}

                    placeholder="Enter Company Ticker (e.g. HDFCBANK.NS)"

                    className="w-full rounded-lg border border-[#3a331f] bg-[#0e0d0b] p-3 text-[#f4ecd8] placeholder:text-[#6b6142] outline-none transition focus:border-[#d4af37] focus:ring-2 focus:ring-[#d4af37]/30"

                />

                {errors.ticker && (

                    <p className="text-sm text-red-400">

                        {errors.ticker.message}

                    </p>

                )}

                <button

                    type="submit"

                    disabled={mutation.isPending}

                    className="w-full rounded-lg bg-gradient-to-r from-[#8a6d1f] via-[#d4af37] to-[#8a6d1f] bg-[length:200%_auto] px-6 py-3 font-semibold text-[#161410] shadow-[0_4px_20px_-6px_rgba(212,175,55,0.6)] transition hover:bg-right disabled:cursor-not-allowed disabled:opacity-60 sm:w-auto"

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

                    <p className="text-sm text-red-400">

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
