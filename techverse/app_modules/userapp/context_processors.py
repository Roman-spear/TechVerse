from app_modules.adminapp import models

def global_data(request):
    servicecategory = models.ServiceDetail.objects.all()
    industrycategory = models.IndustryCategory.objects.all()
    aicategory = models.AICategory.objects.all()
    meta_name_view = request.resolver_match.view_name
    canonical = request.build_absolute_uri()
    metaname = models.MetaName.objects.filter(view_name=meta_name_view)
    metaproperty = models.MetaProperty.objects.filter(view_name=meta_name_view)
    if any(x in meta_name_view for x in ["blog_detail", "service_detail", "industry_detail", "ai_detail"]):
        detail_identifier = request.resolver_match.kwargs.get('slug')
        if detail_identifier:
            metaname = metaname.filter(detail_name=detail_identifier)
            metaproperty = metaproperty.filter(detail_name=detail_identifier) 
    print(f' ==> [Line 18]: \033[38;2;32;184;172m[metaname]\033[0m({type(metaname).__name__}) = \033[38;2;78;26;41m{metaname}\033[0m')
    print(f' ==> [Line 19]: \033[38;2;156;72;38m[metaproperty]\033[0m({type(metaproperty).__name__}) = \033[38;2;142;222;40m{metaproperty}\033[0m')
    print(f' ==> [Line 9]: \033[38;2;189;154;221m[canonical]\033[0m({type(canonical).__name__}) = \033[38;2;160;8;231m{canonical}\033[0m')
    
    context = {
        'servicecategory':servicecategory,
        'industrycategory':industrycategory,
        'aicategory':aicategory,
        'meta_name':metaname,
        'meta_property':metaproperty,
        'canonical':canonical,
    }
    return context 