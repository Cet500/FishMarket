from django.shortcuts import render


def index( request ):
	return render( request, 'core/index.html' )


def about( request ):
	return render( request, 'core/about.html' )


def cart( request ):
	return render( request, 'core/cart.html' )


def events( request ):
	return render( request, 'core/events.html' )


def fish( request ):
	return render( request, 'core/fish.html' )


def loyalty( request ):
	return render( request, 'core/loyalty.html' )


def shop( request ):
	return render( request, 'core/shop.html' )
