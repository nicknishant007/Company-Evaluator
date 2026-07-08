from pathlib import Path

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    ListFlowable,
    ListItem,
    Table,
    TableStyle,
    HRFlowable,
)

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm

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
        output_path=None,
    ):

        if output_path is None:

            output_path = (
                f"outputs/"
                f"{state['ticker']}_Report.pdf"
            )

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )


        doc = SimpleDocTemplate(
            str(output_path),

            pagesize=A4,

            rightMargin=18 * mm,
            leftMargin=18 * mm,
            topMargin=18 * mm,
            bottomMargin=18 * mm,
        )


        elements = []


        # ======================================
        # Cover
        # ======================================
        elements.append(
            Paragraph(
                f"{state['ticker']} Research Report",
                TITLE_STYLE,
            )
        )

        elements.append(
            Spacer(
                1,
                25,
            )
        )


        # ======================================
        # Parsed report
        # ======================================
        blocks = state["parsed_report"]


        for block in blocks:

            block_type = block["type"]


            # ==================================
            # Heading
            # ==================================
            if block_type == "heading":

                if block["level"] == "h1":

                    style = H1_STYLE

                else:

                    style = H2_STYLE


                elements.append(
                    Paragraph(
                        block["text"],
                        style,
                    )
                )


            # ==================================
            # Paragraph
            # ==================================
            elif block_type == "paragraph":

                elements.append(
                    Paragraph(
                        block["text"],
                        BODY_STYLE,
                    )
                )

                elements.append(
                    Spacer(
                        1,
                        8,
                    )
                )


            # ==================================
            # Bullet List
            # ==================================
            elif block_type == "bullet_list":

                bullet_items = []


                for item in block["items"]:

                    bullet_items.append(
                        ListItem(
                            Paragraph(
                                item,
                                BODY_STYLE,
                            )
                        )
                    )


                elements.append(
                    ListFlowable(
                        bullet_items,
                        bulletType="bullet",
                    )
                )

                elements.append(
                    Spacer(
                        1,
                        10,
                    )
                )


            # ==================================
            # Ordered List
            # ==================================
            elif block_type == "ordered_list":

                ordered_items = []


                for item in block["items"]:

                    ordered_items.append(
                        ListItem(
                            Paragraph(
                                item,
                                BODY_STYLE,
                            )
                        )
                    )


                elements.append(
                    ListFlowable(
                        ordered_items,
                        bulletType="1",
                    )
                )

                elements.append(
                    Spacer(
                        1,
                        10,
                    )
                )


            # ==================================
            # Table
            # ==================================
            elif block_type == "table":

                rows = block["rows"]


                if not rows:

                    continue


                table_data = []


                for row in rows:

                    table_row = []


                    for cell in row:

                        table_row.append(
                            Paragraph(
                                cell,
                                BODY_STYLE,
                            )
                        )


                    table_data.append(
                        table_row
                    )


                table = Table(
                    table_data,

                    repeatRows=1,

                    hAlign="LEFT",
                )


                table.setStyle(
                    TableStyle([

                        (
                            "BACKGROUND",
                            (0, 0),
                            (-1, 0),
                            colors.lightgrey,
                        ),

                        (
                            "TEXTCOLOR",
                            (0, 0),
                            (-1, 0),
                            colors.black,
                        ),

                        (
                            "FONTNAME",
                            (0, 0),
                            (-1, 0),
                            "Helvetica-Bold",
                        ),

                        (
                            "GRID",
                            (0, 0),
                            (-1, -1),
                            0.5,
                            colors.grey,
                        ),

                        (
                            "VALIGN",
                            (0, 0),
                            (-1, -1),
                            "TOP",
                        ),

                        (
                            "LEFTPADDING",
                            (0, 0),
                            (-1, -1),
                            6,
                        ),

                        (
                            "RIGHTPADDING",
                            (0, 0),
                            (-1, -1),
                            6,
                        ),

                        (
                            "TOPPADDING",
                            (0, 0),
                            (-1, -1),
                            5,
                        ),

                        (
                            "BOTTOMPADDING",
                            (0, 0),
                            (-1, -1),
                            5,
                        ),

                    ])
                )


                elements.append(
                    table
                )

                elements.append(
                    Spacer(
                        1,
                        12,
                    )
                )


            # ==================================
            # Separator
            # ==================================
            elif block_type == "separator":

                elements.append(
                    HRFlowable(
                        width="100%",
                        thickness=0.5,
                    )
                )

                elements.append(
                    Spacer(
                        1,
                        10,
                    )
                )


        # ======================================
        # Generate PDF
        # ======================================
        doc.build(
            elements
        )


        return str(output_path)