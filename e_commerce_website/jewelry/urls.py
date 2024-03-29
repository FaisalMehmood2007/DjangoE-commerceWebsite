from django.urls import include, path

from e_commerce_website.jewelry.views import display_jewelries, show_jewelry_details

urlpatterns = (
    path("<int:customer_gender_id>/<int:category_id>/", display_jewelries, name="show_jewelries"),
    path("<int:jewelry_id>/", show_jewelry_details, name='show_jewelry_details')
)
