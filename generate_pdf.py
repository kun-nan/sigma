import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def generate_pdf():
    pdf_path = "assets/sigma_30_day_tracker.pdf"
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    
    # Page setup - 0.5 inch margins (36 points)
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0F172A'),
        alignment=TA_CENTER
    )
    
    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=colors.HexColor('#E6B022'), # Gold/Yellow
        alignment=TA_CENTER,
        spaceAfter=12
    )
    
    motto_style = ParagraphStyle(
        'MottoStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=11,
        textColor=colors.HexColor('#64748B'),
        alignment=TA_CENTER,
        spaceBefore=8,
        spaceAfter=5
    )
    
    header_style = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=9,
        textColor=colors.white,
        alignment=TA_CENTER
    )
    
    cell_style = ParagraphStyle(
        'CellStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#1E293B'),
        alignment=TA_CENTER
    )
    
    day_style = ParagraphStyle(
        'DayStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#0F172A'),
        alignment=TA_CENTER
    )

    story = []
    
    # Header Section
    story.append(Paragraph("Σ SIGMA CHALLENGE", title_style))
    story.append(Paragraph("30-DAY DISCIPLINE PROTOCOL TRACKER", subtitle_style))
    
    # Table headers
    headers = [
        Paragraph("<b>Day</b>", header_style),
        Paragraph("<b>Workout<br/>(1 Hour)</b>", header_style),
        Paragraph("<b>Rest Day<br/>(Weekly)</b>", header_style),
        Paragraph("<b>3L Water<br/>Quota</b>", header_style),
        Paragraph("<b>No<br/>Cigarette</b>", header_style),
        Paragraph("<b>No<br/>Alcohol</b>", header_style),
        Paragraph("<b>Mental Tr.<br/>(10 Min)</b>", header_style),
        Paragraph("<b>Daily<br/>Log</b>", header_style)
    ]
    
    data = [headers]
    
    # Table rows
    for day in range(1, 31):
        row = [
            Paragraph(f"Day {day}", day_style),
            Paragraph("[  ]", cell_style),
            Paragraph("[  ]", cell_style),
            Paragraph("[  ]", cell_style),
            Paragraph("[  ]", cell_style),
            Paragraph("[  ]", cell_style),
            Paragraph("[  ]", cell_style),
            Paragraph("[  ]", cell_style)
        ]
        data.append(row)
        
    # Table sizing
    # Letter width is 612. Printable width is 612 - 72 = 540.
    # Col widths: Day (45), Workout (75), Rest Day (75), 3L Water (75), No Cig (65), No Alc (65), Mental (80), Log (60) = 540
    col_widths = [45, 75, 75, 75, 65, 65, 80, 60]
    
    table = Table(data, colWidths=col_widths, repeatRows=1)
    
    # Styling Table
    t_style = TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F172A')), # Dark Slate header
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('BOTTOMPADDING', (0,0), (-1,0), 4),
        ('TOPPADDING', (0,0), (-1,0), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ])
    
    # Alternating row colors
    for i in range(1, 31):
        bg_color = colors.HexColor('#F8FAFC') if i % 2 == 0 else colors.white
        t_style.add('BACKGROUND', (0, i), (-1, i), bg_color)
        t_style.add('BOTTOMPADDING', (0, i), (-1, i), 3)
        t_style.add('TOPPADDING', (0, i), (-1, i), 3)
        
    table.setStyle(t_style)
    story.append(table)
    
    # Footer Section
    story.append(Paragraph("RULES: MISS ONE RULE = RESTART DAY 1. NO NEGOTIATIONS.", ParagraphStyle(
        'WarningStyle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9, leading=11, textColor=colors.HexColor('#EF4444'), alignment=TA_CENTER, spaceBefore=10
    )))
    story.append(Paragraph("Σ 90 DAYS. NO EXCUSES. JUST RESULTS. YOU VS. YOU. WIN.", motto_style))
    
    doc.build(story)
    print(f"Successfully generated tracker PDF at {pdf_path}")

if __name__ == '__main__':
    generate_pdf()
