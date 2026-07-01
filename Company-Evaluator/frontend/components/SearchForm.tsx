"use client";

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

            console.error("ERROR");

            console.error(err);

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

                    placeholder="Enter Company Ticker"

                    className="w-full rounded-lg border p-3"

                />

                {errors.ticker && (

                    <p className="text-red-500">

                        {errors.ticker.message}

                    </p>

                )}

                <button

                    type="submit"

                    disabled={mutation.isPending}

                    className="rounded-lg bg-black px-6 py-3 text-white"

                >

                    {

                        mutation.isPending

                        ?

                        "Analyzing..."

                        :

                        "Analyze"

                    }

                </button>

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