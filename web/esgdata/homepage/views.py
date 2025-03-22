from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import Entity
import os
import json
from django.http import JsonResponse
from .models import ESGStandard,Attributes,SelectedMateriality



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

    # Get all attributes that exist in SelectedMateriality
    existing_material_names = SelectedMateriality.objects.values_list("material_name", flat=True)

    # Filter attributes based on scope & category
    attributes = Attributes.objects.filter(attribute_name__in=existing_material_names)
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
    

def get_selected_materiality(request):
    selected_indicators = list(SelectedMateriality.objects.values_list('linked_indicator_name', flat=True))
    selected_attributes = list(SelectedMateriality.objects.values_list('material_name', flat=True))
    
    return JsonResponse({"selected_indicators": selected_indicators, "selected_attributes": selected_attributes})

@csrf_exempt
def submit_materiality_selection(request):
    if request.method == "POST":
        data = json.loads(request.body)
        selections = data.get("selections", {})  # Now handling the correct structure

        print("Received selections:", selections)

        # Extract selected indicators and attributes from the nested dictionary
        new_set = set((indicator, attr) for indicator, attributes in selections.items() for attr in attributes)
        print("New set to be processed:", new_set)

        # Fetch existing selections from the database
        existing_selections = set(
            SelectedMateriality.objects.values_list("linked_indicator_name", "material_name")
        )
        print("Existing selections in DB:", existing_selections)

        # Insert only new pairs (avoid duplicates)
        to_insert = new_set - existing_selections
        print("To insert:", to_insert)
        SelectedMateriality.objects.bulk_create([
            SelectedMateriality(linked_indicator_name=indicator, material_name=attribute)
            for indicator, attribute in to_insert
        ])

        # Delete only pairs that are no longer selected
        to_delete = existing_selections - new_set
        print("To delete:", to_delete)
        for indicator, attribute in to_delete:
            SelectedMateriality.objects.filter(
                linked_indicator_name=indicator, material_name=attribute
            ).delete()

        return JsonResponse({"message": "Selection updated successfully!"})


@csrf_exempt
def add_custom_material(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            indicator = data.get("indicator", "").strip()
            attribute = data.get("attribute", "").strip()
            measuring_unit = data.get("measuring_unit", "").strip()
            category = data.get("category").strip()
            gwp = data.get("gwp",0)
            print(category)
            if not indicator or not attribute:
                return JsonResponse({"error": "Both indicator and attribute are required."}, status=400)

            # Check if the entry already exists
            if not Attributes.objects.filter(linked_indicator_name=indicator,attribute_name=attribute).exists():
                Attributes.objects.create(linked_indicator_name=indicator, attribute_name=attribute,measuring_unit=measuring_unit,category=category,GWP_factor=gwp)
                SelectedMateriality.objects.create(linked_indicator_name=indicator, material_name=attribute)
                return JsonResponse({"message": "Custom material added successfully!", "indicator": indicator, "attribute": attribute})
            else:
                return JsonResponse({"message": "Material already exists."}, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)