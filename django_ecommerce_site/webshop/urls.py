from django.urls import path
from .controllers import misc_controller as misc
from .controllers import panel_controller as panel
from .controllers import user_controller as user


urlpatterns = [
    path('', misc.home, name='webshop-home'),

    # Panel
    path('panel/<str:category>', panel.overview, name='webshop-panel-overview'),
    path('panel/<str:category>/delete/<int:id>', panel.delete, name='webshop-panel-delete'),
    path('panel/<str:category>/edit/<int:id>', panel.edit, name="webshop-panel-edit"),

    path('login/', user.login, name="webshop-user-login"),
    path('signup/', user.signup, name="webshop-user-signup"),

    # path('product/<int:product_id>', misc.product, name='webshop-product'),

    # Panel
    # path('panel/', panel.main, name='webshop-panel-main'),
    # path('panel/<string:type>', panel.overview, name='webshop-panel-overview'),

        # Overview
    # path('panel/users', panel.overview, name='webshop-panel-users'),
    # path('panel/products', panel.overview, name='webshop-panel-products'),




    #     # Delete
    # path('panel/overview?type=users&id=<int:user_id>', panel.delete_user, name='webshop-panel-users-delete'),
    # path('panel/overview?type=product&id=<int:product_id>', panel.delete_product, name='webshop-panel-products-delete'),
    #     # Add
    # path('panel/users/<int:user_id>/add', panel.add_user, name='webshop-panel-users-add'),
    # path('panel/products/<int:product_id>/add', panel.add_product, name='webshop-panel-products-add'),
    #     # Edit
    # path('panel/users/<int:user_id>/edit', panel.edit_user, name='webshop-panel-users-edit'),
    # path('panel/products/<int:product_id>/edit', panel.edit_product, name='webshop-panel-products-edit'),
     
    # # Users
    # path('account/', user.account, name='webshop-account'),
    # path('logout/', user.logout, name='webshop-logout'),
    #     # Login
    # path('login/', user.login, name='webshop-login'),
    # path('api/login/', user.api_login, name='webshop-api-login'),
    #     # Register
    # path('register/', user.register, name='webshop-register'),
    # path('api/register/', user.api_register, name='webshop-api-register')
    
]
