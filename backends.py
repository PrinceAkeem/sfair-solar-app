from registration.backends.simple.views import RegistrationView

# new reg view, subclassing RegistrationView from the plugin
class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user=None): 
        # the named URL we want to redirect to after
        # successful Registration
        return ('registration_create_my_solar')
