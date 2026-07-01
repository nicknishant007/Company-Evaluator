from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    ListFlowable,
    ListItem,
)

from exporters.style import (
    TITLE_STYLE,
    H1_STYLE,
    H2_STYLE,
    BODY_STYLE,
)


class PDFExporter:

    def export(
        self,
        state,
        output_path,
    ):

        output_path = (
            f"outputs/{state['ticker']}_Report.pdf"
        )

        doc = SimpleDocTemplate(output_path)

        elements = []

        # Cover
        elements.append(
            Paragraph(
                f"{state['ticker']} Research Report",
                TITLE_STYLE
            )
        )

        elements.append(
            Spacer(1, 25)
        )

        blocks = state["parsed_report"]

        for block in blocks:

            # ==================
            # Heading
            # ==================
            if block["type"] == "heading":

                if block["level"] == "h1":

                    style = H1_STYLE

                else:

                    style = H2_STYLE

                elements.append(
                    Paragraph(
                        block["text"],
                        style
                    )
                )

            # ==================
            # Paragraph
            # ==================
            elif block["type"] == "paragraph":

                elements.append(
                    Paragraph(
                        block["text"],
                        BODY_STYLE
                    )
                )

                elements.append(
                    Spacer(
                        1,
                        8
                    )
                )

            # ==================
            # Bullet List
            # ==================
            elif block["type"] == "bullet_list":

                bullet_items = []

                for item in block["items"]:

                    bullet_items.append(
                        ListItem(
                            Paragraph(
                                item,
                                BODY_STYLE
                            )
                        )
                    )

                elements.append(
                    ListFlowable(
                        bullet_items,
                        bulletType="bullet"
                    )
                )

                elements.append(
                    Spacer(
                        1,
                        10
                    )
                )

        doc.build(elements)