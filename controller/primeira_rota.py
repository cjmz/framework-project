from controller import controller

class PrimeiraRota:
    @staticmethod
    def index(request):
        controller.render_view('primeira-rota.html')