def collect_logs():
    failed_logins = {}
    success_logins = {}

    total_records = int(input("Enter number of login records: "))

    for i in range(total_records):
        print("\nRecord", i + 1)
        ip = input("Enter IP address: ").strip()

        if ip == "":
            print("IP cannot be empty!")
            continue

        status = input("Enter login status (SUCCESS/FAILED): ").strip().upper()

        if status == "FAILED":
            if ip in failed_logins:
                failed_logins[ip] = failed_logins[ip] + 1
            else:
                failed_logins[ip] = 1
        elif status == "SUCCESS":
            if ip in success_logins:
                success_logins[ip] = success_logins[ip] + 1
            else:
                success_logins[ip] = 1
        else:
            print("Invalid status! Record skipped.")

    return success_logins, failed_logins


def show_reports(success, failed):
    print("\nSECURITY REPORT")

    print("\nSuccessful Login Attempts:")
    if len(success) > 0:
        for ip in success:
            print(ip, "->", success[ip])
    else:
        print("No successful logins found.")

    print("\nFailed Login Attempts:")
    if len(failed) > 0:
        for ip in failed:
            print(ip, "->", failed[ip])
    else:
        print("No failed login attempts found.")


def check_flagged_ips(failed):
    print("\nSuspicious IP Addresses:")
    found_suspicious = False

    for ip in failed:
        if failed[ip] >= 3:
            print(ip, "->", failed[ip], "failed attempts")
            found_suspicious = True

    if not found_suspicious:
        print("No suspicious activity detected.")


def analyze_security(success, failed):
    print("\nANALYSIS")
    
    total_success = 0
    for count in success.values():
        total_success += count

    total_failed = 0
    for count in failed.values():
        total_failed += count

    print("Total Successful Logins:", total_success)
    print("Total Failed Logins:", total_failed)

    if total_failed > total_success:
        print("High number of failed login attempts detected.")
    else:
        print("Login activity appears normal.")


# Main program starting point
print("CYBERSECURITY LOG ANALYZER")
success_dict, failed_dict = collect_logs()

show_reports(success_dict, failed_dict)
check_flagged_ips(failed_dict)
analyze_security(success_dict, failed_dict)