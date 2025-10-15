# CLOUDINARY SETUP - REQUIRED FOR IMAGES ON RENDER

## Why You Need This

Images don't show on Render because:
1. Render uses ephemeral storage (files disappear on restart)
2. Django's static file serving doesn't work for user uploads in production

**Solution: Cloudinary** - Free cloud storage that persists images permanently.

## Quick Setup (5 minutes)

### Step 1: Create Cloudinary Account

1. Go to: https://cloudinary.com/users/register_free
2. Sign up (use GitHub or Google for faster signup)
3. You'll be taken to the Dashboard

### Step 2: Get Your Credentials

On the Cloudinary Dashboard, you'll see:

```
Cloud name: your-cloud-name
API Key: 123456789012345
API Secret: AbCdEfGhIjKlMnOpQrStUvWx
```

**Copy these three values!**

### Step 3: Add Environment Variables in Render

1. Go to your Render Dashboard: https://dashboard.render.com
2. Click on your web service (django-prueba02 or whatever you named it)
3. Click **"Environment"** in the left sidebar
4. Click **"Add Environment Variable"**
5. Add these THREE variables:

```
Key: CLOUDINARY_CLOUD_NAME
Value: [paste your cloud name]

Key: CLOUDINARY_API_KEY
Value: [paste your API key]

Key: CLOUDINARY_API_SECRET
Value: [paste your API secret]
```

Click "Save Changes" after adding each one.

### Step 4: Deploy

The code is already configured! Just push to GitHub:

```bash
git add requirements.txt registro_cursos/settings.py
git commit -m "Add Cloudinary for media storage"
git push origin main
```

Or if already pushed, just click **"Manual Deploy"** in Render dashboard.

### Step 5: Test

1. Wait for deployment to complete (2-3 minutes)
2. Go to your site
3. Upload a new image to a course
4. The image should now display correctly!
5. **Bonus**: The image persists even after redeployment!

## Verification

After deployment, check the logs in Render. You should see:
```
Successfully installed cloudinary-1.41.0 django-cloudinary-storage-0.3.0
```

## What Changed?

✅ Added Cloudinary packages to requirements.txt
✅ Configured Django to use Cloudinary for media storage
✅ Images now stored in the cloud (not on Render's ephemeral disk)
✅ Automatic fallback to local storage if Cloudinary not configured

## Troubleshooting

### Images still not showing?

1. **Check environment variables are set correctly:**
   - Go to Render → Your Service → Environment
   - Verify all 3 Cloudinary variables are present
   - No typos in variable names

2. **Check deployment logs:**
   - Look for "Successfully installed cloudinary"
   - Look for any import errors

3. **Clear browser cache:**
   - Hard refresh: Ctrl+Shift+R (Windows/Linux) or Cmd+Shift+R (Mac)

4. **Upload a NEW image:**
   - Old images (before Cloudinary setup) won't work
   - Upload a fresh image after deployment completes

### Environment variable names MUST be exact:

```
CLOUDINARY_CLOUD_NAME  ← not "cloud_name" or "CLOUD_NAME"
CLOUDINARY_API_KEY     ← not "api_key" or "API_KEY"
CLOUDINARY_API_SECRET  ← not "api_secret" or "SECRET"
```

## Benefits

✅ **Persistent Storage**: Images never disappear
✅ **Fast CDN**: Images load quickly worldwide
✅ **Free Tier**: 25 GB storage + 25 GB bandwidth/month
✅ **Automatic Optimization**: Images compressed automatically
✅ **Secure**: HTTPS by default
✅ **Scalable**: Handles millions of images

## Cost

**FREE** for:
- 25 GB storage
- 25 GB bandwidth per month
- 25,000 transformations per month

This is more than enough for most small to medium apps!

## Local Development

Cloudinary works locally too! Just add a `.env` file:

```bash
# .env (don't commit this!)
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret
```

Or just develop without it - the app automatically uses local storage if Cloudinary isn't configured.

## Need Help?

If images still don't work after following these steps:
1. Check Render deployment logs
2. Verify all 3 environment variables are set
3. Try uploading a NEW image (old ones won't work)
4. Hard refresh your browser

Still stuck? Check:
- https://cloudinary.com/documentation/django_integration
- Your Render service logs for specific errors
