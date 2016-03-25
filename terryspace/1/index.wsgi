import sae
from terryspace import wsgi

application = sae.create_wsgi_app(wsgi.application)



