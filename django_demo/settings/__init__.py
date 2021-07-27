from .default import env

if env.str('ENV_TYPE') == 'STAGING':
    from .staging import *
elif env.str('ENV_TYPE') == 'PRODUCTION':
    from .production import *
else:
    from .development import *
