from pathlib import Path


class MarkdownExporter:

    def export(
        self,
        state,
        output_path=None,
    ):

        if output_path is None:

            output_path = (
                f"outputs/"
                f"{state['ticker']}_Report.md"
            )

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path.write_text(
            state["cleaned_report"],
            encoding="utf-8",
        )

        return str(output_path)