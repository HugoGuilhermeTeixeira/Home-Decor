from django.urls import path
from .views import PrivacyPolicyView, TermsOfUseView

app_name = 'pages'
urlpatterns = [
    path('privacy-policy/', PrivacyPolicyView.as_view(), name='privacy_policy'),
    path('terms-of-use/', TermsOfUseView.as_view(), name='terms_of_use'),
]
