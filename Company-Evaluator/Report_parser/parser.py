from markdown_it import MarkdownIt


class ReportParser:

    def __init__(self):
        self.md = MarkdownIt()

    def clean_text(self, text):
        return (
            text.replace("**", "")
                .replace("__", "")
                .strip()
        )

    def parse(self, report: str):

        tokens = self.md.parse(report)

        blocks = []

        i = 0

        while i < len(tokens):

            token = tokens[i]

            # =====================
            # Headings
            # =====================
            if token.type == "heading_open":

                level = token.tag

                title = self.clean_text(
                    tokens[i + 1].content
                )

                blocks.append(
                    {
                        "type": "heading",
                        "level": level,
                        "text": title,
                    }
                )

                i += 3
                continue

            # =====================
            # Paragraph
            # =====================
            if token.type == "paragraph_open":

                text = self.clean_text(
                    tokens[i + 1].content
                )

                blocks.append(
                    {
                        "type": "paragraph",
                        "text": text,
                    }
                )

                i += 3
                continue

            # =====================
            # Bullet List
            # =====================
            if token.type == "bullet_list_open":

                items = []

                i += 1

                while tokens[i].type != "bullet_list_close":

                    if tokens[i].type == "inline":

                        items.append(
                            self.clean_text(
                                tokens[i].content
                            )
                        )

                    i += 1

                blocks.append(
                    {
                        "type": "bullet_list",
                        "items": items,
                    }
                )

            i += 1

        return blocks