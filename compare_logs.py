from fetch_logs import fetch_all_logs
from analyze import analyze_discrepancies
from visualizer import visualize_discrepancies

def run_discrepancy_check():
    logs = fetch_all_logs()
    report = analyze_discrepancies(logs)
    visualize_discrepancies(report)
