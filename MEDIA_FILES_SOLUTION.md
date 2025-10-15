# Media Files Solution for Render Deployment

## The Problem

When you upload images on Render, they don't persist because:
1. Render uses **ephemeral storage** - files are lost when the service restarts
2. Each deployment creates a new container, wiping uploaded files
3. Media files in the `media/` folder are temporary

## Current Quick Fix (Temporary Solution)

✅ **What I've implemented:**
- Media files are now served in production (not just DEBUG mode)
- Images will display correctly after upload
- **WARNING**: Files will be lost on service restart or redeploy

This works for:
- Development and testing
- Low-stakes applications
- Temporary demos

## Permanent Solution: Cloudinary (Recommended)

For production apps, use **Cloudinary** - a free cloud storage service for images.

### Step 1: Create Cloudinary Account

1. Go to https://cloudinary.com/users/register_free
2. Sign up for a free account (25 GB storage, 25 GB bandwidth/month)
3. After signup, go to Dashboard
4. Copy these values:
   - Cloud Name
   - API Key
   - API Secret

### Step 2: Install Cloudinary

Add to `requirements.txt`:
```
cloudinary==1.41.0
django-cloudinary-storage==0.3.0
```

### Step 3: Update Django Settings

Add to `settings.py` (after INSTALLED_APPS):

```python
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Cloudinary Configuration
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

# Update INSTALLED_APPS to include cloudinary
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',  # Add this BEFORE 'cloudinary'
    'cloudinary',          # Add this
    'courses',
]

# Change the default storage backend
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

### Step 4: Add Environment Variables in Render

In your Render dashboard → Environment:
```
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

### Step 5: Deploy

Push changes to GitHub:
```bash
git add requirements.txt registro_cursos/settings.py
git commit -m "Add Cloudinary for persistent media storage"
git push origin main
```

Render will automatically redeploy.

### Benefits of Cloudinary

✅ Images persist forever (no data loss)
✅ Automatic image optimization
✅ CDN delivery (fast worldwide)
✅ Free tier is generous (25 GB)
✅ Automatic backups
✅ Image transformations (resize, crop, etc.)

## Alternative: AWS S3

If you prefer AWS:

1. Install: `pip install django-storages boto3`
2. Configure S3 bucket
3. Update settings with S3 credentials

See: https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html

## Testing the Current Fix

Your images should now display after upload, but remember:
- They'll be lost on redeploy
- They'll be lost on service restart
- Not suitable for production with real users

## Recommended Next Steps

1. ✅ Test current fix to verify images display
2. 📦 If satisfied temporarily, you're done
3. 🌟 For production, implement Cloudinary (takes 10 minutes)

## Quick Cloudinary Setup Script

```bash
# 1. Update requirements.txt
echo "cloudinary==1.41.0" >> requirements.txt
echo "django-cloudinary-storage==0.3.0" >> requirements.txt

# 2. Commit and push
git add requirements.txt
git commit -m "Add Cloudinary dependencies"
git push origin main

# 3. Add environment variables in Render dashboard manually
```

Then update settings.py with the Cloudinary configuration shown above.
