from django.template.defaultfilters import register


@register.filter(name='lookup')
def lookup(target_dict, index):
    if index in target_dict:
        return target_dict[index]
    return ''
