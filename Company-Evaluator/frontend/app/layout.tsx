import "./globals.css";
import ReactQueryProvider from "@/providers/ReactQueryProvider";

export const metadata = {
  title: "Company Evaluator",
  description: "AI Company Evaluation Platform",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <ReactQueryProvider>{children}</ReactQueryProvider>
      </body>
    </html>
  );
}
