from django.urls import path

from AppQatarWC2022.generic_modals.views import element_unregistration,element_registration,element_update

urlpatterns = [
    path("element_registration/<str:object_class_name>/<str:form_class_name>/", element_registration, name="element_registration"),
    path("element_unregistration/<int:id>/<str:object_class_name>/<str:form_class_name>/", element_unregistration, name="element_unregistration"),
    path("element_update/<int:id>/<str:object_class_name>/<str:form_class_name>/", element_update, name="element_update"),
]