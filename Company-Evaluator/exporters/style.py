from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle

styles = getSampleStyleSheet()

TITLE_STYLE = styles["Title"]

H1_STYLE = ParagraphStyle(
    "H1",
    parent=styles["Heading1"],
    fontSize=18,
    spaceBefore=20,
    spaceAfter=12
)

H2_STYLE = ParagraphStyle(
    "H2",
    parent=styles["Heading2"],
    fontSize=14,
    spaceBefore=15,
    spaceAfter=10
)

BODY_STYLE = ParagraphStyle(
    "Body",
    parent=styles["BodyText"],
    fontSize=11,
    leading=18,
    spaceAfter=8
)