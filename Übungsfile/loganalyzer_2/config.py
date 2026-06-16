import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT = os.path.join(BASE_DIR, 'service.json')
OUTPUT = os.path.join(BASE_DIR, 'health_report.json')



#generator.py 

NAMES = ["auth-service", "payment-api", "user-db", "test-db", "cloud-service", "website", "credential-db", "admin-db", "intranet", "test-api"]

