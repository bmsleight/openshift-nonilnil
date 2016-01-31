from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(needs_autoescape=True)
def medal_icon(text, autoescape=True):
    if text == "Gold":
        return mark_safe("<i class='fa fa-star fa-2x' style='color:gold'></i>")
    if  text == "Silver":
        return mark_safe("<i class='fa fa-soccer-ball-o fa-1x' style='color:silver'></i>")
    if  text == "Bronze":
        return mark_safe("<i class='fa fa-soccer-ball-o fa-1x' style='color:#CD7F32'></i>")
    if  text == "Every":
        return mark_safe("<i class='fa fa-sort-alpha-as fa-1x' style='color:bronze'></i>")
    if  text == "90":
        return mark_safe("<i class='fa fa-hourglass-3 fa-1x' style='color:LightGreen'></i>")
    if  text == "TopGoal":
        return mark_safe("<i class='fa fa-chevron-circle-up fa-1x' style='color:LightGreen'></i>")
    if  text == "AFC":
        return mark_safe("<i class='fa fa-soccer-ball-o fa-1x fa-spin' style='color:blue; background-color:yellow'></i>")
    if  text == "Bomb":
        return mark_safe("<i class='fa fa-bomb fa-1x' style='color:MediumOrchid'></i>")
    if  text == "Warning":
        return mark_safe("<i class='fa fa-warning fa-1x' style='color:MediumOrchid'></i>")
    if  text == "Postpone":
        return mark_safe("<i class='fa fa-umbrella fa-1x' style='color:MediumOrchid'></i>")
    if  text == "Twitter":
        return mark_safe("<i class='fa fa-twitter fa-1x' style='color:blue'></i>")
    if  text == "Group":
        return mark_safe("<i class='fa fa-group fa-1x' style='color:blue'></i>")
    if  text == "Globe":
        return mark_safe("<i class='fa fa-globe fa-1x' style='color:blue'></i>")

    return mark_safe("")
