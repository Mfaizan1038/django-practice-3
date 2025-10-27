import datetime

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        user = request.user if request.user.is_authenticated else "Anonymous"
        method = request.method
        path = request.path

        
        print(f"[{datetime.datetime.now()}] {user} made a {method} request to {path}")

        
        response = self.get_response(request)

        
        print(f"[{datetime.datetime.now()}] Response status: {response.status_code}")
        return response
