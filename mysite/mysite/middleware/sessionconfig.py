def sessionconfig(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        request.session["dj4e"] = "f331c4fb"

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware