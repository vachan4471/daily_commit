name: Daily Automated Commit

on:
  schedule:
    - cron: '0 12 * * *'  # Runs at 12:00 PM UTC daily
  workflow_dispatch:  # Allows manual triggering for testing

jobs:
  create-daily-commit:
    runs-on: ubuntu-latest
    name: Daily Update by 21f3001091@ds.study.iitm.ac.in

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.PAT_TOKEN }}  # Uses Personal Access Token
          fetch-depth: 0  # Ensures full history is fetched

      - name: Configure Git
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "21f3001091@ds.study.iitm.ac.in"

      - name: Create or update daily log
        run: |
          mkdir -p logs
          echo "Daily update: $(date '+%Y-%m-%d %H:%M:%S UTC')" >> logs/daily-updates.log

      - name: Commit and push changes
        run: |
          git pull --rebase origin main  # Pull latest changes before pushing
          git add logs/daily-updates.log
          git commit -m "Daily automated update $(date '+%Y-%m-%d')"
          remote_repo="https://${{ secrets.PAT_TOKEN }}@github.com/${{ github.repository }}.git"
          git push "${remote_repo}" HEAD:main
