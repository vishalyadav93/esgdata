from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import Entity
import os
from django.http import JsonResponse
from .models import ESGStandard,Attributes


@csrf_exempt
def home(request):
    environment_data = Entity.objects.filter(name='Environment')
    social_data = Entity.objects.filter(name='Social')
    governance_data = Entity.objects.filter(name='Governance')
    
    return render(request,'main.html',{
        'environment_data': environment_data,
        'social_data': social_data,
        'governance_data': governance_data,
       'templates': show_templates()
    }
        )


def filter_attributes(request):
    scope_filter = request.GET.get('scope', '')
    category_filter = request.GET.get('category', '')

    attributes = Attributes.objects.all()
    if scope_filter:
        attributes = attributes.filter(scope=scope_filter)
    if category_filter:
        attributes = attributes.filter(category=category_filter)

    # Convert queryset to a list of dictionaries
    attributes_data = [
        {
            "attribute_name": attr.attribute_name,
            "measuring_unit": attr.measuring_unit,
            "GWP_factor": attr.GWP_factor,
            "scope": attr.scope,
            "category": attr.category,
        }
        for attr in attributes
    ]

    return JsonResponse({'attributes': attributes_data})


def get_scopes_categories(request):
    scopes = list(Attributes.objects.values_list('scope', flat=True).distinct())
    categories = list(Attributes.objects.values_list('category', flat=True).distinct())

    return JsonResponse({'scopes': scopes, 'categories': categories})



def show_templates():
    # Define the directory where the images and Excel templates are stored
    currdirec = os.getcwd()

    image_dir = os.path.join('homepage','static', 'images')
    excel_dir = os.path.join('homepage','job', 'excel_templates')

    # List all files in the image directory
    image_files = [f for f in os.listdir(image_dir) if f.endswith(('.bmp', '.png', '.jpg'))]
    templates = []

    for image_file in image_files:
        # Assuming the Excel file has the same name as the image
        excel_file = f"{os.path.splitext(image_file)[0]}.xlsx"
        image_path = os.path.join(image_dir, image_file)
        excel_path = os.path.join(excel_dir, excel_file)
        image_path = image_path.replace("\\", "/")
        excel_path = excel_path.replace("\\", "/")

        templates.append({
            'image_path': image_path,
            'excel_path': excel_path
        })

    return templates


from .models import ESGStandard

# Fetch unique values for dropdowns
def get_dropdown_values(request):
    iso_standards = ESGStandard.objects.values_list('iso_standard', flat=True).distinct()
    release_dates = ESGStandard.objects.values_list('release_date', flat=True).distinct()
    sectors = ESGStandard.objects.values_list('sector', flat=True).distinct()
    esg_components = ESGStandard.objects.values_list('esg_component', flat=True).distinct()

    data = {
        "iso_standards": [{"value": value, "label": value} for value in iso_standards],
        "release_dates": [{"value": value, "label": value} for value in release_dates],
        "sectors": [{"value": value, "label": value} for value in sectors],
        "esg_components": [{"value": value, "label": value} for value in esg_components],
    }

    return JsonResponse(data)


# Fetch filtered data for the table
def filter_standards(request):
    iso_standard = request.GET.get('iso_standard', '')
    release_date = request.GET.get('release_date', '')
    sector = request.GET.get('sector', '')
    esg_component = request.GET.get('esg_component', '')

    queryset = ESGStandard.objects.all()

    if iso_standard:
        queryset = queryset.filter(iso_standard=iso_standard)
    if release_date:
        queryset = queryset.filter(release_date=release_date)
    if sector:
        queryset = queryset.filter(sector=sector)
    if esg_component:
        queryset = queryset.filter(esg_component=esg_component)

    data = [
        {
            "iso_standard": item.iso_standard,
            "release_date": item.release_date,
            "sector": item.sector,
            "esg_component": item.esg_component,
        }
        for item in queryset
    ]

    return JsonResponse(data, safe=False)



def get_materiality_assessment_data(request):
    indicators = Attributes.objects.values("linked_indicator_name", "attribute_name")
    # Group attributes under each indicator
    grouped_data = {}
    for item in indicators:
        indicator = item["linked_indicator_name"]
        attribute = item["attribute_name"]
        
        if indicator not in grouped_data:
            grouped_data[indicator] = []
        
        grouped_data[indicator].append(attribute)
    
    return JsonResponse({"data": grouped_data})

