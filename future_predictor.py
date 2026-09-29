# Module 13: Look into the Future (Target Setting & Benchmark Projections)

def forecast_future(percentage):
    print("\n--- Semester-2 Placement & Honors Forecast ---")
    if percentage >= 85:
        print("Status: Honors Eligibility Track.")
        print("Forecast: High potential for tier-1 campus placement drives in final year.")
    elif percentage >= 65:
        print("Status: Core Competency Track.")
        print("Forecast: Target reaching 75%+ in Semester 2 to qualify for major recruiter cutoffs.")
    else:
        print("Status: Remedial Support Track.")
        print("Forecast: Need dedicated focus on fundamentals in upcoming internal exams.")


def calculate_target_gap(current_percentage, target_percentage):
    # Calculates needed score jump for future semesters
    if target_percentage > current_percentage:
        gap = target_percentage - current_percentage
        print(f"Goal: You need an increase of {gap:.2f}% to reach your target of {target_percentage}%.")
    else:
        print("Goal: You have already achieved or surpassed your target score!")