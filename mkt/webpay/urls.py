from django.conf.urls import include, patterns, url

from tastypie.api import Api

from mkt.webpay.resources import (FailureNotificationResource,
                                  PreparePayResource, PriceResource,
                                  ProductIconResource, StatusPayResource)

api = Api(api_name='webpay')
api.register(FailureNotificationResource())
api.register(PriceResource())
api.register(ProductIconResource())
api.register(PreparePayResource())
api.register(StatusPayResource())

urlpatterns = patterns('',
    url(r'^', include(api.urls)),
)
