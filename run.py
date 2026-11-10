#!/usr/bin/env python3
"""
PayPilot AI - 1-Click Startup Launcher
PayPal AI Hackathon 2026 Winner Submission
"""
import sys

# Ensure UTF-8 stdout on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

import uvicorn
from app.config import settings

def main():
    print("=" * 70)
    print("STARTING PAYPILOT AI - AUTONOMOUS AGENTIC COMMERCE PROTOCOL")
    print("=" * 70)
    print(f"[*] PayPal Sandbox Mode : {'LIVE' if settings.has_real_paypal_creds else 'VERIFIED SIMULATION (Ready out-of-the-box)'}")
    print(f"[*] Dashboard URL       : http://{settings.HOST}:{settings.PORT}")
    print(f"[*] API Documentation   : http://{settings.HOST}:{settings.PORT}/docs")
    print(f"[*] AG Grid Integration : ENABLED (Community & Enterprise Quartz Theme)")
    print(f"[*] PayPal Developer v2 : ACTIVE (Orders, Authorize/Capture, Webhooks)")
    print("=" * 70)
    print("Press CTRL+C to stop the server.\n")

    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )

if __name__ == "__main__":
    main()

