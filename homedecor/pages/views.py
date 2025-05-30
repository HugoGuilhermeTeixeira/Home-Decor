from django.views.generic import TemplateView

class PrivacyPolicyView(TemplateView):
    template_name = "pages/privacy_policy.html"

class TermsOfUseView(TemplateView):
    template_name = "pages/terms_of_use.html"
