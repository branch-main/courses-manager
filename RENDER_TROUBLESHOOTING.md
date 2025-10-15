# Render Deployment Troubleshooting

## Common Issues and Solutions

### 1. STATIC_ROOT Error (FIXED!)
**Error:** `ImproperlyConfigured: You're using the staticfiles app without having set the STATIC_ROOT setting`

**Solution:** ✅ Already fixed in the latest commit!
- Added `STATIC_ROOT = BASE_DIR / 'staticfiles'` to settings.py

### 2. Build Command Issues
**Problem:** Render doesn't find the build script

**Solutions:**
- Ensure build.sh is executable: `chmod +x build.sh`
- Use Build Command: `./build.sh`
- Alternative: `pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate`

### 3. Start Command Issues
**Problem:** Application won't start

**Solutions:**
- Make sure gunicorn is in requirements.txt ✅ (already added)
- Use Start Command: `gunicorn registro_cursos.wsgi:application`
- Check that WSGI_APPLICATION setting is correct in settings.py

### 4. Missing Environment Variables
**Problem:** Application crashes or shows errors about SECRET_KEY

**Solution:** Add environment variables in Render dashboard:
```
SECRET_KEY=<your-generated-secret-key>
DEBUG=False
PYTHON_VERSION=3.9.0
```

Generate SECRET_KEY:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### 5. Static Files Not Loading
**Problem:** CSS/JS files return 404

**Solutions:**
- ✅ WhiteNoise is already configured
- Ensure `collectstatic` runs during build (it does in build.sh)
- Check that WhiteNoise middleware is in MIDDLEWARE (it is)

### 6. Database Connection Issues
**Problem:** Database errors in production

**Solutions:**
- For SQLite: Works on Render (unlike Vercel)
- For PostgreSQL: 
  - Create a PostgreSQL database in Render
  - Copy the "Internal Database URL"
  - Add as `DATABASE_URL` environment variable

### 7. Module Import Errors
**Problem:** `ModuleNotFoundError` for whitenoise, gunicorn, etc.

**Solution:** ✅ All dependencies are in requirements.txt:
- whitenoise==6.8.2
- gunicorn==21.2.0
- psycopg2-binary==2.9.10
- dj-database-url==2.3.0

### 8. Python Version Issues
**Problem:** Build uses wrong Python version

**Solution:** Add environment variable:
```
PYTHON_VERSION=3.9.0
```

### 9. Port Binding Issues
**Problem:** Application can't bind to port

**Solution:** Gunicorn automatically binds to the PORT environment variable that Render provides. No action needed.

### 10. ALLOWED_HOSTS Error
**Problem:** DisallowedHost error

**Solution:** ✅ Already fixed! Settings.py includes:
- `*.onrender.com`
- Automatic detection of `RENDER_EXTERNAL_HOSTNAME`

## Viewing Logs

1. Go to your Render dashboard
2. Click on your web service
3. Click "Logs" tab
4. Look for error messages

## Manual Deploy

If auto-deploy isn't working:
1. Go to Render dashboard
2. Click "Manual Deploy"
3. Select "Deploy latest commit"

## Testing Locally

Before deploying, test with production-like settings:

```bash
# Set environment variables
export SECRET_KEY='your-test-secret-key'
export DEBUG=False

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Test with gunicorn
gunicorn registro_cursos.wsgi:application
```

Then visit http://localhost:8000

## Still Having Issues?

Check the Render documentation:
- https://render.com/docs/deploy-django
- https://render.com/docs/troubleshooting-deploys

Or review the deployment logs carefully for specific error messages.
