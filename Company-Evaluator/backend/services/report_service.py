from pathlib import Path


class ReportService:

    REPORT_DIR = Path("outputs/reports")

    def __init__(self):
        self.REPORT_DIR.mkdir(parents=True, exist_ok=True)

    def save_report(
        self,
        ticker: str,
        report: str,
    ):

        report_path = self.REPORT_DIR / f"{ticker}_Report.md"

        report_path.write_text(
            report,
            encoding="utf-8",
        )

        return report_path

    def get_report(
        self,
        ticker: str,
    ):

        report_path = self.REPORT_DIR / f"{ticker}_Report.md"

        if not report_path.exists():
            return None

        return report_path.read_text(
            encoding="utf-8"
        )


report_service = ReportService()