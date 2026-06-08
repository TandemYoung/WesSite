#!/usr/bin/env python3
"""Generate a professional invoice PDF for the Wes Freeman campaign website build."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_RIGHT, TA_LEFT, TA_CENTER

# ---- Brand palette (matches the site) ----
NAVY = colors.HexColor("#0A2540")
RED = colors.HexColor("#B8202E")
CREAM = colors.HexColor("#FAF7F2")
GREY = colors.HexColor("#5A6472")
LIGHT = colors.HexColor("#E7E2D9")

OUT = "/home/user/WesSite/Invoice-WesFreeman-Website.pdf"

doc = SimpleDocTemplate(
    OUT, pagesize=letter,
    leftMargin=0.75 * inch, rightMargin=0.75 * inch,
    topMargin=0.7 * inch, bottomMargin=0.6 * inch,
    title="Invoice — Wes Freeman for State Representative Website",
    author="Web Services",
)

ss = getSampleStyleSheet()

def style(name, **kw):
    base = kw.pop("parent", ss["Normal"])
    return ParagraphStyle(name, parent=base, **kw)

h_brand = style("brand", fontName="Helvetica-Bold", fontSize=20, textColor=NAVY, leading=23)
h_sub = style("sub", fontName="Helvetica", fontSize=9.5, textColor=GREY, leading=13)
h_invoice = style("inv", fontName="Helvetica-Bold", fontSize=26, textColor=RED, leading=28, alignment=TA_RIGHT)
meta_r = style("metar", fontName="Helvetica", fontSize=9.5, textColor=NAVY, leading=14, alignment=TA_RIGHT)
label = style("label", fontName="Helvetica-Bold", fontSize=8, textColor=RED, leading=12, spaceAfter=2)
body = style("body", fontName="Helvetica", fontSize=9.5, textColor=NAVY, leading=13)
small = style("small", fontName="Helvetica", fontSize=8, textColor=GREY, leading=11)
small_i = style("smalli", fontName="Helvetica-Oblique", fontSize=8, textColor=GREY, leading=11)
sec = style("sec", fontName="Helvetica-Bold", fontSize=11, textColor=NAVY, leading=14, spaceBefore=6, spaceAfter=4)
cell = style("cell", fontName="Helvetica", fontSize=8.7, textColor=NAVY, leading=11)
cell_b = style("cellb", fontName="Helvetica-Bold", fontSize=8.7, textColor=NAVY, leading=11)
cell_r = style("cellr", fontName="Helvetica", fontSize=8.7, textColor=NAVY, leading=11, alignment=TA_RIGHT)
cell_hdr = style("cellh", fontName="Helvetica-Bold", fontSize=8.5, textColor=colors.white, leading=11)
cell_hdr_r = style("cellhr", fontName="Helvetica-Bold", fontSize=8.5, textColor=colors.white, leading=11, alignment=TA_RIGHT)
total_lbl = style("totlbl", fontName="Helvetica-Bold", fontSize=11, textColor=colors.white, leading=14, alignment=TA_RIGHT)
total_val = style("totval", fontName="Helvetica-Bold", fontSize=13, textColor=colors.white, leading=15, alignment=TA_RIGHT)

E = []

# ---------------- Header ----------------
left = [
    Paragraph("Wes Freeman for State Representative", h_brand),
    Paragraph("Custom Campaign Website &mdash; Design &amp; Development", h_sub),
]
right = [
    Paragraph("INVOICE", h_invoice),
    Spacer(1, 4),
    Paragraph("Invoice&nbsp;#: <b>WF-2026-001</b>", meta_r),
    Paragraph("Date: <b>June&nbsp;8,&nbsp;2026</b>", meta_r),
    Paragraph("Terms: <b>Net 15</b>", meta_r),
]
htbl = Table([[left, right]], colWidths=[3.9 * inch, 3.1 * inch])
htbl.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
]))
E.append(htbl)
E.append(Spacer(1, 8))
E.append(HRFlowable(width="100%", thickness=2, color=RED))
E.append(Spacer(1, 10))

# ---------------- From / To ----------------
frm = [
    Paragraph("FROM", label),
    Paragraph("Independent Web Developer / Studio", body),
    Paragraph("Arkansas River Valley", small),
    Paragraph("hello@yourstudio.example", small),
]
to = [
    Paragraph("BILL TO", label),
    Paragraph("Wes Freeman for State Representative", body),
    Paragraph("Republican &mdash; Arkansas State House, District 44", small),
    Paragraph("wesfreemanforstaterep.com", small),
]
ftbl = Table([[frm, to]], colWidths=[3.5 * inch, 3.5 * inch])
ftbl.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ("TOPPADDING", (0, 0), (-1, -1), 0),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
]))
E.append(ftbl)
E.append(Spacer(1, 14))

E.append(Paragraph("Project: 7-page custom-coded static campaign website", sec))
E.append(Paragraph(
    "Hand-written HTML/CSS (~1,000 lines, original design system), vanilla-JS mobile navigation, "
    "original fact-checked copywriting, custom SVG/graphic assets, third-party integrations "
    "(RaiseTheMoney donations, FormSubmit volunteer form, SMS opt-in scaffolding), full SEO/technical "
    "setup, legal &amp; compliance content, and deployment to GitHub Pages with a custom domain.",
    small))
E.append(Spacer(1, 10))

# ---------------- Line items ----------------
rows = [[
    Paragraph("#", cell_hdr),
    Paragraph("Service", cell_hdr),
    Paragraph("Hrs", cell_hdr_r),
    Paragraph("Rate", cell_hdr_r),
    Paragraph("Amount", cell_hdr_r),
]]

items = [
    ("1", "Discovery &amp; content strategy", "5", "$70", "$350"),
    ("2", "Visual design &amp; design system", "12", "$70", "$840"),
    ("3", "Front-end development (7 pages, ~1,000 lines CSS, JS nav, accessibility)", "26", "$70", "$1,820"),
    ("4", "Copywriting &mdash; fact-checked, all pages", "10", "$65", "$650"),
    ("5", "Custom graphics (logo treatment, flag SVG, vote badge, OG image)", "5", "$70", "$350"),
    ("6", "Integrations (RaiseTheMoney, FormSubmit, SMS scaffolding)", "4", "$70", "$280"),
    ("7", "SEO &amp; technical setup (Open Graph, sitemap, robots, manifest, favicons)", "5", "$70", "$350"),
    ("8", "Legal &amp; compliance content (privacy, SMS terms, AR disclosures)", "4", "$70", "$280"),
    ("9", "Deployment &amp; DNS (GitHub Pages, custom domain, QA)", "3", "$70", "$210"),
    ("10", "Revisions &amp; QA (two rounds)", "6", "$70", "$420"),
]
for r in items:
    rows.append([
        Paragraph(r[0], cell),
        Paragraph(r[1], cell),
        Paragraph(r[2], cell_r),
        Paragraph(r[3], cell_r),
        Paragraph(r[4], cell_r),
    ])

tbl = Table(rows, colWidths=[0.35 * inch, 4.05 * inch, 0.55 * inch, 0.75 * inch, 1.05 * inch], repeatRows=1)
ts = [
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("TOPPADDING", (0, 0), (-1, 0), 7),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 7),
    ("TOPPADDING", (0, 1), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 1), (-1, -1), 5),
    ("LEFTPADDING", (0, 0), (-1, -1), 7),
    ("RIGHTPADDING", (0, 0), (-1, -1), 7),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LINEBELOW", (0, 1), (-1, -2), 0.5, LIGHT),
    ("LINEBELOW", (0, -1), (-1, -1), 1, NAVY),
]
for i in range(1, len(rows)):
    if i % 2 == 0:
        ts.append(("BACKGROUND", (0, i), (-1, i), CREAM))
tbl.setStyle(TableStyle(ts))
E.append(tbl)
E.append(Spacer(1, 8))

# ---------------- Totals ----------------
tot_rows = [
    [Paragraph("Subtotal (80 hrs)", cell_r), Paragraph("$5,550", cell_r)],
    [Paragraph("Hosting (GitHub Pages)", cell_r), Paragraph("$0", cell_r)],
    [Paragraph("Domain registration (billed separately, ~$15/yr)", small), Paragraph("&mdash;", cell_r)],
]
tt = Table(tot_rows, colWidths=[2.4 * inch, 1.05 * inch], hAlign="RIGHT")
tt.setStyle(TableStyle([
    ("TOPPADDING", (0, 0), (-1, -1), 3),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ("RIGHTPADDING", (0, 0), (-1, -1), 7),
    ("LINEBELOW", (0, 0), (-1, 1), 0.5, LIGHT),
]))
E.append(tt)

grand = Table(
    [[Paragraph("TOTAL DUE", total_lbl), Paragraph("$5,550", total_val)]],
    colWidths=[2.4 * inch, 1.05 * inch], hAlign="RIGHT")
grand.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), RED),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ("RIGHTPADDING", (0, 0), (-1, -1), 7),
    ("LEFTPADDING", (0, 0), (-1, -1), 7),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
]))
E.append(Spacer(1, 2))
E.append(grand)
E.append(Spacer(1, 16))

# ---------------- Market context box ----------------
ctx = []
ctx.append(Paragraph("Market context &mdash; how this rate was set", sec))
ctx_rows = [
    [Paragraph("Build tier", cell_hdr), Paragraph("Comparable market price", cell_hdr), Paragraph("Source", cell_hdr_r)],
    [Paragraph("This invoice (AR-region freelancer, ~$70/hr blended)", cell_b), Paragraph("$5,550", cell), Paragraph("Line items above", cell_r)],
    [Paragraph("Industry survey &mdash; basic custom site", cell), Paragraph("$4,000&ndash;$8,000 (36% of firms)", cell), Paragraph("GoodFirms 2025", cell_r)],
    [Paragraph("Small-business site median", cell), Paragraph("~$5,000", cell), Paragraph("Clutch", cell_r)],
    [Paragraph("National freelancer / small agency", cell), Paragraph("$7,000&ndash;$10,000", cell), Paragraph("jim.com / agency data", cell_r)],
    [Paragraph("Full-service agency", cell), Paragraph("$12,000&ndash;$20,000+", cell), Paragraph("DigitalPresent", cell_r)],
    [Paragraph("Off-the-shelf campaign platform (for reference)", cell), Paragraph("$149&ndash;$699 or ~$29/mo", cell), Paragraph("Online Candidate", cell_r)],
]
ctbl = Table(ctx_rows, colWidths=[3.3 * inch, 2.05 * inch, 1.4 * inch], repeatRows=1)
cts = [
    ("BACKGROUND", (0, 0), (-1, 0), NAVY),
    ("TOPPADDING", (0, 0), (-1, -1), 5),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ("LEFTPADDING", (0, 0), (-1, -1), 7),
    ("RIGHTPADDING", (0, 0), (-1, -1), 7),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LINEBELOW", (0, 1), (-1, -1), 0.5, LIGHT),
    ("BACKGROUND", (0, 1), (-1, 1), CREAM),
]
ctbl.setStyle(TableStyle(cts))
ctx.append(ctbl)
ctx.append(Spacer(1, 6))
ctx.append(Paragraph(
    "Rate basis: U.S. Bureau of Labor Statistics median web-developer wage $90,930/yr (~$43.72/hr, May 2024); "
    "Arkansas employed web developers ~$39&ndash;$45/hr, designers ~$28&ndash;$29/hr (Salary.com, ERI, ZipRecruiter), "
    "uplifted to a ~$65&ndash;$90/hr freelance billing rate to cover self-employment overhead. Build effort of ~55&ndash;85 "
    "hours per small-custom-site estimates (spdload, 12AM Agency).",
    small_i))
E.append(KeepTogether(ctx))
E.append(Spacer(1, 12))

# ---------------- Notes / payment ----------------
E.append(HRFlowable(width="100%", thickness=0.75, color=LIGHT))
E.append(Spacer(1, 8))
E.append(Paragraph("Notes", sec))
E.append(Paragraph(
    "&bull;&nbsp; Static site &mdash; no CMS, database, or logins; the right architecture for a campaign "
    "(fast, secure, free hosting). Priced accordingly, below WordPress/Webflow custom builds.", small))
E.append(Paragraph(
    "&bull;&nbsp; The premium over an off-the-shelf platform reflects original code, a custom design system, and "
    "polished, fact-checked, compliant copy &mdash; not template licensing.", small))
E.append(Paragraph(
    "&bull;&nbsp; Attorney review of campaign-finance and SMS-compliance language is recommended and not included.", small))
E.append(Spacer(1, 6))
E.append(Paragraph(
    "Figures other than BLS wage data and vendor-published platform prices are corroborated market estimates, "
    "not formal quotes. This document is an illustrative cost estimate.", small_i))

doc.build(E)
print("Wrote", OUT)
