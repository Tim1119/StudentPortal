response = HttpResponse(content_type= 'application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename = expenses'+str(request.user.username)+str(datetime.datetime.now())+'.xlsx'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Expenses')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold  = True
    columns= ['Description','Category','Amount','Expense_Date'] 
    
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)    
    
    font_style = xlwt.XFStyle()
    
    rows = Expense.objects.filter(owner=request.user).values_list('description','category','amount','expense_date')
    
    for row in rows:
        row_num+=1
    
        for col_num in range(len(rows)):
            ws.write(row_num,col_num,str(row[col_num]),font_style) 
    wb.save(response) 
    

 response = HttpResponse(content_type='text/pdf')
    response['Content-Disposition'] = 'attachment; filename=Expenses'+str(request.user.username)+str(datetime.datetime.now())+'.csv'
    
from reportlab.platypus import SimpleDocTemplate,Image,Paragraph
from reportlab.platypus.tables import Table,TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import inch
from reportlab.lib.styles import getSampleStyleSheet

@require_http_methods('GET')
def export_pdf(request,*args, **kwargs):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'
    elements = []
    cm = 2.54
    doc = SimpleDocTemplate(response, rightMargin=0, leftMargin=6.5 * cm, topMargin=0.3 * cm, bottomMargin=0)
    import os
    styleSheet = getSampleStyleSheet()
    I = Image(os.path.join(settings.BASE_DIR,'static/assets/img/logo1.svg'))
    I.drawHeight = 1.25*inch*I.drawHeight / I.drawWidth
    I.drawWidth = 1.25*inch
    P0 = Paragraph('''A paragraph1''',styleSheet["BodyText"])
    P = Paragraph(''' The ReportLab Left Logo Image''', styleSheet["BodyText"])
    
    # writing expense_data as a table to pdf
    title = ['Description','Category','Amount','Date']
    expenses = Expense.objects.filter(owner=request.user).order_by('-expense_date')
    data= [title,]
    for expense in expenses:
        data.append([str(expense.description).capitalize(),str(expense.category.name).capitalize(),expense.amount,expense.expense_date],)
    
    table = Table(data, colWidths=100, rowHeights=30)
    
    
    table.setStyle(TableStyle([('ALIGN',(1,1),(-2,-2),'LEFT'),
    #('TEXTCOLOR',(1,1),(-2,-2),colors.red),
    ('VALIGN',(0,0),(0,-1),'BOTTOM'),
    #('TEXTCOLOR',(0,0),(0,-1),colors.blue),
    ('ALIGN',(0,-1),(-1,-1),'LEFT'),
    ('VALIGN',(0,-1),(-1,-1),'BOTTOM'),
    #('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
    ('BOX', (0,0), (-1,-1), 0.25, colors.black),
    ]))
    elements.append(table)
    doc.build(elements)
    return response
    
    return response  






@require_http_methods('GET')
def export_pdf(request,*args, **kwargs):    
    template_path = 'pdf-output.html'
    expenses = Expense.objects.filter(owner=request.user)
    profile = Profile.objects.filter(owner=request.user)
    user_details = User.objects.get(email=request.user.email)
    context = {'expenses':expenses,'profile':profile,'user_details':user_details}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' filename=somefilename.pdf'
    elements = [] #Final list to append everything to for final display on pdf
    cm = 2.54
    doc = SimpleDocTemplate(response, rightMargin=0, leftMargin=6.5 * cm, topMargin=0.3 * cm, bottomMargin=0)
    styles = getSampleStyleSheet()
    
    #logo image on top of page
    logo_image = Image('static\\assets\\img\\logo.jpg',1.2*inch,1.2*inch)
    # logo default style
    logo_small_font = ParagraphStyle('logo_small_font',parent=styles['Normal'],fontSize=26,alignment=TA_JUSTIFY)
    logo_table = [[[logo_image],Paragraph("Student Portal",logo_small_font)]]    
    
    # final header table to be displayed on pdf
    HEADER_TABLE = Table(logo_table,colWidths=265, rowHeights=60)
    HEADER_TABLE.setStyle(
        TableStyle([
            ('BOX', (0,0), (-1,-1),1, colors.black),
             ('VALIGN',(0,0),(1,0),'CENTER'),          
        ]))
    
    # here you add your rows and columns, these can be platypus objects
    expenses_letterhead_font = ParagraphStyle('expenses_letterhead_font',parent=styles['Normal'],fontSize=16,alignment=TA_CENTER)
    expense_letterhead = Paragraph("Expenses incured by " + str(request.user.first_name).capitalize()+ ' '+ str(request.user.last_name).capitalize(),expenses_letterhead_font)
    
    
    #('ALIGN',(0,0),(1,0),'RIGHT')
    # writing expense_data as a table to pdf
    
    
    
    
    title = ['Description','Category','Amount','Date']
    expenses = Expense.objects.filter(owner=request.user).order_by('-expense_date')
    data= [title,]
    for expense in expenses:
        data.append([str(expense.description).capitalize(),str(expense.category.name).capitalize(),expense.amount,expense.expense_date],)
    
    
    table = Table(data, colWidths=130, rowHeights=20)
    
    
    table.setStyle(TableStyle([('ALIGN',(1,1),(-2,-2),'LEFT'),
    ('FONTSIZE',(0,0),(3,0),12),
    ('VALIGN',(0,1),(0,-1),'BOTTOM'),
    #('TEXTCOLOR',(0,0),(4,0),colors.blue),
    ('ALIGN',(0,-1),(-1,-1),'LEFT'),
    ('VALIGN',(0,-1),(-1,-1),'BOTTOM'),
    #('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
    ('BOX', (0,0), (-1,-1), 0.25, colors.black),
    
    ]))
    elements.append(HEADER_TABLE)
    elements.append(Spacer(200,220))
    elements.append(expense_letterhead)
    elements.append(Spacer(100,50))
    elements.append(BalancedColumns(data,nCols=4))
    doc.build(elements)
    return response
