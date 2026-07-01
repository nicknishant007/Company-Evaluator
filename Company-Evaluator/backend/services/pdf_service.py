from pathlib import Path


class PDFService:

    def get_pdf(

        self,

        ticker: str,

    ):

        pdf_path = Path(

            f"outputs/pdf/{ticker}_Report.pdf"

        )

        if not pdf_path.exists():

            return None

        return pdf_path


pdf_service = PDFService()