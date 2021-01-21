"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from App import views

urlpatterns = [
    path('', views.index, name='index'),
    path('advanced-highlight/', views.highlight, name='advanced-highlight'),
    path('advanced-rating/', views.rating, name='advanced-rating'),
    path('advanced-alertify/', views.lertify, name='advanced-alertify'),
    path('advanced-rangeslider/', views.rangeslider, name='advanced-rangeslider'),

    path('calendar/', views.calendar, name='calendar'),

    path('ui-buttons/', views.buttons, name='ui-buttons'),
    path('ui-cards/', views.cards, name='ui-cards'),
    path('ui-tabs-accordions/', views.tabs_accordions, name='ui-tabs-accordions'),
    path('ui-images/', views.images, name='ui-images'),
    path('ui-alerts/', views.alerts, name='ui-alerts'),
    path('ui-progressbars/', views.progressbars, name='ui-progressbars'),
    path('ui-dropdowns/', views.dropdowns, name='ui-dropdowns'),
    path('ui-lightbox/', views.lightbox, name='ui-lightbox'),
    path('ui-navs/', views.navs, name='ui-navs'),
    path('ui-pagination/', views.pagination, name='ui-pagination'),
    path('ui-popover-tooltips/', views.popover_tooltips, name='ui-popover-tooltips'),
    path('ui-badge/', views.badge, name='ui-badge'),
    path('ui-carousel/', views.carousel, name='ui-carousel'),
    path('ui-video/', views.video, name='ui-video'),
    path('ui-typography/', views.typography, name='ui-typography'),
    path('ui-sweet-alert/', views.sweet_alert, name='ui-sweet-alert'),
    path('ui-grid/', views.grid, name='ui-grid'),

    path('form-elements/', views.elements, name='form-elements'),
    path('form-validation/', views.validation, name='form-validation'),
    path('form-advanced/', views.advanced, name='form-advanced'),
    path('form-editors/', views.editors, name='form-editors'),
    path('form-uploads/', views.uploads, name='form-uploads'),
    path('form-mask/', views.mask, name='form-mask'),
    path('form-summernote/', views.summernote, name='form-summernote'),
    path('form-xeditable/', views.xeditable, name='form-xeditable'),

    path('charts-morris/', views.morris, name='charts-morris'),
    path('charts-chartist/', views.chartist, name='charts-chartist'),
    path('charts-chartjs/', views.chartjs, name='charts-chartjs'),
    path('charts-flot/', views.flot, name='charts-flot'),
    path('charts-c3/', views.c3, name='charts-c3'),
    path('charts-other/', views.other, name='charts-other'),

    path('icons-material/', views.material, name='icons-material'),
    path('icons-ion/', views.ion, name='icons-ion'),
    path('icons-fontawesome/', views.fontawesome, name='icons-fontawesome'),
    path('icons-themify/', views.themify, name='icons-themify'),
    path('icons-dripicons/', views.dripicons, name='icons-dripicons'),
    path('icons-typicons/', views.typicons, name='icons-typicons'),

    path('tables-basic/', views.basic, name='tables-basic'),
    path('tables-datatable/', views.datatable, name='tables-datatable'),
    path('tables-responsive/', views.responsive, name='tables-responsive'),
    path('tables-editable/', views.editable, name='tables-editable'),

    path('maps-google/', views.google, name='maps-google'),
    path('maps-vector/', views.vector, name='maps-vector'),

    path('pages-login/', views.login, name='pages-login'),
    path('pages-register/', views.register, name='pages-register'),
    path('pages-recoverpw/', views.recoverpw, name='pages-recoverpw'),
    path('pages-lock-screen/', views.lock_screen, name='pages-lock-screen'),
    path('pages-404/', views.pages_404, name='pages-404'),
    path('pages-500/', views.pages_500, name='pages-500'),

]
