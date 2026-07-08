import type { ReportBlock } from "@/types/api";

interface Props {
  report: ReportBlock[];
}

export default function ReportViewer({
  report,
}: Props) {
  return (
    <div className="rounded-xl border border-[#3a331f] bg-[#161410] p-6 shadow-lg">

      <h2 className="mb-8 text-2xl font-bold text-[#f4ecd8]">
        Research Report
      </h2>

      <div className="space-y-5">

        {report.map((block, index) => {

          if (block.type === "heading") {
            if (block.level === "h1") {
              return (
                <h1
                  key={index}
                  className="mt-10 border-b border-[#3a331f] pb-3 text-3xl font-bold text-[#f2cf6b]"
                >
                  {block.text}
                </h1>
              );
            }

            return (
              <h2
                key={index}
                className="mt-8 text-2xl font-bold text-[#f2cf6b]"
              >
                {block.text}
              </h2>
            );
          }

          if (block.type === "paragraph") {
            return (
              <p
                key={index}
                className="leading-8 text-[#c9c0a3]"
              >
                {block.text}
              </p>
            );
          }

          if (block.type === "bullet_list") {
            return (
              <ul
                key={index}
                className="list-disc space-y-3 pl-6 text-[#c9c0a3]"
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