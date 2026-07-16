import "./globals.css";
import ReactQueryProvider from "@/providers/ReactQueryProvider";
import Sidebar from "@/components/Sidebar";

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
        <ReactQueryProvider>
          <div className="flex min-h-screen">
            <Sidebar />
            <div className="min-w-0 flex-1">{children}</div>
          </div>
        </ReactQueryProvider>
      </body>
    </html>
  );
}
