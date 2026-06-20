# MAX BOT - Replit + UptimeRobot Setup Guide

## Step 1: Create Replit Account
1. Go to: https://replit.com
2. Sign up with Google (easiest)
3. Verify your email

## Step 2: Create New Repl
1. Click "Create Repl"
2. Language: Python
3. Template: Empty
4. Name: maxbot
5. Click "Create Repl"

## Step 3: Upload Code
### Option A: From GitHub (Recommended)
1. In Replit, click "Version Control" (git icon)
2. Click "Connect to GitHub"
3. Select repository: maxbot-koyeb
4. Click "Clone"

### Option B: Manual Upload
1. Copy all files from your PC to Replit
2. Use the upload button or drag & drop

## Step 4: Add Environment Variables
1. Click "Secrets" (lock icon on left sidebar)
2. Add each variable:
   - DISCORD_TOKEN = your_bot_token
   - DISCORD_CLIENT_SECRET = your_client_secret
   - FLASK_SECRET_KEY = random_string
   - HONEYPOT_SECRET = random_string
   - CAPTCHA_SECRET = random_string
   - PYTHONUNBUFFERED = 1
   - PORT = 5001

## Step 5: Run the Bot
1. Click "Run" button (green triangle)
2. Wait 30-60 seconds
3. Bot will connect to Discord

## Step 6: Get Replit URL
1. Click "Web" tab on left sidebar
2. You'll see a URL like: https://maxbot-username.repl.co
3. Copy this URL

## Step 7: Setup UptimeRobot
1. Go to: https://uptimerobot.com
2. Sign up (free)
3. Click "Add New Monitor"
4. Settings:
   - Monitor Type: HTTP(s)
   - Friendly Name: MAX BOT
   - URL: https://maxbot-username.repl.co
   - Monitoring Interval: 5 minutes
5. Click "Create Monitor"

## Step 8: Done!
- UptimeRobot will ping your Replit every 5 minutes
- Your bot will stay alive 24/7
- Dashboard is accessible at your Replit URL

## Troubleshooting
- If bot stops: Check Replit Console for errors
- If Replit sleeps: UptimeRobot will wake it up
- If RAM exceeded: Upgrade to Replit Core ($20/month) or optimize

## Cost: $0 forever!
