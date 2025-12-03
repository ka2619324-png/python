# ---------------------------------------------------------------
# CAPSTONE PROJECT – Electricity Use Summary Dashboard
# Course: Foundations of Programming using Python
# Student: <YOUR NAME>
# Date: <CURRENT DATE>
# ---------------------------------------------------------------

import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Global variable to store combined electricity data
electricity_data = []

# Predefined CSV files
CSV_FILES = ["jan.csv", "feb.csv", "mar.csv"]


# ---------------------------------------------------------------
# FUNCTION: Load CSV Files
# ---------------------------------------------------------------
def load_csv_files():
    global electricity_data
    electricity_data = []  # Reset previous data

    for filename in CSV_FILES:
        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    row["units"] = float(row["units"])   # convert to number
                    row["date"] = datetime.strptime(row["date"], "%Y-%m-%d")
                    electricity_data.append(row)

            print(f"✔ Loaded successfully: {filename}")

        except FileNotFoundError:
            print(f"❌ File not found: {filename}")
        except Exception as e:
            print(f"Error reading {filename}: {e}")

    if electricity_data:
        print("\n✔ All data loaded successfully. Total records:", len(electricity_data))
    else:
        print("❌ No data loaded! Please make sure CSV files exist in the same folder.")


# ---------------------------------------------------------------
# FUNCTION: Usage Analysis
# ---------------------------------------------------------------
def analyze_usage():
    if not electricity_data:
        print("\n❌ No data loaded. Load CSV files first!")
        return None

    total_usage = sum(item["units"] for item in electricity_data)
    avg_usage = total_usage / len(electricity_data)

    min_usage = min(electricity_data, key=lambda x: x["units"])
    max_usage = max(electricity_data, key=lambda x: x["units"])

    # Monthly totals
    monthly_totals = {}
    for item in electricity_data:
        month = item["date"].strftime("%B")
        monthly_totals[month] = monthly_totals.get(month, 0) + item["units"]

    print("\n----------- Electricity Usage Summary -----------")
    print(f"Total Electricity Consumption: {total_usage:.2f} units")
    print(f"Average Daily Consumption: {avg_usage:.2f} units/day")
    print(f"Minimum Daily Usage: {min_usage['units']} units on {min_usage['date'].date()}")
    print(f"Maximum Daily Usage: {max_usage['units']} units on {max_usage['date'].date()}")
    print("\nMonthly Usage:")
    for month, total in monthly_totals.items():
        print(f" - {month}: {total:.2f} units")
    print("------------------------------------------------\n")

    # Return analysis for exporting
    return {
        "total_usage": total_usage,
        "avg_usage": avg_usage,
        "min_usage": min_usage,
        "max_usage": max_usage,
        "monthly_totals": monthly_totals
    }


# ---------------------------------------------------------------
# FUNCTION: Plot Usage Trend
# ---------------------------------------------------------------
def plot_usage():
    if not electricity_data:
        print("\n❌ No data loaded. Load CSV files first!")
        return

    electricity_data_sorted = sorted(electricity_data, key=lambda x: x["date"])

    dates = [item["date"] for item in electricity_data_sorted]
    units = [item["units"] for item in electricity_data_sorted]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, units, marker="o")
    plt.title("Household Electricity Usage Trend")
    plt.xlabel("Date")
    plt.ylabel("Units Consumed")
    plt.grid(True)

    plt.savefig("usage_plot.png")
    plt.show()
    print("✔ Plot saved as usage_plot.png\n")


# ---------------------------------------------------------------
# FUNCTION: Export Results
# ---------------------------------------------------------------
def export_results(analysis):
    if not electricity_data or not analysis:
        print("\n❌ Nothing to export!")
        return

    # Export combined data
    with open("electricity_summary_output.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "units"])

        for item in electricity_data:
            writer.writerow([item["date"].strftime("%Y-%m-%d"), item["units"]])

    print("✔ Exported combined data → electricity_summary_output.csv")

    # Export analysis summary
    with open("electricity_report.txt", "w") as report:
        report.write("Electricity Usage Analysis Report\n")
        report.write("----------------------------------\n")
        report.write(f"Total Usage: {analysis['total_usage']:.2f} units\n")
        report.write(f"Average Usage: {analysis['avg_usage']:.2f} units\n")
        report.write(f"Min Usage: {analysis['min_usage']['units']} units on {analysis['min_usage']['date'].date()}\n")
        report.write(f"Max Usage: {analysis['max_usage']['units']} units on {analysis['max_usage']['date'].date()}\n")

        report.write("\nMonthly Totals:\n")
        for month, total in analysis["monthly_totals"].items():
            report.write(f"{month}: {total:.2f} units\n")

    print("✔ Exported analysis report → electricity_report.txt\n")


# ---------------------------------------------------------------
# MAIN DASHBOARD MENU
# ---------------------------------------------------------------
def main_menu():
    analysis = None

    while True:
        print("\n========== ELECTRICITY USE DASHBOARD ==========")
        print("1. Load electricity data from CSV files (jan, feb, mar)")
        print("2. View usage analysis")
        print("3. Plot usage trend")
        print("4. Export results")
        print("5. Exit")
        print("================================================")

        choice = input("Enter choice (1–5): ")

        if choice == "1":
            load_csv_files()
        elif choice == "2":
            analysis = analyze_usage()
        elif choice == "3":
            plot_usage()
        elif choice == "4":
            export_results(analysis)
        elif choice == "5":
            print("Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice! Please try again.")


# Run the dashboard
main_menu()