from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from io import BytesIO
from datetime import date

NAVY   = colors.HexColor("#0F2B4C")
BLUE   = colors.HexColor("#1A6DB5")
GREEN  = colors.HexColor("#27AE60")
ORANGE = colors.HexColor("#E67E22")
RED    = colors.HexColor("#E74C3C")
LIGHT  = colors.HexColor("#F4F6FA")
GREY   = colors.HexColor("#7F8C8D")


def score_color(score):
    if score >= 75:
        return GREEN
    if score >= 50:
        return ORANGE
    return RED


def score_label(score):
    if score >= 75:
        return "Conforme"
    if score >= 50:
        return "Partiellement conforme"
    return "Non conforme"


def generate_pdf(company_name, global_score, category_scores, action_plan, answers):
    buf = BytesIO()
    doc = SimpleDocTemplate(
        buf, pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=2*cm, bottomMargin=2*cm,
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle("title", fontSize=22, textColor=colors.white,
                                  fontName="Helvetica-Bold", alignment=TA_CENTER, spaceAfter=4)
    subtitle_style = ParagraphStyle("subtitle", fontSize=11, textColor=colors.white,
                                     fontName="Helvetica", alignment=TA_CENTER)
    h1 = ParagraphStyle("h1", fontSize=14, textColor=NAVY,
                          fontName="Helvetica-Bold", spaceBefore=14, spaceAfter=6)
    h2 = ParagraphStyle("h2", fontSize=11, textColor=BLUE,
                          fontName="Helvetica-Bold", spaceBefore=8, spaceAfter=4)
    body = ParagraphStyle("body", fontSize=9, textColor=colors.black,
                           fontName="Helvetica", spaceAfter=4, leading=13)
    small = ParagraphStyle("small", fontSize=8, textColor=GREY,
                            fontName="Helvetica", spaceAfter=2)
    center = ParagraphStyle("center", fontSize=9, alignment=TA_CENTER)

    story = []

    # Header banner
    header_data = [[
        Paragraph(f"RAPPORT D'AUDIT RGPD", title_style),
        Paragraph(f"{company_name}<br/><font size=9>Généré le {date.today().strftime('%d/%m/%Y')}</font>", subtitle_style),
    ]]
    header_table = Table(header_data, colWidths=[10*cm, 7*cm])
    header_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 16),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 16),
        ("ROUNDEDCORNERS", [6]),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 0.4*cm))

    # Global score box
    sc = round(global_score)
    sc_color = score_color(sc)
    sc_lbl = score_label(sc)
    score_data = [[
        Paragraph(f"<b>Score global de conformité</b>", ParagraphStyle("x", fontSize=12, textColor=colors.white, fontName="Helvetica-Bold")),
        Paragraph(f"<b>{sc} %</b>", ParagraphStyle("x2", fontSize=28, textColor=colors.white, fontName="Helvetica-Bold", alignment=TA_CENTER)),
        Paragraph(f"<b>{sc_lbl}</b>", ParagraphStyle("x3", fontSize=11, textColor=colors.white, fontName="Helvetica-Bold", alignment=TA_CENTER)),
    ]]
    score_tbl = Table(score_data, colWidths=[8*cm, 4*cm, 5*cm])
    score_tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), sc_color),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
    ]))
    story.append(score_tbl)
    story.append(Spacer(1, 0.5*cm))

    # Category scores table
    story.append(Paragraph("Résultats par domaine", h1))
    story.append(HRFlowable(width="100%", thickness=1, color=BLUE))
    story.append(Spacer(1, 0.2*cm))

    cat_header = [
        Paragraph("<b>Domaine</b>", ParagraphStyle("th", fontSize=9, fontName="Helvetica-Bold", textColor=colors.white)),
        Paragraph("<b>Score</b>", ParagraphStyle("th2", fontSize=9, fontName="Helvetica-Bold", textColor=colors.white, alignment=TA_CENTER)),
        Paragraph("<b>Statut</b>", ParagraphStyle("th3", fontSize=9, fontName="Helvetica-Bold", textColor=colors.white, alignment=TA_CENTER)),
        Paragraph("<b>Barre de progression</b>", ParagraphStyle("th4", fontSize=9, fontName="Helvetica-Bold", textColor=colors.white)),
    ]
    cat_rows = [cat_header]
    for cat in category_scores:
        s = cat["score"]
        bar_filled = max(1, int(s / 5))
        bar_empty = 20 - bar_filled
        bar = "█" * bar_filled + "░" * bar_empty
        bar_color = score_color(s)
        cat_rows.append([
            Paragraph(f"{cat['icon']} {cat['label']}", body),
            Paragraph(f"<b>{s}%</b>", ParagraphStyle("sc", fontSize=10, fontName="Helvetica-Bold",
                                                       textColor=score_color(s), alignment=TA_CENTER)),
            Paragraph(score_label(s), ParagraphStyle("lb", fontSize=8, alignment=TA_CENTER,
                                                      textColor=score_color(s))),
            Paragraph(f"<font color='#{bar_color.hexval()[2:]}'>{bar}</font>", small),
        ])

    cat_table = Table(cat_rows, colWidths=[6*cm, 2*cm, 4*cm, 5*cm])
    cat_style = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("BACKGROUND", (0, 1), (-1, -1), LIGHT),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#D0D8E4")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]
    cat_table.setStyle(TableStyle(cat_style))
    story.append(cat_table)
    story.append(Spacer(1, 0.5*cm))

    # Action plan
    if action_plan:
        story.append(Paragraph("Plan d'action prioritaire", h1))
        story.append(HRFlowable(width="100%", thickness=1, color=BLUE))
        story.append(Spacer(1, 0.2*cm))

        priority_order = {"haute": 0, "moyenne": 1, "faible": 2}
        sorted_actions = sorted(action_plan, key=lambda x: priority_order.get(x.get("priority", "faible"), 2))

        for i, action in enumerate(sorted_actions, 1):
            prio = action.get("priority", "moyenne")
            prio_color = RED if prio == "haute" else (ORANGE if prio == "moyenne" else GREEN)
            prio_label = {"haute": "⚡ PRIORITÉ HAUTE", "moyenne": "⚠ PRIORITÉ MOYENNE", "faible": "✓ PRIORITÉ FAIBLE"}.get(prio, prio)

            block = [
                [
                    Paragraph(f"<b>{i}. {action['category']}</b>", ParagraphStyle("ah", fontSize=9, fontName="Helvetica-Bold", textColor=NAVY)),
                    Paragraph(f"<font color='#{prio_color.hexval()[2:]}'>{prio_label}</font>",
                              ParagraphStyle("ap", fontSize=8, fontName="Helvetica-Bold", alignment=TA_RIGHT)),
                ],
                [
                    Paragraph(action["recommendation"], ParagraphStyle("ar", fontSize=9, leading=13)),
                    "",
                ],
            ]
            action_tbl = Table(block, colWidths=[12*cm, 5*cm])
            action_tbl.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("SPAN", (0, 1), (1, 1)),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#D0D8E4")),
                ("LINEBELOW", (0, 0), (-1, 0), 0.5, colors.HexColor("#D0D8E4")),
            ]))
            story.append(KeepTogether([action_tbl, Spacer(1, 0.2*cm)]))

    # CTA page
    story.append(Spacer(1, 0.5*cm))
    cta_content = [[
        Paragraph(
            "Accompagnement IA & Automatisation — Fahima B.",
            ParagraphStyle("cta_t", fontSize=13, textColor=colors.white, fontName="Helvetica-Bold", alignment=TA_CENTER)
        ),
        Paragraph(
            "Cheffe Projet IA & No-Code | Formation OREEGAMI<br/>"
            "<br/>Je vous accompagne pour transformer cet audit en conformité réelle, grâce à l'automatisation :<br/>"
            "<br/>✅ <b>Audit RGPD approfondi</b> — analyse complète de vos traitements et processus<br/>"
            "✅ <b>Rédaction des documents obligatoires</b> — registre, politique, mentions légales, DPA<br/>"
            "✅ <b>Automatisation RGPD</b> — workflows Make/Airtable, purge automatique, alertes<br/>"
            "✅ <b>Formation de vos équipes</b> — sensibilisation IA et bonnes pratiques<br/>"
            "✅ <b>Suivi & veille réglementaire</b> — restez conformes dans la durée<br/>",
            ParagraphStyle("cta_b", fontSize=10, textColor=colors.white, fontName="Helvetica", leading=16)
        ),
        Paragraph(
            "💼 LinkedIn : linkedin.com/in/fahima-be  |  📅 Calendly : calendly.com/horizonsdatas/30min",
            ParagraphStyle("cta_c", fontSize=10, textColor=colors.white, fontName="Helvetica-Bold", alignment=TA_CENTER)
        ),
    ]]
    cta_table = Table([[row] for row in cta_content[0:1]] + [[row] for row in cta_content[1:]], colWidths=[17*cm])
    cta_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 16),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story.append(cta_table)

    # Footer note
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        f"Rapport généré le {date.today().strftime('%d/%m/%Y')} — Outil conçu par Fahima B. | Cheffe Projet IA & No-Code | OREEGAMI<br/>"
        "Ce rapport est fourni à titre informatif. Il ne constitue pas un avis juridique.",
        ParagraphStyle("footer", fontSize=7, textColor=GREY, alignment=TA_CENTER, leading=11)
    ))

    doc.build(story)
    buf.seek(0)
    return buf
