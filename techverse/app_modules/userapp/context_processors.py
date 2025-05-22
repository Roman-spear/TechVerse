from app_modules.adminapp import models

def global_data(request):
    servicecategory = models.ServiceCategory.objects.all()
    industrycategory = models.IndustryCategory.objects.all()
    aicategory = models.AICategory.objects.all()
    context = {
        'servicecategory':servicecategory,
        'industrycategory':industrycategory,
        'aicategory':aicategory,
    }
    return context 