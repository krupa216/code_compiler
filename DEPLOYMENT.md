# Deployment Guide

## Quick Deploy on Render

### Step 1: Prepare Your Repository

1. Fork or clone this repository to your GitHub account
2. Make sure all files are committed and pushed

### Step 2: Create Render Account

1. Go to [render.com](https://render.com)
2. Sign up with GitHub (recommended for easy integration)
3. Authorize Render to access your GitHub repositories

### Step 3: Deploy to Render

1. Click "New +" button in Render dashboard
2. Select "Web Service"
3. Connect your GitHub repository
4. Fill in the configuration:
   - **Name:** `code-compiler` (any name you prefer)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** Free (or Starter for better performance)

### Step 4: Configure Environment (Optional)

No specific environment variables needed for basic setup.

Optional environment variables you can add:
- `FLASK_ENV`: Set to `production` (already handled)
- `PORT`: Auto-configured by Render (default 5000)

### Step 5: Deploy

1. Click "Create Web Service"
2. Wait for the build to complete (2-5 minutes)
3. Once deployed, you'll get a URL like: `https://code-compiler-xxxx.onrender.com`
4. Access your app at that URL

## Deployment on Other Platforms

### Heroku (Deprecated - Free tier closed)

Previously supported, but Heroku no longer offers free tier.

### Railway

1. Go to [railway.app](https://railway.app)
2. Connect GitHub repository
3. Railway auto-detects Python and deploys

### PythonAnywhere

1. Sign up at [pythonanywhere.com](https://pythonanywhere.com)
2. Upload files via web interface
3. Configure web app settings
4. Flask app URL provided automatically

### AWS Elastic Beanstalk

```bash
# Install AWS CLI
pip install awsebcli

# Initialize
eb init -p python-3.11 code-compiler
eb create code-compiler-env
eb deploy
```

### DigitalOcean App Platform

1. Create DigitalOcean account
2. Create new App
3. Connect GitHub repository
4. Auto-detects Python/Flask
5. Configure and deploy

### Docker + Any Cloud

Create a Dockerfile:

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 5000
CMD ["gunicorn", "app:app"]
```

Build and deploy:
```bash
docker build -t code-compiler .
docker run -p 5000:5000 code-compiler
```

## Post-Deployment

### Verify Deployment

1. Visit your app URL in browser
2. Try running sample code in each language
3. Check execution times and output

### Monitor Performance

- **Render Dashboard:** View logs and metrics
- **Error Tracking:** Check error logs for issues
- **Usage:** Monitor free tier usage limits

### Custom Domain (Optional)

On Render:
1. Go to Service Settings
2. Add Custom Domain
3. Update DNS records with provider
4. Wait 24-48 hours for propagation

## Troubleshooting Deployment

### Build Fails

**Issue:** Python version mismatch
**Solution:** Update `render.yaml` with compatible Python version

```yaml
pythonVersion: 3.11
```

### App Crashes After Deploy

**Issue:** Missing dependencies
**Solution:** Ensure all dependencies in `requirements.txt`:
```bash
pip freeze > requirements.txt
```

### Slow Response Time

**Issue:** Free tier resource limits
**Solution:** Upgrade to Starter tier for better performance

### Code Execution Fails

**Issue:** Language compiler not installed
**Solution:** Render free tier may not have C++/C compilers

Add to Procfile or build script:
```bash
# Install compilers (may exceed free tier limits)
apt-get update && apt-get install -y build-essential
```

### Memory Issues

**Issue:** Server runs out of memory
**Solution:** 
- Clear temporary files more frequently
- Set smaller output limits
- Upgrade instance

## Environment Variables Reference

```bash
# Flask Configuration
FLASK_ENV=production
FLASK_DEBUG=False

# Server Configuration
PORT=5000
WORKERS=2

# Security
MAX_CONTENT_LENGTH=1048576  # 1MB
TIMEOUT=10

# Logging
LOG_LEVEL=INFO
```

## Scaling Tips

For production use:

1. **Upgrade Plan:** Free tier has limitations
2. **Add CDN:** For static assets
3. **Database:** Add PostgreSQL for data persistence
4. **Monitoring:** Set up error tracking (Sentry)
5. **Load Balancing:** For high traffic

## Cost Estimates

### Render (Recommended)
- **Free:** ~$0/month (shared CPU, 512MB RAM)
- **Starter:** ~$7/month (dedicated CPU)
- **Standard:** ~$12/month (more resources)

### Railway
- **Pay as you go:** ~$5/month usage
- Excellent free tier for learning

### DigitalOcean
- **Droplet:** $4-6/month (basic)
- **App Platform:** Variable pricing

### AWS
- **EC2:** $5-10/month (free tier available)
- **Elastic Beanstalk:** Varies

## Maintenance

### Regular Updates

```bash
# Check for updates
pip list --outdated

# Update dependencies
pip install -r requirements.txt --upgrade
pip freeze > requirements.txt

# Commit and push
git add requirements.txt
git commit -m "Update dependencies"
git push
```

### Monitoring

Set up monitoring alerts for:
- High CPU usage
- Memory issues
- Error rates
- Response times

### Backups

If adding database features:
- Set up automated backups
- Test restore procedures
- Monitor backup storage

---

**Need help?** Check the main README.md or create a GitHub issue!
