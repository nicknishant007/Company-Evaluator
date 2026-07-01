interface Props {
  loading: boolean;
}

export default function LoadingTimeline({ loading }: Props) {

  if (!loading) return null;

  const steps = [
    "Collecting Company Data",
    "Calculating Financial Ratios",
    "Analyzing Financial Statements",
    "Analyzing News",
    "Risk Assessment",
    "Valuation",
    "Generating Research Report",
  ];

  return (
    <div className="mt-8 rounded-xl border bg-white p-6 shadow">

      <h2 className="mb-6 text-xl font-bold">

        AI Pipeline

      </h2>

      <div className="space-y-4">

        {steps.map((step, index) => (

          <div
            key={index}
            className="flex items-center gap-3"
          >

            <div className="h-3 w-3 animate-pulse rounded-full bg-blue-500"/>

            <p>{step}</p>

          </div>

        ))}

      </div>

    </div>
  );
}