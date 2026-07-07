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
    <div className="mt-8 rounded-xl border border-[#3a331f] bg-[#161410] p-6 shadow-lg">

      <h2 className="mb-6 text-xl font-bold text-[#f4ecd8]">

        AI Pipeline

      </h2>

      <div className="space-y-4">

        {steps.map((step, index) => (

          <div
            key={index}
            className="flex items-center gap-3"
          >

            <div
              className="h-3 w-3 animate-pulse rounded-full bg-[#d4af37] shadow-[0_0_8px_2px_rgba(212,175,55,0.6)]"
              style={{ animationDelay: `${index * 120}ms` }}
            />

            <p className="text-[#c9c0a3]">{step}</p>

          </div>

        ))}

      </div>

    </div>
  );
}
