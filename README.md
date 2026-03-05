# mzm_portfolio

Personal portfolio website — SvelteKit frontend deployed to AWS via Python CDK (S3 + CloudFront).

---

## Prerequisites

- Node.js
- Python 3 + pip
- AWS CLI v2 — add to PATH if using Git Bash:
  ```bash
  echo 'export PATH="/c/Program Files/Amazon/AWSCLIV2:$PATH"' >> ~/.bashrc && source ~/.bashrc
  ```
- AWS CDK: `npm install -g aws-cdk`

---

## Dev — Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## Deploy to AWS

### 1. Activate the Python venv (infrastructure)

```bash
cd infrastructure
source .venv/Scripts/activate        # Git Bash
# or: .venv\Scripts\Activate.ps1    # PowerShell
```

### 2. Install CDK dependencies

```bash
pip install -r requirements.txt
```

### 3. Build the frontend

```bash
cd ../frontend
npm run build
cd ../infrastructure
```

### 4. Bootstrap CDK (first time only, per account/region)

```bash
cdk bootstrap
```

### 5. Deploy

```bash
cdk deploy
```

CloudFront URL is printed in the output as `InfrastructureStack.PortfolioURL`.

### 6. Tear down (when not needed)

```bash
cdk destroy
```

---

## TODO

- [ ] Add project demo videos/screenshots to card image areas
- [ ] Beef up AWS Edge Automation description
- [ ] Get a custom domain and point it at CloudFront
- [ ] Update GitHub link to correct profile URL
- [ ] Replace LinkedIn URL if handle changes
- [ ] Fill in placeholder project card when ready
