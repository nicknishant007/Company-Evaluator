from markdown_it import MarkdownIt


class ReportParser:

    def __init__(self):

        self.md = MarkdownIt(
            "commonmark"
        ).enable("table")


    def clean(self, report: str) -> str:

        if not report:

            return ""

        cleaned_report = report.strip()

        # Remove accidental outer code fences
        if cleaned_report.startswith("```markdown"):

            cleaned_report = cleaned_report[
                len("```markdown"):
            ]

        elif cleaned_report.startswith("```md"):

            cleaned_report = cleaned_report[
                len("```md"):
            ]

        elif cleaned_report.startswith("```"):

            cleaned_report = cleaned_report[3:]


        if cleaned_report.endswith("```"):

            cleaned_report = cleaned_report[:-3]


        return cleaned_report.strip()


    def clean_text(self, text: str) -> str:

        return (
            text
            .replace("**", "")
            .replace("__", "")
            .strip()
        )


    def parse(self, report: str):

        tokens = self.md.parse(report)

        blocks = []

        i = 0


        while i < len(tokens):

            token = tokens[i]


            # Heading
            if token.type == "heading_open":

                blocks.append({
                    "type": "heading",
                    "level": token.tag,
                    "text": self.clean_text(
                        tokens[i + 1].content
                    ),
                })

                i += 3

                continue


            # Paragraph
            if token.type == "paragraph_open":

                if (
                    i + 1 < len(tokens)
                    and tokens[i + 1].type == "inline"
                ):

                    blocks.append({
                        "type": "paragraph",
                        "text": self.clean_text(
                            tokens[i + 1].content
                        ),
                    })

                i += 3

                continue


            # Bullet list
            if token.type == "bullet_list_open":

                items = []

                i += 1


                while (
                    i < len(tokens)
                    and tokens[i].type
                    != "bullet_list_close"
                ):

                    if tokens[i].type == "inline":

                        items.append(
                            self.clean_text(
                                tokens[i].content
                            )
                        )

                    i += 1


                blocks.append({
                    "type": "bullet_list",
                    "items": items,
                })

                i += 1

                continue


            # Ordered list
            if token.type == "ordered_list_open":

                items = []

                i += 1


                while (
                    i < len(tokens)
                    and tokens[i].type
                    != "ordered_list_close"
                ):

                    if tokens[i].type == "inline":

                        items.append(
                            self.clean_text(
                                tokens[i].content
                            )
                        )

                    i += 1


                blocks.append({
                    "type": "ordered_list",
                    "items": items,
                })

                i += 1

                continue


            # Table
            if token.type == "table_open":

                rows = []

                current_row = []

                i += 1


                while (
                    i < len(tokens)
                    and tokens[i].type != "table_close"
                ):

                    current_token = tokens[i]


                    if current_token.type == "tr_open":

                        current_row = []


                    elif current_token.type == "inline":

                        current_row.append(
                            self.clean_text(
                                current_token.content
                            )
                        )


                    elif current_token.type == "tr_close":

                        if current_row:

                            rows.append(current_row)


                    i += 1


                if rows:

                    blocks.append({
                        "type": "table",
                        "rows": rows,
                    })


                i += 1

                continue


            # Horizontal separator
            if token.type == "hr":

                blocks.append({
                    "type": "separator"
                })


            i += 1


        return blocks