from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def highlight(request):
    return render(request, 'advanced-highlight.html')


def rating(request):
    return render(request, 'advanced-rating.html')


def lertify(request):
    return render(request, 'advanced-alertify.html')


def rangeslider(request):
    return render(request, 'advanced-rangeslider.html')


def calendar(request):
    return render(request, 'calendar.html')


def buttons(request):
    return render(request, 'ui-buttons.html')


def cards(request):
    return render(request, 'ui-cards.html')


def tabs_accordions(request):
    return render(request, 'ui-tabs-accordions.html')


def images(request):
    return render(request, 'ui-images.html')


def alerts(request):
    return render(request, 'ui-alerts.html')


def progressbars(request):
    return render(request, 'ui-progressbars.html')


def dropdowns(request):
    return render(request, 'ui-dropdowns.html')


def lightbox(request):
    return render(request, 'ui-lightbox.html')


def pagination(request):
    return render(request, 'ui-pagination.html')


def navs(request):
    return render(request, 'ui-navs.html')


def popover_tooltips(request):
    return render(request, 'ui-popover-tooltips.html')


def badge(request):
    return render(request, 'ui-badge.html')


def carousel(request):
    return render(request, 'ui-carousel.html')


def typography(request):
    return render(request, 'ui-typography.html')


def video(request):
    return render(request, 'ui-video.html')


def sweet_alert(request):
    return render(request, 'ui-sweet-alert.html')


def grid(request):
    return render(request, 'ui-grid.html')


def elements(request):
    return render(request,'form-elements.html')


def validation(request):
    return render(request,'form-validation.html')


def advanced(request):
    return render(request,'form-advanced.html')


def editors(request):
    return render(request,'form-editors.html')


def uploads(request):
    return render(request,'form-uploads.html')


def mask(request):
    return render(request,'form-mask.html')


def summernote(request):
    return render(request,'form-summernote.html')


def xeditable(request):
    return render(request,'form-xeditable.html')


def morris(request):
    return render(request,'charts-morris.html')


def chartist(request):
    return render(request,'charts-chartist.html')


def chartjs(request):
    return render(request,'charts-chartjs.html')


def flot(request):
    return render(request,'charts-flot.html')


def c3(request):
    return render(request,'charts-c3.html')


def other(request):
    return render(request,'charts-other.html')


def material(request):
    return render(request,'icons-material.html')


def ion(request):
    return render(request,'icons-ion.html')


def fontawesome(request):
    return render(request,'icons-fontawesome.html')


def themify(request):
    return render(request,'icons-themify.html')


def dripicons(request):
    return render(request,'icons-dripicons.html')


def typicons(request):
    return render(request,'icons-typicons.html')


def basic(request):
    return render(request,'tables-basic.html')


def datatable(request):
    return render(request,'tables-datatable.html')


def responsive(request):
    return render(request,'tables-responsive.html')


def editable(request):
    return render(request,'tables-editable.html')


def google(request):
    return render(request,'maps-google.html')


def vector(request):
    return render(request,'maps-vector.html')


def login(request):
    return render(request,'pages-login.html')


def register(request):
    return render(request,'pages-register.html')


def recoverpw(request):
    return render(request,'pages-recoverpw.html')


def lock_screen(request):
    return render(request,'pages-lock-screen.html')


def pages_404(request):
    return render(request,'pages-404.html')


def pages_500(request):
    return render(request,'pages-500.html')