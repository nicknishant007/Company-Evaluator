from exporters.markdown_exporter import (
    MarkdownExporter
)

from exporters.pdf_exporter import (
    PDFExporter
)


async def export_node(state):

    markdown_exporter = MarkdownExporter()

    pdf_exporter = PDFExporter()

    markdown_path = markdown_exporter.export(state)


    pdf_path = pdf_exporter.export(state)

    print("\n========== EXPORT OUTPUT ==========" )

    print("Markdown:",markdown_path)

    print("PDF:",pdf_path)

    print("===================================\n")


    return {

        "markdown_path":markdown_path,

        "pdf_path":pdf_path,

    }