from django.urls import path
from . import views as v


app_name = "core"
urlpatterns = [
	path( '',        v.index,   name = 'index' ),
	path( 'about',   v.about,   name = 'about' ),
	path( 'cart',    v.cart,    name = 'cart' ),
	path( 'events',  v.events,  name = 'events' ),
	path( 'fish',    v.fish,    name = 'fish' ),
	path( 'loyalty', v.loyalty, name = 'loyalty' ),
	path( 'shop',    v.shop,    name = 'shop' ),
]
