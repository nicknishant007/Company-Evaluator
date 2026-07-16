import type { ReportBlock } from "@/types/api";

interface Props {
  report: ReportBlock[];
}

export default function ReportViewer({
  report,
}: Props) {
  return (
    <div className="rounded-2xl border border-border bg-card p-6 shadow-[0_10px_30px_-18px_rgba(124,92,255,0.35)]">

      <h2 className="mb-8 text-2xl font-bold text-foreground">
        Research Report
      </h2>

      <div className="space-y-5">

        {report.map((block, index) => {

          if (block.type === "heading") {
            if (block.level === "h1") {
              return (
                <h1
                  key={index}
                  className="mt-10 border-b border-border pb-3 text-3xl font-bold text-[#5b3fd6]"
                >
                  {block.text}
                </h1>
              );
            }

            return (
              <h2
                key={index}
                className="mt-8 text-2xl font-bold text-[#5b3fd6]"
              >
                {block.text}
              </h2>
            );
          }

          if (block.type === "paragraph") {
            return (
              <p
                key={index}
                className="leading-8 text-muted-foreground"
              >
                {block.text}
              </p>
            );
          }

          if (block.type === "bullet_list") {
            return (
              <ul
                key={index}
                className="list-disc space-y-3 pl-6 text-muted-foreground"
              >
                {block.items.map((item, itemIndex) => (
                  <li
                    key={itemIndex}
                    className="leading-7"
                  >
                    {item}
                  </li>
                ))}
              </ul>
            );
          }

          return null;
        })}

      </div>

    </div>
  );
}
