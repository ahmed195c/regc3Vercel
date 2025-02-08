# ...existing code...

import os

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ...existing code...

# Ensure DEBUG is set to False in production
DEBUG = False

# Add your domain to ALLOWED_HOSTS
ALLOWED_HOSTS = ['your-vercel-domain.vercel.app', 'your-custom-domain.com']

# ...existing code...