# Setup Instructions for FastAPI Render Project

1. Fork the Repository
   - Go to https://github.com/rohitk523/fastapi-render
   - Click the "Fork" button in the top right
   - This will create a copy in your GitHub account

2. Create .env file
   You only need one environment variable:
   API_KEY=your-chosen-api-key
   Note: Replace 'your-chosen-api-key' with any secure string you want to use as your API key

3. Set up on Render
- Log in to your Render account
- Click "New +"
- Select "Web Service"
- Click "Connect" under GitHub section
- Find and select your forked repository
- Configure the service:
  - Name: [any name you prefer]
  - Environment: Docker
  - Region: Oregon (or your preferred region)
  - Branch: main
  - Plan: Free

4. Add Environment Variable
- In Render dashboard, go to your service
- Click "Environment" tab
- Add:
  Key: API_KEY
  Value: [same value you chose for your .env file]
- Click "Save Changes"

5. Verify Deployment
- The service will automatically deploy
- Once deployed, test these endpoints:
  - `GET /` (public endpoint)
  - `GET /test2` (public endpoint)
  - `GET /items/{item_id}` (protected endpoint - requires API key)

6. Using the API
To test protected endpoints:
- Add header: `X-API-Key: your-chosen-api-key`
- Example curl:
  ```bash
  curl -H "X-API-Key: your-chosen-api-key" https://your-app-url.onrender.com/items/1
  ```

Auto-deploy is enabled by default on Render, so any changes pushed to your main branch will trigger a new deployment.
