from router.router import Router
from controller.primeira_rota import PrimeiraRota

Router.add_route('/primeira-rota', PrimeiraRota.index)
