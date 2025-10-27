from django.http import HttpResponse

class BlockIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
        self.blocked_ips = ['127.0.0.2', '192.168.1.10']

    def __call__(self, request):
        
        ip = request.META.get('REMOTE_ADDR')

        
        if ip in self.blocked_ips:
            return HttpResponse(" Access Denied: Your IP is blocked.", status=403)

        
        response = self.get_response(request)
        return response
